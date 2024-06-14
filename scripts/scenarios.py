from treat_sim import model as md


def create_scenarios(df_scenarios):
    """
    Returns dictionary of Scenario object based on contents of a dataframe

    Params:
    ------
    df_scenarios: pandas.DataFrame
        Dataframe of scenarios. First two columns are id, name followed by
        variable names. No fixed width.

    Returns:
    --------
    dict

    Notes:
    -----
    No validation is currently done.  This will crash when format or variable
    names do not meet assumptions or are invalid.
    """
    cust_scenarios = {}
    for index, row in df_scenarios.iterrows():
        scenario_i = md.Scenario()
        # loop through variable names
        for var_name in df_scenarios.columns.tolist()[2:]:
            # get the value for update
            current_value = getattr(scenario_i, var_name)

            # update the variable using the relative
            setattr(scenario_i, var_name, current_value + row[var_name])

        cust_scenarios[row["name"]] = scenario_i

    return cust_scenarios
