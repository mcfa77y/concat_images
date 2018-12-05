from image_manipulator import merge_images_PIL, create_name_array, label_image_PIL, label_image_title_PIL
from utils import buff_number, copy_files
from os import path, open

BASE_DIR = path.join(path.dirname(__file__), '..')

FOLDER0 = BASE_DIR + "/input/SP20299/Overlay"
FOLDER1 = BASE_DIR + "/input/SP20299-LPS/SP20299-LPS-Overlay"
FOLDER2 = BASE_DIR + "/input/LPS-SP20299/LPS-SP20299-Overlay"

OUTPUT_DIR = BASE_DIR + "/output"
TITLES_URI = BASE_DIR + "/input/names.txt"


def merge_label():


    name_array = create_name_array(TITLES_URI)

    for x in range(1, 4):
        print(buff_number(x))
        index = buff_number(x)

        img0 = f'{FOLDER0}{index}.jpg'
        img1 = f'{FOLDER1}{index}.jpg'
        img2 = f'{FOLDER2}{index}.jpg'
        
        img0_out = f'{BASE_DIR}/output/Overlay{index}_labeled.jpg'
        img1_out = f'{BASE_DIR}/output/SP20299-LPS-Overlay{index}_labeled.jpg'
        img2_out = f'{BASE_DIR}/output/LPS-SP20299-Overlay{index}_labeled.jpg'

        label_image_title_PIL(name_array[0], img0, img0_out)
        label_image_title_PIL(name_array[1], img1, img1_out)
        label_image_title_PIL(name_array[2], img2, img2_out)
       
        output_image_uri = f'{BASE_DIR}/output/DrugvDrugLPSvLPSDrug_{index}.jpg'
        merge_images_PIL([img0_out, img1_out, img2_out], output_image_uri)
        label_image_PIL("duck brothers", output_image_uri)

def copy_things():
         # Tubulin_001.jpg
        prefix = "Tubulin_"
        ext = ".jpg"
        src = "/home/joe/Desktop/ImageMappingData/Tubulin"
        dest = "/home/joe/Sites/concat_images/output/img"
        start = 5
        end = 365
        multiple = 24

        copy_files(prefix, ext, src, dest, start, end, multiple) 
def main():
       merge_label()
           

main()