#!/usr/bin/env python
"""
This script was written by Gregory Bolet for the Instructables Community

Description:
        This program was written to serve as a starting point for those
    experimenting with the Google Drive API for Python with a
    service account
"""

from __future__ import print_function
import httplib2
import os
import time
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

#####################################  PREDEFINES  #####################################
########################################################################################
#Scroll down to main() to see what is happening...

#This tells Google what API service you are trying to use (We are using drive)
#If you are backing up to gdrive, don't change this
SCOPES = 'https://www.googleapis.com/auth/drive'

#This points to the JSON key file for the service account
#You should have downloaded the file when creating your service account 
#It should be in the same directory as this script
KEY_FILE_NAME = 'my_project_key_file.json' 
########################################################################################
########################################################################################      


def get_service():
    """Get a service that communicates to a Google API.
    Returns:
      A service that is connected to the specified API.
    """
    print("Acquiring credentials...")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(filename=KEY_FILE_NAME, scopes=SCOPES)

    #Has to check the credentials with the Google servers
    print("Authorizing...")
    http = credentials.authorize(httplib2.Http())

    # Build the service object for use with any API
    print("Acquiring service...")
    service = discovery.build(serviceName="drive", version="v3", http=http, credentials=credentials)

    print("Service acquired!")
    return service


def main():
    print("This is an example script for working with a Google Drive API service account\n")

    #get the service object using the credentials file
    service = get_service()

    #Do whatever service object calls here...

    print("Requested operations complete. Exiting...\n")

if __name__ == '__main__':
    main()
