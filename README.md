# Simple YAML to XML
Script converter of YAML to XML. Written in Python 3

## Example

```yaml
sample: file
list:
    example 1
    example 2
items:
    - name: example1
      price: 2

    - name: example2
      price: 3
```

Result in

```xml
<list>example 1 example 2
</list>
<sample>file</sample>
<items>
  <price>2</price>
  <name>example1</name>
</items>
<items>
  <price>3</price>
  <name>example2</name>
</items>
```

## Information
* This is a simple script that parses an YAML file to XML
* This is testing and sampling purposes but can be changed to production ready
* This should be run in an isolated python environment (virtual env)

## Requirements
* Python 3.6+
* Virtual env

## Usage
This can be executed inside any python environment 3.6+ but I would recommend creating a virtual environment for this purpose and not to break any system

For the user of virtualenv wrapper (my preference), please follow the instructions below:

1. In the command line execute `pip install virtualenvwrapper-win` and linux users `pip install virtualenvwrapper`
2. Create your virtual env `mkvirtualenv _name_at_your_choice`
3. Install the requirements inside `pip install -r requirements.txt`
4. Execute the application `python ./app.py` with the required parameters

E.g.: `python ./app.py -l <location>/<something>.yml -d <localtion>/<something>.xml`

## Parameters
* `-l` - Location of the file to be parsed (required)
* `-d` - Destination of the file with the file name after parsing (optional)
* `-t` - Whether elements get a data type attribute (defaulting to True. E.g.: `<element type="str">`)
* `-s` - Whether the output should be on the screen (defaulting to True)

You can run the result only on the screen or just destination or both

* Outputting to a file only `python ./app.py -l resources/test.yml -d resources/result.xml -t false -s false`
* Outputting to a file and screen `python ./app.py -l resources/test.yml -d resources/result.xml -t false`
* Outputting only to screen `python ./app.py -l resources/test.yml -t false`
