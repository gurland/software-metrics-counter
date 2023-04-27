# software-metrics-counter
This utility helps to count software metrics and measurement based on source code

## Features
1. Count lines of code **DONE**
2. Count empty lines **DONE**
3. Count both physical and logical lines of code **DONE**
4. Count comment lines & comment level of code **DONE**
5. Cyclomatic complexity **DONE**


## Usage
In order to analyze any code base provide a github repo URL as the first argument. 
`python count_software_metrics.py https://github.com/USER/REPO.git`

- Additional argument `-d` (by default is `./src/`) is used to specify repo 
  directories to recursively search for source files, e.g. 
  `-d ./src/project/package ./tests`

- Additional argument `-e` is used to specify file extensions to analyze 
  e.g. `-e .py`


## How it works
This tool downloads a git repo to temporary directory, after that runs 
analysis using specified set of directories and extensions and represents
visual data table in your browser
