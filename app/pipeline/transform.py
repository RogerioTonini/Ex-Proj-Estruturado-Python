import pandas as pd

from typing import List

def contact_data_frames(listas_de_data_frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Transforma uma lista de dataframes em um único dataframe
    """
    return pd.concat(listas_de_data_frames, ignore_index=True)
