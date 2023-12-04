import os
import pdb
import csv
import json
import boto3
import ntpath
import socket
import logging
import datetime
import pandas as pd
from json import JSONEncoder
from botocore.exceptions import ClientError

from formats import *

def datetime_for_file(datetime_aws):
    return datetime_aws.strftime("%Y-%m-%d-%H_%M_%S")


def credential(profile_name, region_name, service):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    client = session.client(service)

    return client


def structure(parameter):
    data = {
        'Region': [], 'WorkspaceId': [], 'Eliminado': [], 'Detalles': []
    }

    if parameter == 'columna':
        col = []
        for item in data:
            col.append(item)

        return col

    return data


def create_folder(folder):
    try:
        os.mkdir(folder)
        print(folder)
    except OSError as error:
        pass

    return True


def route(profile_name, current_date, region_name):
    directory = os.getcwd()
    filename = ntpath.basename(__file__)
    folder = filename[:-3]
    create_folder(folder)
    file = "{}/{}/{}-{}-{}_{}.xlsx".format(directory, folder,
                                           folder, region_name, profile_name,
                                           datetime_for_file(current_date))

    return file
