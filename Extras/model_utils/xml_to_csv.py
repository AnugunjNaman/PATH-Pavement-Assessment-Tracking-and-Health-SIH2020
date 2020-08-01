import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    c = 0
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            print(member[0].text, xml_file)
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member.find('name').text,
                     int(member.find('bndbox')[0].text),
                     int(member.find('bndbox')[1].text),
                     int(member.find('bndbox')[2].text),
                     int(member.find('bndbox')[3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    base = 'C:\\Users\\naman\\OneDrive\\Documents\\Tensorflow\\'
    image_path = os.path.join(base + 'workspace\\training_demo\\images\\test')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv(base + 'workspace\\training_demo\\annotations\\test_record.csv' , index=None)
    print('Successfully converted xml to csv.')


main()