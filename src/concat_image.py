import os
from functools import reduce
# from wand.image import Image
# from wand.sequence import Sequence
from PIL import Image, ImageColor, ImageDraw, ImageFont
BASE_DIR = "."

FOLDER0 = BASE_DIR + "/input/SP20299/Overlay"
FOLDER1 = BASE_DIR + "/input/SP20299-LPS/SP20299-LPS-Overlay"
FOLDER2 = BASE_DIR + "/input/LPS-SP20299/LPS-SP20299-Overlay"

OUTPUT_DIR = BASE_DIR + "/output"

TITLES_URI = BASE_DIR + "/input/names.txt"
FONT_URI = BASE_DIR + "/input/Arial_Narrow.ttf"


def buff_number(number):
    result = str(number)
    if (number < 10):
        result = "00" + str(number)
    elif (number < 99):
        result = "0" + str(number)
    return result


def create_name_array():
    file = open(TITLES_URI, "r")
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
        label_height = 100
        font_size = 100

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


def main():
    
    name_array = create_name_array()

    for x in range(1, 4):
        print(buff_number(x))
        index = buff_number(x)
        img0 = f'{FOLDER0}{index}.jpg'
        img1 = f'{FOLDER1}{index}.jpg'
        img2 = f'{FOLDER2}{index}.jpg'
        
        img0_out = f'{BASE_DIR}/output/Overlay{index}_labeled.jpg'
        img1_out = f'{BASE_DIR}/output/SP20299-LPS-Overlay{index}_labeled.jpg'
        img2_out = f'{BASE_DIR}/output/LPS-SP20299-Overlay{index}_labeled.jpg'

        output_image_uri = f'{BASE_DIR}/output/DrugvDrugLPSvLPSDrug_{index}.jpg'

        label_image_PIL(name_array[0], img0, img0_out)
        label_image_PIL(name_array[1], img1, img1_out)
        label_image_PIL(name_array[2], img2, img2_out)
        # label_image(img0, img0_out, name_array[x-1])
        # label_image(img1, img1_out , name_array[x-1])
        # label_image(img2, img2_out , name_array[x-1])

        merge_images_PIL([img0_out, img1_out, img2_out], output_image_uri)

main()
