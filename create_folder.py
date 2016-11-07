# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
- Purpose: creates a mysql folder (collection) entry with appropriate rights.
- Usage: from shell: source ../env/bin/activate; python ./create_folders.py
"""

import logging, os, pprint
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)
log.info( 'script started' )

FOLDER_NAME = os.environ['MAKE_FLDR__FOLDER_NAME']

FOLDER_API_URL = os.environ['MAKE_FLDR__API_URL']
FOLDER_API_AUTH_NAME = os.environ['MAKE_FLDR__API_AUTH_NAME']
FOLDER_API_AUTH_KEY = os.environ['MAKE_FLDR__AUTH_KEY']
ADDITIONAL_RIGHTS = os.environ['MAKE_FLDR__ADDITIONAL_RIGHTS']
PARENT_FOLDERS = os.environ['MAKE_FLDR__PARENT_FOLDERS']


def runCode():
    """ Creates mysql folder (collection). """
    payload = {
        'identity': FOLDER_API_AUTH_NAME,
        'authorization_code': FOLDER_API_AUTH_KEY,
        'folder_name': FOLDER_NAME,
        'additional_rights': ADDITIONAL_RIGHTS,
        'allow_duplicate_names': 'True',
        # 'description': 'folder_description_here',
        'parent_folders': PARENT_FOLDERS,
        }
    r = requests.post( settings.FOLDER_API_URL, data=payload, verify=False )
    json_string = r.content.decode( 'utf-8' )
    log.debug( 'json_string, ```{}```'.format(json_string) )
    log.debug( '-- END OF SCRIPT --' )



if __name__ == "__main__":
    log.debug( 'FOLDER_NAME, ```{}```'.format(FOLDER_NAME) )
    log.debug( 'FOLDER_API_URL, ```{}```'.format(FOLDER_API_URL) )
    log.debug( 'FOLDER_API_AUTH_NAME, ```{}```'.format(FOLDER_API_AUTH_NAME) )
    log.debug( 'FOLDER_API_AUTH_KEY, ```{}```'.format(FOLDER_API_AUTH_KEY) )
    log.debug( 'ADDITIONAL_RIGHTS, ```{}```'.format(ADDITIONAL_RIGHTS) )
    log.debug( 'PARENT_FOLDERS, ```{}```'.format(PARENT_FOLDERS) )
    runCode()
