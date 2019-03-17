from image_manipulator import merge_images_PIL, create_name_array, label_image_PIL, label_image_title_PIL, stack_images_PIL
from utils import buff_number, copy_files, clean_up_files
from os import path, open
from multiprocessing import Pool


BASE_DIR   = path.join(path.dirname(__file__), '..')
BASE_DIR_1   = path.join(path.dirname(__file__), '..', 'input_2/190314_RAW_SP20299_PerkinElmer_2/Cyto')
BASE_DIR_2 = path.join(path.dirname(__file__), '..', 'input_2/190314_RAW_SP20299_LPS_PerkinElmer_2/Cyto')

FOLDER0 = BASE_DIR_1 + "/Cyto_Nuclei/190314_RAW_SP20299_Cyto_Nuclei"
FOLDER1 = BASE_DIR_1 + "/Actin/190314_RAW_SP20299_Actin"
FOLDER2 = BASE_DIR_1 + "/Tubulin/190314_RAW_SP20299_Tubulin"
FOLDER3 = BASE_DIR_1 + "/ER/190314_RAW_SP20299_ER"
FOLDER4 = BASE_DIR_1 + "/Cyto_Overlay/190314_RAW_SP20199_Cyto_Overlay"

FOLDER5 = BASE_DIR_2 + "/Cyto_Nuclei/190314_RAW_SP20299_LPS_Nuclei"
FOLDER6 = BASE_DIR_2 + "/Actin/190314_RAW_SP20299_LPS_Actin"
FOLDER7 = BASE_DIR_2 + "/Tubulin/190314_RAW_SP20299_LPS_Tubulin"
FOLDER8 = BASE_DIR_2 + "/ER/190314_RAW_SP20299_LPS_ER"
FOLDER9 = BASE_DIR_2 + "/Cyto_Overlay/190314_RAW_SP20299_LPS_Cyto_Overlay"

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
        
        merge_images_PIL([img0_out, img1_out, img2_out, img3_out, img4_out], output_image_uri)

        img5 = f'{FOLDER5}_{index}.jpg'
        img6 = f'{FOLDER6}_{index}.jpg'
        img7 = f'{FOLDER7}_{index}.jpg'
        img8 = f'{FOLDER8}_{index}.jpg'
        img9 = f'{FOLDER9}_{index}.jpg'

        img5_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_LPS_Cyto_Nuclei_{index}_labeled.jpg'
        img6_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_LPS_Actin_{index}_labeled.jpg'
        img7_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_LPS_Tubulin_{index}_labeled.jpg'
        img8_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_LPS_ER_{index}_labeled.jpg'
        img9_out = f'{BASE_DIR}/output_PE_Exp2_Cyto/190314_RAW_SP20299_LPS_Cyto_Overlay_{index}_labeled.jpg'

        label_image_title_PIL("Nuclei", img5, img5_out)
        label_image_title_PIL("Actin", img6, img6_out)
        label_image_title_PIL("Tubulin", img7, img7_out)
        label_image_title_PIL("ER", img8, img8_out)
        label_image_title_PIL("Overlay", img9, img9_out)

        output_image_LPS_uri = f'{BASE_DIR}/output_PE_Exp2_Cyto/Cyto_LPS_Concat_{index}.jpg'
        
        merge_images_PIL([img5_out, img6_out, img7_out, img8_out, img9_out], output_image_LPS_uri)

        output_image_COMBINED_uri = f'{BASE_DIR}/output_PE_Exp2_Cyto/Cyto_LPS_Concat_COMBINED_{index}.jpg'
        
        stack_images_PIL([output_image_uri, output_image_LPS_uri], output_image_COMBINED_uri)
        # remove labeled files from hard drive
        clean_up_files([img0_out, img1_out, img2_out, img3_out, img4_out])
        clean_up_files([img5_out, img6_out, img7_out, img8_out, img9_out])
        clean_up_files([output_image_uri, output_image_LPS_uri])

        label_image_PIL(NAME_ARRAY[x-1], output_image_COMBINED_uri)

def merge_label_parallel():
    final_img_index_minus_one = 385
#     final_img_index_minus_one = 2
    with Pool() as p:
        p.map(merge_label_fn, range(1, final_img_index_minus_one))

def main():
    merge_label_parallel()


main()

