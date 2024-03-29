import pandas as pd
import pytest
from gambling_metrics.config import TEST_DIR
from gambling_metrics.data_management import clean_data
from gambling_metrics.utilities import read_yaml


@pytest.fixture()
def data():
    return pd.read_csv(TEST_DIR / "data_management" / "data_fixture.csv")


@pytest.fixture()
def data_info():
    return read_yaml(TEST_DIR / "data_management" / "data_info_fixture.yaml")


def test_clean_data_drop_columns(data, data_info):
    data_clean = clean_data(data, data_info)
    assert not set(data_info["columns_to_drop"]).intersection(set(data_clean.columns))


def test_clean_data_dropna(data, data_info):
    data_clean = clean_data(data, data_info)
    assert not data_clean.isna().any(axis=None)


def test_clean_data_categorical_columns(data, data_info):
    data_clean = clean_data(data, data_info)
    for cat_col in data_info["categorical_columns"]:
        cat_col = data_info["column_rename_mapping"].get(cat_col, cat_col)
        assert data_clean[cat_col].dtype == "category"


def test_clean_data_column_rename(data, data_info):
    data_clean = clean_data(data, data_info)
    old_names = set(data_info["column_rename_mapping"].keys())
    new_names = set(data_info["column_rename_mapping"].values())
    assert not old_names.intersection(set(data_clean.columns))
    assert new_names.intersection(set(data_clean.columns)) == new_names
