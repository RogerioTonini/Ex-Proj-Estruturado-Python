import os

from pipeline.extract import extract_from_excel
from pipeline.load import load_new_excel
from pipeline.transform import contact_data_frames

listas_de_data_frames = extract_from_excel(path=r'data\input')
print(listas_de_data_frames)

if __name__ == '__main__':
    data_frame_list = extract_from_excel(path=r'data\input')
    print(type(data_frame_list))

    df = contact_data_frames(listas_de_data_frames=data_frame_list)
    print(type(df))

    load_new_excel(
        data_frame=df,
        output_path=r'data\output',
        file_name='dados_consolidados.xlsx',
    )
