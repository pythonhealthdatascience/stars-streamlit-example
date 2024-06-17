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
    res = df.rename_axis("Result").reset_index()
    labels = {
        "00_arrivals": "Total arrivals",
        "01a_triage_wait": "Wait time for triage bay",
        "01b_triage_util": "Utilisation of triage bay",
        "02a_registration_wait": "Wait time for registration clerk",
        "02b_registration_util": "Utilisation of registration clerk",
        "03a_examination_wait": "Wait time for exam room (non-trauma)",
        "03b_examination_util": "Utilisation of exam room (non-trauma)",
        "04a_treatment_wait(non_trauma)": (
            "Wait time for treatment cubicle (non-trauma)"),
        "04b_treatment_util(non_trauma)": (
            "Utilisation of treatment cubicle (non-trauma)"),
        "05_total_time(non-trauma)": (
            "Total time patients spent at centre (non-trauma)"),
        "06a_trauma_wait": "Wait time for room for stabilisation (trauma)",
        "06b_trauma_util": (
            "Utilisation of room for stabilisation (trauma)"),
        "07a_treatment_wait(trauma)": (
            "Wait time for treatment cubicle (trauma)"),
        "07b_treatment_util(trauma)": (
            "Utilisation of treatment cubicle (trauma)"),
        "08_total_time(trauma)": (
            "Total time patients spent at centre (trauma)"),
        "09_throughput": "Model throughput"}
    res["Result"] = res["Result"].map(labels)
    return res
