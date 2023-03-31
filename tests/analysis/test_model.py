"""Tests for the regression model."""

import numpy as np
import pandas as pd
import pytest
from gambling_metrics.analysis.model import fit_did_model


@pytest.fixture()
def data():
    data = pd.DataFrame({"did_var": [0, 0, 1, 1], "outcome": [1, 2, 4, 6]})
    return data


@pytest.fixture()
def data_info():
    return {"outcome": "outcome"}


def test_fit_did_model_check_characteristics(data, data_info):
    model = fit_did_model(data, data_info, model_type="linear")
    assert np.all(model.pvalues >= 0) and np.all(model.pvalues <= 1)
    assert np.all(model.bse >= 0)


def test_fit_logit_model_error_model_type(data, data_info):
    with pytest.raises(ValueError):  # noqa: PT011
        assert fit_did_model(data, data_info, model_type="quadratic")
