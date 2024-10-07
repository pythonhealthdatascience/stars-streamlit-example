start_1

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10055168.svg)](https://doi.org/10.5281/zenodo.10055168)

## About the treatment centre

We have developed a computer based tool for managers of a health clinic for patients with urgent or emergency health problems.  The clinic treats patients with either:

* **Minor trauma**, e.g. impact injuries, broken bones, strains or cuts.
* **Non-trauma**, e.g. acute sickness, pain, and general feelings of being unwell.

Using the default arrival profile, patients do not require an appointment to attend the clinic. Patients arrive in an ad-hoc manner over the day, but there is a well known **pattern of peak and quiet times** throughout the day.

end_1
start_2

## Applications of the model

The computer tool allows managers to explore, test and ask questions about:

* The physical design and layout of the clinic.
* The order in which patients are seen.
* The diagnostic equipment needed by patients.
* Speed of treatments.
* Ways of speeding up the clinic processes.
* Ways of improving patient experience.

For example:

> “*What if we converted a doctors examination room into a room where nurses assess the urgency of the patients needs?*”
>
> “*What if the number of patients we treat in the afternoon doubled?*”

## How the model works

We call this type of computer model a simulation model.  The simulation model is set-up to initially copy the treatment and processes of the real health clinic.  For example, in the model the number registration booking clerks, triage rooms, and the time to treat non-trauma patients would all be based on the numbers collected **in the real world**.  All of this data is inputted into the model and a base run of the model is conducted.

The model works by **generating the arrival of synthetic patients** over a working day. The patients **follow the simple rules** the clinic has for caring for them.  For example, non-trauma patients register their details with a booking clerk then wait for to see a nurse who will determine their level of emergency.

After the model is run managers can view predictions of the performance of the model. In this study the model predicts:

* **Waiting times** for patients
* The percentage of **time that rooms and diagnostic equipment are in use**.  

end_2
start_3

## Using the model to explore different scenarios

The results from the base run of the simulation model are kept. The managers can then ask their questions and change the data used by the simulation model to be different from the real world; for example, adding an additional triage room. We call this type of ‘what-if’ use of the model an experiment. The model is again run and predictions from the experiment are compared to the base run to investigate if improvement has been achieved.

For this study we have included the following experiments:

* Increasing the number of triage rooms one;
* Increasing the number of examination capacity by one;
* Increasing the number of cubicles to treat non-trauma patients by one;
* Combining additional triage and additional examination capacity.

end_3