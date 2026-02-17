import pandas as pd

from app.pipeline.transform import contact_data_frames

df_1 = pd.DataFrame({"col_1": [1, 2], "col_2": [3, 4]})
df_2 = pd.DataFrame({"col_1": [5, 6], "col_2": [7, 8]})

def test_contact_data_frames():
    """
    Use o arrange, act e assert para testar a função contact_data_frames
    """
    #arrange
    data_frame_list = [df_1, df_2]
    
    # act
    df = contact_data_frames(data_frame_list)

    assert df.shape == (4, 2)
    