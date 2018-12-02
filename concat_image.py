import os

BASE_DIR = "/Users/joelau/Sites/tannia"

FOLDER0 = BASE_DIR + "/input/SP20299/Overlay"
FOLDER1 = BASE_DIR + "/input/SP20299-LPS/SP20299-LPS-Overlay"
FOLDER2 = BASE_DIR + "/input/LPS-SP20299/LPS-SP20299-Overlay"

OUTPUT_DIR = BASE_DIR + "/output"

TITLES_URI = BASE_DIR + "/input/names.txt"
FONT_URI = "/Library/Fonts/Arial\ Narrow.ttf"


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
    image_uri_array_string = reduce(
        (lambda acc, x: acc + " " + x), image_uri_array)

    concat_images_command = "convert +append " + \
        image_uri_array_string + " " \
        "-background white -splice 10x0+1080+0 " + \
        output_image_uri

    os.system(concat_images_command)


def label_image(image_uri, output_image_uri, label):
    add_label_command = 'convert ' + image_uri + ' ' +\
        '-gravity center ' + \
        '-background "#f0f0f0" ' + \
        '-font ' + FONT_URI + ' ' + \
        '-pointsize 180 ' + \
        'label:"' + label + '" ' + \
        '-append "' + output_image_uri + '"'
    print(add_label_command)
    os.system(add_label_command)


def main():
    name_array = create_name_array()

    for x in range(1, 4):
        print(buff_number(x))
        index = buff_number(x)
        img0 = FOLDER0 + index + ".jpg"
        img1 = FOLDER1 + index + ".jpg"
        img2 = FOLDER2 + index + ".jpg"
        
        img0_out = BASE_DIR + "/output/Overlay" +index + "_labeled.jpg"
        img1_out = BASE_DIR + "/output/SP20299-LPS-Overlay" +index + "_labeled.jpg"
        img2_out = BASE_DIR + "/output/LPS-SP20299-Overlay" +index + "_labeled.jpg"

        output_image_uri = BASE_DIR + "/output/DrugvDrugLPSvLPSDrug_" + index + ".jpg"

        label_image(img0, img0_out, name_array[x-1])
        label_image(img1, img1_out , name_array[x-1])
        label_image(img2, img2_out , name_array[x-1])

        merge_images([img0_out, img1_out, img2_out], output_image_uri)
main()
