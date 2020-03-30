# Python Modules For CMS Fits

This repository contains python modules useful for fitting with root and for CMS plot styles. The easiest way to use this
repository is with `CMSSW` later than `CMSSW_9_X`.

## Installation Instructions

Clone this git repository.

```bash
git clone https://github.com/bregnery/PythonModulesForCMSfits.git
```

### Dependencies

In order to use the programs in this repository, the following are required: Python, ROOT: Data Analysis Framework, PyROOT (https://root.cern.ch/pyroot), and numpy (python package), which are included in a CMSSW environment. To use the more advanced tools, an updated version of uproot is required. For this, a python virtual environment must be used. This repo includes a setup script for a virtual environment.

## Local Run Instructions

Examples for using this program are located in the examples directory. To use these examples, copy the python program and data file to the parent directory. To run these examples, simply do 

```bash
python ExamplePlots.py
```

The example programs can be used as a template to create more advanced fitting programs (like those in `jetHTplots.py`, `FEWZplots.py`, and `hhmcTestingPlots.py`).

## CMSSW Instructions

This repository was developed with ``CMSSW_10_2_18``. I recommend using this repository with ``CMSSW_10_X``. To install CMSSW, it is easiest to do so by using a computer with access to CVMFS. Also note, that these instructions are for bash (not tcsh or zsh).

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh 
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src/
git clone https://github.com/bregnery/PythonModulesForCMSfits.git
scram b
cmsenv
```

## Virtual Environment Instructions

From the CMSSW src directory, the python modules can be updated to latest versions in a python virtual environment. A shell script is included to streamline this process. This script will also open the venv if it already exists.

```bash
# First make sure that there is a directory to store python virtual environments. If there is not, then make one
mkdir /path/to/venvs
source ./setup_plotEnv.sh /path/to/venvs
```


