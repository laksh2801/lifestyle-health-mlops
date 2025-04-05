import pytest
import pandas as pd
import os

def test_data_integrity():
    data_path = os.path.join('data', 'raw', 'FINAL_LIFESTYLE_DATASET.csv')
    df = pd.read_csv(data_path)
    
    assert not df.empty, "Dataset is empty"
    assert 'BMI_Category' in df.columns, "Missing BMI_Category column"
    assert df.shape[1] >= 10, "Insufficient features"
