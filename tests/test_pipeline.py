import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.pipeline.transform import concat_dataframe

df1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def testar_concat():
    """use o arrange, act e assert para testar a função concat_dataframe"""
    # Arrange
    data_frame_list = [df1,df2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # Act
    df = concat_dataframe(data_frame_list)

    # Assert
    assert df.shape == (4,2)
    assert data_frame.equals(df)
    
