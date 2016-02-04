#!/usr/bin/python

import os
import sys


def get_environment_variable(key):
    try:
        variable = os.environ[key]
    except:
        pass

    return variable


def get_environment_variable_token():
    try:
        variable = os.environ["token"]
    except:
        pass

    return variable


def get_environment_variable_mysql_passwd():
    try:
        variable = os.environ["mysql_passwd"]
    except
        pass

    return variable
