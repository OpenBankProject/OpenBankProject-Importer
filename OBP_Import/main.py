#!/usr/bin/env python
# -*- coding: utf-8 -*
__doc__ = """
This is the main program.
It gets a CSV file from Postbank and then inserts it via
the Scala Lift API to the Database backend.

Dependencies: Scala API
at: https://github.com/OpenBankProject/OpenBankProject-Server
"""

__author__ = [' Jan Alexander Slabiak (alex@tesobe.com)']
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

import os
import sys
import obp_config
import libs.to_utf8
import libs.postbank_get_csv
import libs.import_helper
import libs.csv_importer

from libs.debugger import logger
from time import sleep


def get_transactions_from_bank_as_csv(username, password):
    """
    Imports a csv from Postbank, calls the postbank_get_csv file and
    starts the Selenium Browser (Firefox) to access Postbank.
    Returns the full path to the csv file.
    """

    # TODO: When no username and password is set, use the demo login.
    # Clean up the OBP temp folder (delete all csv files there).
    logger.info("Setting csv_folder...") #E.S. Can't this call be moved to 
	#E.S. within postbank_get_csv.get_csv_with_selenium, and avoid having to pass it back to the same lib?
    csv_folder = libs.postbank_get_csv.check_for_clean_tmp() 
    logger.debug("csv_folder is: %s" % csv_folder)

    # Get a new csv file using selenium
    logger.debug("About to start Selenium, with csv_path")
    libs.postbank_get_csv.get_csv_with_selenium(csv_folder, username, password)

    # Now check that one file exists in the folder and return its name
    logger.info("Getting the csv_file...")
    csv_file = libs.import_helper.check_and_return_csv_file_name(csv_folder)
    logger.debug("csv_file is: %s " % csv_file)

    # Now return the full path of the file.
    #E.S. 'csv/'? <- "magic number". Should this be csv_folder?
    csv_path = os.path.join(obp_config.TMP, 'csv/', csv_file)
    logger.debug("joining csv_file and TMP to: %s" % csv_path) #E.S. again, the ref to TMP
    logger.debug("returning csv_path: %s" % csv_path)
    return csv_path


def transactions_to_obp(username, password):
    """
    Retrieves the csv from postbank and posts it to the OpenBankProject server
    """

    # TODO: Some of this functionality should probably move inside the csv parser/importer.
    #       This function should in theory only call two functions:
    #       1. get_transactions_from_bank_as_csv()
    #       2. push_csv_to_obp(csv)
    #
    #       Any complexities should then be handled by those functions
    # (y.a.)
    # Getting the raw CSV file from PostBank.
    logger.info("start transactions_to_obp and calling get_transactions_from_bank_as_csv")
    unconverted_file = get_transactions_from_bank_as_csv(username, password)
    logger.info("Get csv_path, not UTF-8")

    # We need to convert it to UTF-8. Otherwise Python can't work with it.
    logger.info("converting unconverted_file to UTF-8")
    csv_file = libs.to_utf8.main(unconverted_file)
    logger.debug("csv_file with UTF-8 is: %s" % csv_file)

    # Before we can read the CSV, we remove all empty newlines.
    # Otherwise the CSV Parser stops working.
    logger.info("Removing all unused newlines.")
    libs.import_helper.remove_empty_lines(csv_file)

    # Now read the file and push it to the Scala API
    # TODO: It would be better, when we just getting the JSON back and
    # then we can decide how to insert. #E.S. eh?
    logger.info("Converting to JSON, inserting to Scala API")
    libs.csv_importer.main(csv_file)

    # Clean up and remove all files.
    # TODO: using the tempfile library might be much more efficient/clean.
    #       (y.a.)
    libs.postbank_get_csv.check_for_clean_tmp()
    libs.import_helper.clean_up(obp_config.TMP)


def main():
    """
    This will make sure that the password has at least 5 characters.
    (Checks like this should probably move inside the function,
    although they might not be at all necessary.
    Use error handling for incorrect auth instead. y.a.)
    """
    logger.info("Starting OpenBankProject-Importer")
    logger.debug("Version: %s " % obp_config.OBP_VERSION)
    logger.debug("SCALA_HOST: %s " % obp_config.SCALA_HOST)
    logger.debug("SCALA_PORT: %s " % obp_config.SCALA_PORT)

    logger.info("Getting login information")
    login_data = libs.import_helper.set_bank_account_login()

    logger.info("Start endless while loop")
    # Will start a endless while loop. This will  start Firefox, controlled by
    # Selenium to fetch the CSV from Postbank.
    # TODO: Need handling of System signals to run this as a daemon.
    while True:
        try:
            transactions_to_obp(login_data[0], login_data[1])
            # TODO: Need another exception for not getting the CSV File.
            # wait 10 minutes
            sleep(10 * 60)

        except KeyboardInterrupt:
                logger.critical("KeyboardInterrupt!")
                logger.critical("Caught Ctrl-C from user")
                raise
        except Exception, e:
            # TODO: need a cleanup as well, just to be sure no sensitive data left on the disk.
            logger.error("Something went wrong")
            logger.error("Error is:\n%s" % e)
            logger.error("restart in 60 seconds")
            print "%s:Something went wrong" % libs.import_helper.date_now_formatted()
            print "%s:Error is:\n%s" % (libs.import_helper.date_now_formatted(), e)
            # When something went wrong wait 1 minute.
            sleep(60)


if __name__ == '__main__':
    main()
