import argparse
import dicttoxml
from xml.dom.minidom import parseString
import os


from helpers import get_data, validate_yml, validate_xml


def run(location, destination, attr_type):
    """
    Runs the process of converting the yaml to XSD

    . Fetches the data from the YAML file
    . Parses to XML
    . Writes in a file
    :return:
    """
    data = get_data(location)
    xml = dicttoxml.dicttoxml(data, attr_type=attr_type)
    dom = parseString(xml)

    with open(destination, 'w') as output:
        output.writelines(dom.toprettyxml())


if __name__ == '__main__':
    """
    Entry point of the application.
    It will execute the program loading the file, parsing to JSON and convert to XML
    
    :params --l: Location of the file to be parsed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', dest='location', type=validate_yml,
                        help="Location of the file to be converted. It should be YML or YAML", required=True)

    parser.add_argument('-d', dest='destination', type=validate_xml,
                        help="Location of the file to be saved", required=True)

    parser.add_argument('-t', dest='attr_type', type=bool,
                        help="Whether elements get a data type attribute.", default=True)
    args = parser.parse_args()

    run(args.location, args.destination, args.attr_type)
