from os import path
from functools import reduce
from PIL import Image, ImageColor, ImageDraw, ImageFont


BASE_DIR = path.join(path.dirname(__file__), '..')

FONT_URI = BASE_DIR + "/input/Arial_Narrow.ttf"

def create_name_array(names_uri):
    file = open(names_uri, "r")
    name_array = []
    for name in file.readlines():
        name_array.append(name.strip('\n'))
    file.close()
    return name_array


def merge_images(image_uri_array, output_image_uri):
    image_uri_array_string = reduce((lambda acc, x: acc + " " + x), image_uri_array)
    
    concat_images_command = f'convert +append {image_uri_array_string} \
        -background white \
        -splice 10x0+1080+0 \
        {output_image_uri}'

    os.system(concat_images_command)

def merge_images_PIL(image_uri_array, output_image_uri):  
    # space on left and right of merged images
    x_offset = 0
    # space on top and below merged images
    y_offset = 0
    # space between images
    x_between = 10

    # open images and collect heights and widths to calc max width
    images = map(Image.open, image_uri_array)
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths) + (len(image_uri_array)) * x_offset
    max_height = max(heights) + 2 * y_offset

    # create new image to hold merge images
    new_im = Image.new('RGB', (total_width, max_height), ImageColor.getrgb('white'))

    # have to get images again because they close after initial use
    images = map(Image.open, image_uri_array)
    for im in images:
        new_im.paste(im, (x_offset, y_offset))
        x_offset += im.width + x_between

    new_im.save(output_image_uri)
        
        
def label_image_PIL(label, image_uri, output_image_uri=None):        
    
    with Image.open(image_uri) as img:
        font_size = 120
        label_height = font_size + 30

        # make a blank image for the text
        label_img = Image.new('RGBA', (img.width, label_height), ImageColor.getrgb('white'))

        # get a font
        fnt = ImageFont.truetype(FONT_URI, font_size)
        # get a drawing context
        label_draw = ImageDraw.Draw(label_img)
        label_draw.text((10,10),label, font=fnt,fill=(0,0,255,128))

        # image holder 
        new_img = Image.new('RGB', (img.width, img.height + label_img.height), ImageColor.getrgb('white'))
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
        font_size = 120
        buffer = 30
        label_height = font_size + buffer

        # make a blank image for the text
        label_img = Image.new('RGBA', (img.width, label_height), ImageColor.getrgb('white'))

        # get a font
        fnt = ImageFont.truetype(FONT_URI, font_size)
        # get a drawing context
        label_draw = ImageDraw.Draw(label_img)
        label_draw.text((10,10),label, font=fnt,fill=(0,0,255,128))

        # image holder 
        new_img = Image.new('RGB', (img.width, img.height + label_img.height), ImageColor.getrgb('white'))
        # paste label in image holder
        new_img.paste(label_img)
        # paste image in image holder
        new_img.paste(img, (0, label_img.height))

        # save image
        if (output_image_uri == None):
            new_img.save(image_uri)
        else:
            new_img.save(output_image_uri)


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


