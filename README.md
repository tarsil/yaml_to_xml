# Simple YAML to XML
-----------------------------------------------

## Information
* This is a simple script that parses an YAML file to XML
* This is testing and sampling purposes but can be changed to production ready
* This should be run in an isolated python environment (venv)

## Requirements
* Python 3.6+
* Virtual env

## How to run
This can be executed inside any python environment 3.6+ but I would recommend creating a virtual environment for this purpose and not to break any system

For the user of virtualenv wrapper (my preference), please follow the instructions below:

1. In the command line execute `pip install virtualenvwrapper-win` and linux users `pip install virtualenvwrapper`
2. Create your virtual env `mkvirtualenv _name_at_your_choice`
3. Install the requirements inside `pip install -r requirements.txt`
4. Execute the application `python ./app.py` with the required parameters

## Parameters
* `-l` - Location of the file to be parsed (required)
* `-d` - Destination of the file after parsing (required)
* `-t` - Whether elements get a data type attribute (defaulting to True. E.g.: `<element type="str">`)
