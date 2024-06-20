The "🎱 Interactive simulation" page allowed you to run one scenario at a time. This page enables you to get the results from multiple scenarios, compared in a single table.

## Create a scenario CSV file

To run these experiments, you need to upload a CSV file containing a table of parameters. In the table, each row is a scenario, and each column is an argument for the model Scenario() object.

> See [stars-treat-sim/treat_sim/model.py]({url}) for a full list of parameters that you can vary in each scenario.

For each scenario, values are interpreted as **relative changes** to parameters from their default values.

**Resource counts are bounded at 0** - you will therefore get an error if you set the count to be too low.

### Template

This template varies four parameters:

* **n_triage** - the number of triage cubicles - default: {n_triage}
* **n_exam** - the number of examination rooms - default: {n_exam}
* **n_cubicles_1** - the number of non-trauma treatment cubicles - default: {n_cubicles_1}
* **exam_mean** - the mean length of examination (min) - default: {exam_mean}
* **n_trauma** - number of trauma bays for stabilisation - default: {n_trauma}

Hover over the table to view **download** button in top right corner.