"""
Placing all helpers in one place
"""
import argparse
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
    if not isinstance(value, str):
        raise argparse.ArgumentTypeError('Value must be a string')
    if not value.lower().endswith(('xml', 'xml')):
        raise argparse.ArgumentTypeError('Value must be yml or xml')
    return value
