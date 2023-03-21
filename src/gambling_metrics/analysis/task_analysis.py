"""Tasks running the core analyses."""

import pandas as pd
import pytask

from gambling_metrics.analysis.model import fit_did_model
from gambling_metrics.config import BLD, SRC
from gambling_metrics.utilities import read_yaml


@pytask.mark.depends_on(
    {
        "scripts": ["model.py", "predict.py"],
        "data": BLD / "python" / "data" / "data_clean.csv",
        "data_info": SRC / "data_management" / "data_info.yaml",
    },
)
@pytask.mark.produces(BLD / "python" / "models" / "model.pickle")
def task_fit_model_python(depends_on, produces):
    """Fit a difference in difference regression model (Python version)."""
    data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    model = fit_did_model(data, data_info, model_type="linear")
    model.save(produces)


# for group in GROUPS:


#     @pytask.mark.depends_on(
#         },
#     @pytask.mark.task(id=group, kwargs=kwargs)
#     def task_predict_python(depends_on, group, produces):
