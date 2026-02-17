import os
import pandas as pd

def load_new_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Receber um Dataframe e salvar como excel

    args: data_frame (pd.DataFrame): dataframe a ser salvo como excel
    output_path (str): caminho onde o arquivo serrá salvo
    file_name (str): nome do arquivo a ser salvo

    return: "Arquivbo salvo com sucesso" ou "Erro ao salvar o arquivo"
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except Exception as e:
        return f"Erro ao criar o diretório: {e}"
    
    try:
        data_frame.to_excel(f"{output_path}/{file_name}", index=False)
        return "Arquivo salvo com sucesso"
    except Exception as e:
        return f"Erro ao salvar o arquivo: {e}"