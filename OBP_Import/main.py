#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__ = [' Jan Alexander Slabiak (alex@tesobe.com)']
__license__ = """
  Copyright 2011 Music Pictures Ltd / TESOBE

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
import libs.to_utf8
import obp_import_post_bank
import obp_config

def import_from_postbank_testuser():
    #import obp_postbank_get_csv
    #csv_file = os.path.join(obp_postbank_get_csv.csv_save_path,obp_postbank_get_csv.csv_files[0])
    return None

    
def main():

    #csv_file = obp_config.CSV_FILE_PATH
    libs.to_utf8.main(csv_file)
    obp_import_post_bank.main(csv_file)




if __name__ == '__main__':
    main()

