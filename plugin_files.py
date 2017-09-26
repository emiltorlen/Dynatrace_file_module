# import json
# import requests
# import logging
import os
import glob
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name


class FilesPlugin(BasePlugin):
    def query(self, **kwargs):
        config = kwargs["config"]
        """returns "OneAgent system monitoring" if processName is not set"""

        processName = config["processName"] if config["processName"] is not None else "OneAgent system monitoring"
        pgi = self.find_single_process_group(pgi_name(processName))
        pgi_id = pgi.group_instance_id

        #returns /etc/* if filePath is not set
        path = config["filePath"] if config["filePath"] is not None else "/etc/*"

        file_count = len([f for f in glob.glob(path) if os.path.isfile(os.path.join(path, f))])
        dirs_count = len([f for f in glob.glob(path) if os.path.isdir(os.path.join(path, f))])
        self.results_builder.absolute(key="Files", value=file_count, entity_id=pgi_id)
        self.results_builder.absolute(key="Directories", value=dirs_count, entity_id=pgi_id)