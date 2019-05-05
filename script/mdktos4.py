
import xml.etree.ElementTree as ET
import os
import traceback

PATH = r"E:\rt-thread\rt-thread-v4.0.0\rt-thread-4.0.0\bsp\stm32\stm32f407-atk-explorer\project.uvproj"
os.chdir(os.path.dirname(PATH))


def find_source_files(file_path=PATH):
    tree = ET.parse(file_path)
    root = tree.getroot()
    file_list =[]
    for i in root.iter("FilePath"):
        # print(i.text)
        file_list.append(os.path.abspath(i.text)+"\r")
    for i in root.iter("IncludePath"):
        if i.text:
            include_file_list = i.text.split(";")
            for j in include_file_list:
                if len(j)>2:
                    try:
                        input_file_path = os.path.abspath(j)
                        input_files = os.listdir(input_file_path)
                    except:
                        traceback.print_exc()

                    for k in input_files:
                        if ".h" in k:
                            file_list.append(os.path.join(input_file_path, k)+"\r")
                            print(os.path.join(input_file_path, k))
    return file_list


def output_file_list(input_list):
    output_file_path = PATH.replace("project.uvproj", "source_file_list.txt")
    print(output_file_path)
    with open(output_file_path, "w+") as fp:
        for i in input_list:
            fp.writelines(i)


if __name__ == '__main__':
    files = find_source_files()
    output_file_list(files)