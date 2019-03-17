from os import path
from functools import reduce
from PIL import Image, ImageColor, ImageDraw, ImageFont

BASE_DIR = path.join(path.dirname(__file__), '..')
FONT_URI = BASE_DIR + "/input/Arial_Narrow.ttf"

# https://en.wikipedia.org/wiki/Web_colors
# https://coolors.co/4392f1-008080-ffffff-262626-dc493a color palet generator

BACKGROUND_COLOR = ImageColor.getrgb('#262626')
# BACKGROUND_COLOR = ImageColor.getrgb('black')
TEXT_COLOR = ImageColor.getrgb('teal')

def create_name_array(names_uri):
    file = open(names_uri, "r")
    name_array = []
    for name in file.readlines():
        name_array.append(name.strip('\n'))
    file.close()
    return name_array

def merge_images_PIL(image_uri_array, output_image_uri):
    # space on left and right of merged images
    x_offset = 0
    # space on top and below merged images
    y_offset = 0
    # space between images
    x_between = 10

    # open images and collect heights and widths to calc max width
    images = map(Image.open, image_uri_array)
    widths, heights = zip(*(img.size for img in images))

    total_width = sum(widths) + (len(image_uri_array)) * x_offset
    max_height = max(heights) + 2 * y_offset

    # create new image to hold merge images
    new_img = Image.new('RGB', (total_width, max_height), BACKGROUND_COLOR)

    # have to get images again because they close after initial use
    images = map(Image.open, image_uri_array)
    for img in images:
        new_img.paste(img, (x_offset, y_offset))
        x_offset += img.width + x_between

    new_img.save(output_image_uri)

      
def stack_images_PIL(image_uri_array, output_image_uri):  
    # space on left and right of merged images
    x_offset = 0
    # space on top and below merged images
    y_offset = 0
    # space between images
    y_between = 10

    # open images and collect heights and widths to calc max width
    images = map(Image.open, image_uri_array)
    widths, heights = zip(*(i.size for i in images))
    
    total_height = sum(heights) + (len(image_uri_array)) * x_offset
    max_width = max(widths) + 2 * y_offset

    # create new image to hold merge images
    new_im = Image.new('RGB', (max_width, total_height), BACKGROUND_COLOR)

    # have to get images again because they close after initial use
    images = map(Image.open, image_uri_array)
    for im in images:
        new_im.paste(im, (x_offset, y_offset))
        y_offset += im.height + y_between

    new_im.save(output_image_uri)

def create_label(label_text, label_width, font_size=120, font_color=TEXT_COLOR, x_offset=10, y_offset=10):
  buffer = 30
  label_height = font_size + buffer

  # make a blank image for the text
  label_img = Image.new('RGBA', (label_width, label_height), BACKGROUND_COLOR)

  # get a font
  fnt = ImageFont.truetype(FONT_URI, font_size)
  # get a drawing context
  label_draw = ImageDraw.Draw(label_img)
  label_draw.text((x_offset,y_offset), label_text, font=fnt,fill=font_color)
  return label_img

def label_image_PIL(label, image_uri, output_image_uri=None):
    with Image.open(image_uri) as img:
        label_img = create_label(label, img.width)

        # image holder
        new_img = Image.new('RGB', (img.width, img.height + label_img.height), BACKGROUND_COLOR)
        # paste image in image holder
        new_img.paste(img)
        # paste label in image holder
        new_img.paste(label_img, (0, img.height))

        # save image
        if (output_image_uri == None):
            new_img.save(image_uri)
        else:
            new_img.save(output_image_uri)

def label_image_title_PIL(label, image_uri, output_image_uri=None):
    with Image.open(image_uri) as img:
        label_img = create_label(label, img.width)

        # image holder
        new_img = Image.new('RGB', (img.width, img.height + label_img.height), BACKGROUND_COLOR)
        # paste label in image holder
        new_img.paste(label_img)
        # paste image in image holder
        new_img.paste(img, (0, label_img.height))

        # save image
        if (output_image_uri == None):
            new_img.save(image_uri)
        else:
            new_img.save(output_image_uri)


# functions for using terminal image manipulation 'convert'

def label_image(image_uri, output_image_uri, label):
    add_label_command = f'convert {image_uri} \
        -gravity center \
        -background "#f0f0f0" \
        -font {FONT_URI} \
        -pointsize 180 \
        label:"{label}" \
        -append "{output_image_uri}"'


    # print(add_label_command)
    os.system(add_label_command)


def merge_images(image_uri_array, output_image_uri):
    image_uri_array_string = reduce((lambda acc, x: acc + " " + x), image_uri_array)

    concat_images_command = f'convert +append {image_uri_array_string} \
        -background white \
        -splice 10x0+1080+0 \
        {output_image_uri}'

    os.system(concat_images_command)
