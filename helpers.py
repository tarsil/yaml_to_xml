"""
Placing all helpers in one place
"""
import argparse
from xml.dom.minidom import parseString

import dicttoxml
import yaml


def get_data(file_path):
    """
    Loads the file from a location and returns the structure, the file is in YML
    and is converted to a dict
    :param file_path:
    :return: dict (treated as the same as JSON in python)
    """
    with open(file_path) as inf:
        content = yaml.load(inf, Loader=yaml.Loader)
    return content


def get_xml_data(location, attr_type):
    """
    Get the data and parses to XML
    :param location: location of the file
    :return: xml str
    """
    data = get_data(location)
    xml = dicttoxml.dicttoxml(data, attr_type=attr_type)
    return parseString(xml)


def validate_yml(value):
    """
    Validates if teh file is in YAML or YML and it's a string
    :param value: string location of the file
    :return: value
    """
    if not isinstance(value, str):
        raise argparse.ArgumentTypeError('Value must be a string')
    if not value.lower().endswith(('yml', 'yaml')):
        raise argparse.ArgumentTypeError('Value must be yml or yaml')
    return value


def validate_xml(value):
    """
    Validates if teh file is in YAML or YML and it's a string
    :param value: string location of the file
    :return: value
    """
    if isinstance(value, bool):
        return value

    if not isinstance(value, str):
        raise argparse.ArgumentTypeError('Value must be a string')
    if not value.lower().endswith(('xml', 'xml')):
        raise argparse.ArgumentTypeError('Value must be yml or xml')
    return value


def str2bool(value):
    """
    Parses a string to a boolean
    """
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
