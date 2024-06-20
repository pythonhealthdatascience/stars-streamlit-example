from treat_sim import model as md


def label_results(df):
    """
    Sets dataframe index as a column and replaces with more descriptive labels

    Parameters:
    -----------
    df : pd.dataframe
        Dataframe where the index has each of the result names

    Returns:
    --------
    res : pd.dataframe
        Resultant dataframe with relabelled index as first column
    """
    # Rename column
    res = df.rename_axis("Result").reset_index()
    # Relabel values using labels from package
    res["Result"] = res["Result"].map(md.RESULT_LABELS)
    return res
