# Change Log

## v3.1.0

26th May 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11316319.svg)](https://doi.org/10.5281/zenodo.11316319)

* IMG: updated process flow image.

## v3.0.1

2nd May 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11102678.svg)](https://doi.org/10.5281/zenodo.11102678)

* PATCH: Trauma patient treatment fixed to use the correct distribution and parameters
* PATCH: Tramna and non-trauma pathways updated to self internal instance of `Scenario` class as opposed to module level variable. 

## v3.0.0

22nd April 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11034479.svg)](https://doi.org/10.5281/zenodo.11034479)

* ENV: `plotly` v5.21.0 added.
* ENV: Arrival rate and MORE plot have been migrated to be interactive `plotly` format.  
* MODULE: `more_plot.py` updated to include a `more_plotly` function.
* PAGES: Multiple replications setting moved from side bar to main window and converted to text input in 🎱 Interactive Simulation page.
* PAGES: Creation of Resources app page. Migration of Links from About page.
* PAGES: Creation of Changes app page: logging all major, minor and patched releases of the app.
* PAGES: About page cleaned up and linked to STARS main study and team.
* PAGES: Emojis 😀 added to app internal page names

## v2.2.0

20th April 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11001959.svg)](https://doi.org/10.5281/zenodo.11001959)

* PAGES: Introduce of License page 
* PAGES: Links to GitHub, Zenodo archive, Documentation and Tutorial material added to About Page
* ENV: Upgrade `streamlit` to 1.33.0
* ENV: Upgrade `simpy` to 4.1.1

## v2.1.0

8th March 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10935920.svg)](https://doi.org/10.5281/zenodo.10935920)

* SIM: Upgraded internal implementation of generating non-overlapping random number streams.  This is now implemented to use `np.random.SeedSequence`. See https://numpy.org/doc/stable/reference/random/parallel.html 
* PATCH: Removed deprecated use of st.@cache decorator.

## v2.0.0

1st March 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10732700.svg)](https://doi.org/10.5281/zenodo.10732700)

* ENV: Upgraded to Python 3.10 and upgrade `numpy`, `pandas`, `matplotlib`` versions etc.
* ENV: Upgraded to streamlit `1.31.1`
* PAGES: Removed deprecated `streamlit`` functions
* PATCH: Fixed `st.setup_page` location in `Overview.py` (main landing page) to avoid runtime error.

## v1.2.0

30th October 2023

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10055169.svg)](https://doi.org/10.5281/zenodo.10055169)

* Updated pilot Web App release to support *Toward Sharing Tools and Artefacts for Reusable Simulations in Healthcare* project.
* GITHUB: Included detailed instructions to download the code, install dependencies and run the app locally
* GITHUB: Updated README URLs and included link to SW23 version of app redundancy.

## v1.1.0

23rd January 2023

* Added Dockerfile that creates a python:3.8 image running the latest version of streamlit and the app on port 8989.

## v1.0.0

19th July 2022

* Pilot Web App release to test project feasibility.
* The release supports [conference paper](https://www.theorsociety.com/media/7313/doiorg1036819sw23030.pdf) and talk given at the OR Society Simulation Workshop 2023 (SW23) 
* Code can be found in separate repository: 
