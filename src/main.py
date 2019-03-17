from image_manipulator import merge_images_PIL, create_name_array, label_image_PIL, label_image_title_PIL
from utils import buff_number, copy_files
from os import path, open
from multiprocessing import Pool


BASE_DIR = path.join(path.dirname(__file__), '..')

FOLDER0 = BASE_DIR + "/input/RAW_SP20299"
FOLDER1 = BASE_DIR + "/input/RAW_SP20299_LPS"
FOLDER2 = BASE_DIR + "/input/RAW_LPS_SP20299"

OUTPUT_DIR = BASE_DIR + "/output_RAW"
TITLES_URI = BASE_DIR + "/input/names.txt"
name_array = create_name_array(TITLES_URI)

def merge_label_fn(x):
    print(buff_number(x))
    index = buff_number(x)

        img0 = f'{FOLDER0}{index}.jpg'
        img1 = f'{FOLDER1}{index}.jpg'
        img2 = f'{FOLDER2}{index}.jpg'

        img0_out = f'{BASE_DIR}/output_RAW/RAW_SP20299_Overlay{index}_labeled.jpg'
        img1_out = f'{BASE_DIR}/output_RAW/RAW_SP20299_LPS_Overlay{index}_labeled.jpg'
        img2_out = f'{BASE_DIR}/output_RAW/RAW_LPS_SP20299_Overlay{index}_labeled.jpg'

        label_image_title_PIL("Drug", img0, img0_out)
        label_image_title_PIL("Drug-LPS", img1, img1_out)
        label_image_title_PIL("LPS-Drug", img2, img2_out)

        output_image_uri = f'{BASE_DIR}/output_RAW/RAWDrugvDrugLPSvLPSDrug_{index}.jpg'
        merge_images_PIL([img0_out, img1_out, img2_out], output_image_uri)
        label_image_PIL(NAME_ARRAY[x-1], output_image_uri)

def merge_label_fn(x):
        print(buff_number(x))
        index = buff_number(x)

        img0 = f'{FOLDER0}{index}.jpg'
        img1 = f'{FOLDER1}{index}.jpg'
        img2 = f'{FOLDER2}{index}.jpg'

        img0_out = f'{BASE_DIR}/output_RAW/RAW_SP20299{index}_labeled.jpg'
        img1_out = f'{BASE_DIR}/output_RAW/RAW_SP20299_LPS_Overlay{index}_labeled.jpg'
        img2_out = f'{BASE_DIR}/output_RAW/RAW_LPS_SP20299_Overlay{index}_labeled.jpg'

        label_image_title_PIL("Drug", img0, img0_out)
        label_image_title_PIL("Drug-LPS", img1, img1_out)
        label_image_title_PIL("LPS-Drug", img2, img2_out)

        output_image_uri = f'{BASE_DIR}/output_RAW/RAWDrugvDrugLPSvLPSDrug_{index}.jpg'
        merge_images_PIL([img0_out, img1_out, img2_out], output_image_uri)
        label_image_PIL(NAME_ARRAY[x-1], output_image_uri)

def merge_label_parallel():
    final_img_index_minus_one = 385
    with Pool() as p:
        p.map(merge_label_fn, range(1, final_img_index_minus_one))

def copy_things():
          # Tubulin_001.jpg
    prefix = "Tubulin_"
    ext = ".jpg"
    src = "/Users/tannialau/Desktop/161126_EpD12N_CP/181113_EpD12N_Cyto/Tubulin"
    dest = "/Users/tannialau/Desktop/tannia/output"
    start = 5
    end = 365
    multiple = 24

    copy_files(prefix, ext, src, dest, start, end, multiple)


def main():
    merge_label_parallel()


main()
