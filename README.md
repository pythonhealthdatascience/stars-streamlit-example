[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10055169.svg)](https://doi.org/10.5281/zenodo.10055169)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100+/)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)
[<img src="https://img.shields.io/static/v1?label=dockerhub&message=images&color=important?style=for-the-badge&logo=docker">](https://hub.docker.com/r/tommonks01/treat_sim)

# Towards Sharing Tools and Artifacts for Reusable Simulation: deploying a `simpy` model as a web app

## Overview

The materials and methods in this repository support work towards developing the S.T.A.R.S healthcare framework (**S**haring **T**ools and **A**rtifacts for **R**eusable **S**imulations in healthcare).  The code and written materials here demonstrate the application of S.T.A.R.S' version 1 to sharing a `simpy` discrete-event simuilation model and associated research artifacts.  

* All artifacts in this repository are linked to study researchers via ORCIDs;
* Model code is made available under the MIT license;
* Python dependencies are managed through `conda`;
* The code builds a `streamlit` web application that can be used to run the model (web app);
* The materials are deposited and made citatable using Zenodo;
* The models are sharable with other researchers and the NHS without the need to install software.

## Author ORCIDs

[![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

## Citation

> Monks, T., & Harper, A. (2023). Towards Sharing Tools and Artifacts for Reusable Simulation: deploying a `simpy` model as a web app (v2.0.0). Zenodo. https://doi.org/10.5281/zenodo.10055169

```bibtex
@software{monks_streamlit_example,
  author       = {Monks, Thomas and
                  Harper, Alison},
  title        = {{Towards Sharing Tools and Artifacts for Reusable 
                   Simulation: deploying a `simpy` model as a web app}},
  month        = oct,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v2.0.0},
  doi 	       = {10.5281/zenodo.10055169},
  url	       = {https://doi.org/10.5281/zenodo.10055169}, 
}
```

## Funding

This code is part of independent research supported by the National Institute for Health Research Applied Research Collaboration South West Peninsula. The views expressed in this publication are those of the author(s) and not necessarily those of the National Institute for Health Research or the Department of Health and Social Care.

## Case study model

**This example is based on exercise 13 from Nelson (2013) page 170.**

> *Nelson. B.L. (2013). [Foundations and methods of stochastic simulation](https://www.amazon.co.uk/Foundations-Methods-Stochastic-Simulation-International/dp/1461461596/ref=sr_1_1?dchild=1&keywords=foundations+and+methods+of+stochastic+simulation&qid=1617050801&sr=8-1). Springer.* 

We adapt a textbook example from Nelson (2013): a terminating discrete-event simulation model of a U.S based treatment centre. In the model, patients arrive to the health centre between 6am and 12am following a non-stationary Poisson process. On arrival, all patients sign-in and are triaged into two classes: trauma and non-trauma. Trauma patients include impact injuries, broken bones, strains or cuts etc. Non-trauma include acute sickness, pain, and general feelings of being unwell etc. Trauma patients must first be stabilised in a trauma room. These patients then undergo treatment in a cubicle before being discharged. Non-trauma patients go through registration and examination activities. A proportion of non-trauma patients require treatment in a cubicle before being discharged. The model predicts waiting time and resource utilisation statistics for the treatment centre. The model allows managers to ask question about the physical design and layout of the treatment centre, the order in which patients are seen, the diagnostic equipment needed by patients, and the speed of treatments. For example: “what if we converted a doctors examination room into a room where nurses assess the urgency of the patients needs.”; or “what if the number of patients we treat in the afternoon doubled” 

## Streamlit community cloud deployment of the code

* https://stars-simpy-example.streamlit.app/

A backup and replica of the web app is available here:

* https://treat-sim.streamlit.app

> Please note that we have deployed this to the a free tier service.  If the app has not been used for a time then you will need to "wake up" the app.  Please be patient while it reboots.


## Online documentation produced by Jupyter-book

[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)

We have a separate artifact that documents the model. 

* The documentation can be access at [https://pythonhealthdatascience.github.io/stars-simpy-example-docs](https://pythonhealthdatascience.github.io/stars-simpy-example-docs)

## Docker container

A containerised version of the model is available from Dockerhub.  Follow the link and the instructions provided.  Note tht you will need docker installed in order to pull and run the container.

* https://hub.docker.com/r/tommonks01/streamlit_sim

## How to create the model interface locally

Alternatively you may wish to create the website on your local machine.  

### Downloading the code

Either clone the repository using git or click on the green "code" button and select "Download Zip".

```bash
git clone https://github.com/pythonhealthdatascience/stars-streamlit-example
```

### Installing dependencies

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-360+/)

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend install [mini-conda](https://docs.conda.io/en/latest/miniconda.html); navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

```bash
conda env create -f binder/environment.yml
```

To activate the environment issue the following command:

```bash
conda activate stars_streamlit`
```

### Running the interface to the model

In the directory (folder) containing the code issue the following command via the terminal (or cmd prompt/powershell on windows)

```bash
streamlit run Overview.py
```

This should open your browser and launch the interface automatically.  Alternatively you can navigate to the following URL.

```bash
http://localhost:8501
```

