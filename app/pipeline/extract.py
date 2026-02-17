import glob  # biblioteca para encontrar arquivos e diretórios usando padrões
import os    # biblioteca para manipulação de arquivos e diretórios
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler arquivos de uma pasta e retornar uma Lista de DataFrames
    args: input_path: str - caminho pasta onde estão os arquivos a serem lidos
    return: Lista de DataFrames contendo os dados dos arquivos lidos
    """
    # Encontrar todos os arquivos Excel na pasta especificada
    all_files = glob.glob(
        os.path.join(path, '*.xlsx')
    )
    # Lista para armazenar os DataFrames
    data_frame_list = (
        []
    )

    # Ler cada arquivo Excel e adicionar o DataFrame à lista
    for file in all_files:
        data_frame_list.append(
            pd.read_excel(file)
        )

    # Lançar um erro se nenhum arquivo for encontrado
    if not data_frame_list:
        raise ValueError(
            'Nenhum arquivo Excel encontrado na pasta especificada.'
        )

    return data_frame_list


if __name__ == '__main__':
    # path_dados = "data/input" # Exemplo de caminho relativo
    data_frame_list = extract_from_excel(path=r'data\input')
    print(data_frame_list)
