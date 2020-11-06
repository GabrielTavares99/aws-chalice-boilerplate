#! /usr/bin/env python
import json
import os

from chalice.cli import run_local_server, CLIFactory

from chalicelib.config.environment_variables import EnvironmentVariables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHALICE_CONFIG = '/'.join([BASE_DIR, '.chalice', 'config.json'])

ENV = os.environ.get('ENV', 'homolog')
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', 8000)


def set_app_env(stage):
    with open(CHALICE_CONFIG, 'r') as f:
        chalice_config_json = json.load(f)
    environment_variables = chalice_config_json['stages'][stage]['environment_variables']

    for key, value in environment_variables.items():
        EnvironmentVariables.set(key, value)


def main():
    set_app_env(ENV)
    factory = CLIFactory('./', debug=True)
    run_local_server(factory, HOST, PORT, ENV)


if __name__ == '__main__':
    main()
