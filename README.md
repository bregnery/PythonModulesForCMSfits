# Python Modules For CMS Fits

This repository contains python modules useful for fitting with root and for CMS plot styles. The easiest way to use this
repository is with ``CMSSW_9_X``.

## Installation Instructions

Clone this git repository.

```bash
git clone https://github.com/bregnery/PythonModulesForCMSfits.git
```

### Dependencies

In order to use the programs in this repository, the following are required: Python, ROOT: Data Analysis Framework, PyROOT (https://root.cern.ch/pyroot), and numpy (python package). All of these dependencies are included in a CMSSW environment.

## Local Run Instructions

Examples for using this program are located in the examples directory. To use these examples, copy the python program and data file to the parent directory. To run these examples, simply do 

```bash
python ExamplePlots.py
```

The example programs can be used as a template to create more advanced fitting programs (like those in FEWZplots.py and hhmcTestingPlots.py).

## CMSSW Instructions

This repository was build with ``CMSSW_9_4_8``. I recommend using this repository with ``CMSSW_9_X``.

```bash
cmsrel CMSSW_9_4_8
cd CMSSW_9_4_8/src/
git clone https://github.com/bregnery/PythonModulesForCMSfits.git
scram b
cmsenv
```
