# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

Consistent identifier (represents all versions, resolves to latest): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10055168.svg)](https://doi.org/10.5281/zenodo.10055168)

## Unreleased

Modifications to help improve user experience and clarity of the application and repository.

### Added

* Created `scripts/` folder and moved functions to that folder (to organise repository and prevent duplication of functions between pages)
* Add `config.toml` to ensure consistent theme for users with multiple apps or global config settings
* Add `treat_sim` to environment to import model (rather than using local model file)
* Created function to set page configuration on every page of app, including NIHR logo in sidebar
* Add Zenodo badges for each version in `CHANGES.md`
* Add Andy Mayne's ORCID and STARS logo to About page
* Add Towards paper to citation page and add Amy to `CITATION.cff`
* Add more description to interactive simulation (help statements for each parameter, labelled process flow diagram, and step-by-step instructions)
* Add instructions for using the Upload experiments page (including display of template `scenarios.csv`)

### Changed

* Made files PEP-8 compliant and consistent use of " / '
* Upgraded environment to `streamlit`==1.35.0 (to use new features like `st.logo()`)
* `read_file_contents()` uses local import (to prevent accidentally importing from deprecated development branches)
* Used headings, bullets, bold text and images to Overview page to help break up paragraph of text. This includes the arrival figure which was moved from the Interactive Simulation page, as it is not used when choosing model parameters but is relevant to the overview description of the model

### Removed

* Removed `model.py`
* Removed duplicate or unused functions from `more_plot.py`
* Moved several unused files to `archive/`: `copy_table.py`, `gcp.yml`, `git_update.sh`, `more_plot.ipynb`, and `more_plot.png`
* Deleted `CHANGES.md.backup`

### Fixed

* Saved preset experiment and uploaded experiments to session state so they are not lost between page changes
* Fixed bugs with download button (where table for preset experiments disappears if click button) and copy button (which required workaround for streamlit bug) by displaying results using `st.dataframe()` which has built-in download button and is easy to copy to clipboard using `Ctrl+A`

## [v3.1.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v3.1.0) - 2024-05-26 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11316319.svg)](https://doi.org/10.5281/zenodo.11316319)

### Changed

* IMG: updated process flow image.

## [v3.0.1](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v3.0.1) - 2024-05-02 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11102678.svg)](https://doi.org/10.5281/zenodo.11102678)

### Changed

* PATCH: Tramna and non-trauma pathways updated to self internal instance of `Scenario` class as opposed to module level variable. 

### Fixed

* PATCH: Trauma patient treatment fixed to use the correct distribution and parameters

## [v3.0.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v3.0.0) - 2024-04-22 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11034479.svg)](https://doi.org/10.5281/zenodo.11034479)

### Added

* ENV: `plotly` v5.21.0 added.
* MODULE: `more_plot.py` updated to include a `more_plotly` function.
* PAGES: Creation of Resources app page. Migration of Links from About page.
* PAGES: Creation of Changes app page: logging all major, minor and patched releases of the app.

### Changed

* PAGES: Multiple replications setting moved from side bar to main window and converted to text input in 🎱 Interactive Simulation page.
* PAGES: About page cleaned up and linked to STARS main study and team.
* PAGES: Emojis 😀 added to app internal page names

### Removed

* ENV: Arrival rate and MORE plot have been migrated to be interactive `plotly` format.

## [v2.2.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v2.2.0) - 2024-04-20 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11001959.svg)](https://doi.org/10.5281/zenodo.11001959)

### Added

* PAGES: Introduce of License page 
* PAGES: Links to GitHub, Zenodo archive, Documentation and Tutorial material added to About Page

### Changed

* ENV: Upgrade `streamlit` to 1.33.0
* ENV: Upgrade `simpy` to 4.1.1

## [v2.1.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v2.1.0) - 2024-03-08 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10935920.svg)](https://doi.org/10.5281/zenodo.10935920)

### Changed

* SIM: Upgraded internal implementation of generating non-overlapping random number streams.  This is now implemented to use `np.random.SeedSequence`. See https://numpy.org/doc/stable/reference/random/parallel.html

### Removed

* PATCH: Removed deprecated use of st.@cache decorator.

## [v2.0.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v2.0.0) - 2024-03-01 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10732700.svg)](https://doi.org/10.5281/zenodo.10732700)

### Changed

* ENV: Upgraded to Python 3.10 and upgrade `numpy`, `pandas`, `matplotlib`` versions etc.
* ENV: Upgraded to streamlit `1.31.1`

### Removed

* PAGES: Removed deprecated `streamlit` functions

### Fixed

* PATCH: Fixed `st.setup_page` location in `Overview.py` (main landing page) to avoid runtime error.

## [v1.2.0](https://github.com/pythonhealthdatascience/stars-streamlit-example/releases/tag/v1.2.0) - 2023-10-30 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10055169.svg)](https://doi.org/10.5281/zenodo.10055169)

### Changed

* Updated pilot Web App release to support *Toward Sharing Tools and Artefacts for Reusable Simulations in Healthcare* project.
* GITHUB: Included detailed instructions to download the code, install dependencies and run the app locally
* GITHUB: Updated README URLs and included link to SW23 version of app redundancy.

## v1.1.0 - 2023-01-23

### Added

* Added Dockerfile that creates a python:3.8 image running the latest version of streamlit and the app on port 8989.

## v1.0.0 - 2022-07-19

:seedling: First release. Pilot Web App release to test project feasibility. The release supports [conference paper](https://www.theorsociety.com/media/7313/doiorg1036819sw23030.pdf) and talk given at the OR Society Simulation Workshop 2023 (SW23). Code can be found in separate repository.