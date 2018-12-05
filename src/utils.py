import shutil

def buff_number(number):
    result = str(number)
    if (number < 10):
        result = "00" + str(number)
    elif (number < 99):
        result = "0" + str(number)
    return result


def copy_files(prefix, extension, src_dir, dest_dir, start, end, multiple):
    for x in range (start, end, multiple):
        index = buff_number(x)
        filename = f'{prefix}{index}{extension}'
        src_uri = f'{src_dir}/{filename}'
        shutil.copy(src_uri, dest_dir)

