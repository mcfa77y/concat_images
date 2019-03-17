from image_manipulator import merge_images_PIL, create_name_array, label_image_PIL, label_image_title_PIL, stack_images_PIL
from utils import buff_number, copy_files, clean_up_files
from os import path, open
from multiprocessing import Pool


BASE_DIR = path.join(path.dirname(__file__), '..')

FOLDER0 = BASE_DIR + "/input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto/Cyto_Nuclei/190314_RAW_SP20299_Cyto_Nuclei"
FOLDER1 = BASE_DIR + "/input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto/Actin/190314_RAW_SP20299_Actin"
FOLDER2 = BASE_DIR + "/input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto/Tubulin/190314_RAW_SP20299_Tubulin"
FOLDER3 = BASE_DIR + "/input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto/ER/190314_RAW_SP20299_ER"
FOLDER4 = BASE_DIR + "/input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto/Cyto_Overlay/190314_RAW_SP20199_Cyto_Overlay"

OUTPUT_DIR = BASE_DIR + "/output_PE_Exp2_Cyto"
TITLES_URI = BASE_DIR + "/input/SP20299_names.txt"
name_array = create_name_array(TITLES_URI)

NAME_ARRAY = create_name_array(TITLES_URI)

def merge_label_fn(x):
        print(buff_number(x))
        index = buff_number(x)

        img0 = f'{FOLDER0}_{index}.jpg'
        img1 = f'{FOLDER1}_{index}.jpg'
        img2 = f'{FOLDER2}_{index}.jpg'
        img3 = f'{FOLDER3}_{index}.jpg'
        img4 = f'{FOLDER4}_{index}.jpg'

        img0_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20199_Cyto_Nuclei_{index}_labeled.jpg'
        img1_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_Actin_{index}_labeled.jpg'
        img2_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_Tubulin_{index}_labeled.jpg'
        img3_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_ER_{index}_labeled.jpg'
        img4_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_Cyto_Overlay_{index}_labeled.jpg'

        label_image_title_PIL("Nuclei", img0, img0_out)
        label_image_title_PIL("Actin", img1, img1_out)
        label_image_title_PIL("Tubulin", img2, img2_out)
        label_image_title_PIL("ER", img3, img3_out)
        label_image_title_PIL("Overlay", img4, img4_out)

        output_image_uri = f'{BASE_DIR}/output_PE_Exp2_Cyto/Cyto_Concat_{index}.jpg'
        stack_images_PIL([img0_out, img1_out, img2_out, img3_out, img4_out], output_image_uri)
        clean_up_files([img0_out, img1_out, img2_out, img3_out, img4_out])
        label_image_PIL(NAME_ARRAY[x-1], output_image_uri)

def merge_label_parallel():
    final_img_index_minus_one = 2
#     final_img_index_minus_one = 385
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

