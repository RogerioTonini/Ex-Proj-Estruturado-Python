from typing import List

import pandas as pd


def contact_data_frames(
    listas_de_data_frames: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    Transforma uma lista de dataframes em um único dataframe
    """
    return pd.concat(listas_de_data_frames, ignore_index=True)
