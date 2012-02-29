# -*- coding: utf-8 -*-
# Server Settings:
__author__ = ['Jan Alexander Slabiak (alex@tesobe.com)']
__license__ = """
  Copyright 2011/2012 Music Pictures Ltd / TESOBE

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

__doc__ = """
This file sets some importer options:
Here you are able to set the Host and Port configuration of
your Database or API.
"""


#from libs.import_helper import show_here
from libs.debugger import logger
from os import path
from os import getcwd
# Currently unused but approved.
MONGODB_SERVER = 'obp_mongod'
MONGODB_SERVER_PORT = 27017


#MongoDB Setting
# Name of the Database and the Mongo Collection.
# How to setup a MongoDB:
# LINK: http://www.mongodb.org/display/DOCS/Quickstart
MONGODB_DATABASE = 'OBP006'
MONGODB_COLLECTION = 'obptransactions'

# The importer version
OBP_VERSION = '0.0.1'

# Files:
# The folder where the CSV file gets saved
SAVEDIR = ''
TMP = path.join(getcwd(), 'tmp/')
TMP_CSV_SUFFIX= "csv"  # TODO: Adapt to files. 

# This can be used to specify a local CSV file.
# TODO: When this file is define. Don't run the postbank_importer
CSV_FILE_PATH = 'usr/PB_Umsatzauskunft_198_rows.csv'
# There is also the alternative of using a HTML file. This
# would get parsed with BeautifulSoup and insert to the MongoDB

HTML_FILE_PATH = ''

# This sets the hostname and port of the Scala API.
SCALA_HOST = 'localhost' #E.S : better to call this API_HOST?
SCALA_PORT = '8080' #E.S : better to call this API_PORT?

# Defines a file where the sha512 hashes of transactions get saved. The hash
# values are used to detect transactions that have already been imported.
HASH_FILE = 'var/cache'


# Logger Settings
# Define Path and Debug level.
