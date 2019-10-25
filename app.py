import argparse
import sys

from helpers import validate_yml, validate_xml, get_xml_data, str2bool


def run(location, attr_type, screen, destination=None, ):
    """
    Runs the process of converting the yaml to XSD

    . Fetches the data from the YAML file
    . Parses to XML
    . Writes in a file
    :return:
    """
    xml = get_xml_data(location, attr_type)

    if destination:
        with open(destination, 'w') as output:
            output.writelines(xml.toprettyxml())
    if screen:
        print(xml.toprettyxml())


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
                        help="Location of the file to be saved", default=False)
    parser.add_argument('-t', dest='attr_type', type=str2bool,
                        help="Whether elements get a data type attribute.", default=True)
    parser.add_argument('-s', dest='screen', type=str2bool,
                        help="Output the result in the stdout. If this is passed in the console, the destination is mandatory",
                        default=False)

    args = parser.parse_args()

    if not args.screen and not args.destination:
        print("You must specify a destination file", file=sys.stderr)
        sys.exit(1)

    run(args.location, args.attr_type, args.screen, args.destination)
