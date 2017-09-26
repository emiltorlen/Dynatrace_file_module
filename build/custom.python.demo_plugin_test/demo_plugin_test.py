import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name


class BTCPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('puppet'))
        pgi_id = pgi.group_instance_id
        #stats_url = "http://localhost:8769"
        #stats = json.loads(requests.get(stats_url).content.decode())
        #self.results_builder.absolute(key='random', value=stats['random'], entity_id=pgi_id)
        #self.results_builder.relative(key='counter', value=stats['counter'], entity_id=pgi_id)
        # open("testfile.txt","w+").write("Hello")
        stats_url = "http://api.coindesk.com/v1/bpi/currentprice.json"
        stats = json.loads(requests.get(stats_url).content.decode())
        btc_value = stats['bpi']['USD']['rate_float']
        print(btc_value)
        self.results_builder.absolute(key="BTC", value=stats['bpi']['USD']['rate_float'], entity_id=pgi_id)
