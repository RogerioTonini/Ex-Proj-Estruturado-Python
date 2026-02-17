from pipeline.extract import extract_files_excel

listas_de_data_frames =  extract_files_excel(path=r"data\input")
print(listas_de_data_frames)

# import os

# from pipeline.extract import extract_files_excel

# if __name__ == "__main__":
#     path_dados = "data/input" # Exemplo de caminho relativo
#     dados = extract_files_excel(path_dados)
#     print(dados)