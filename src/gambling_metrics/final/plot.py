"""Functions plotting results."""

import plotly.express as px


def plot_gambling_over_time(data, data_info, group):
    """Plot different types of gambling before and after treatment.

    Args:
        data (pandas.DataFrame): The data set.
        data_info (dict): Information on data set stored in data_info.yaml. The
            following keys can be accessed:
            - 'outcome': Name of dependent variable column in data
            - 'outcome_numerical': Name to be given to the numerical version of outcome
            - 'columns_to_drop': Names of columns that are dropped in data cleaning step
            - 'categorical_columns': Names of columns that are converted to categorical
            - 'column_rename_mapping': Old and new names of columns to be renamend,
                stored in a dictionary with design: {'old_name': 'new_name'}
            - 'url': URL to data set
        predictions (pandas.DataFrame): Model predictions for different age values.
        group (str): Categorical column in data set. We create predictions for each
            unique value in column data[group]. Cannot be 'age' or 'smoke'.

    Returns:
        plotly.graph_objects.Figure: The figure.

    """
    fig = px.line(
        data,
        x="week1",
        y=group,
        color="casino",
    )

    # fig.add_traces(
    #     go.Scatter(
    #     ),
    return fig
