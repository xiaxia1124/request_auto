import json
import os.path

import requests
import yaml

from common.readFile import ReadFile


class Run(object):
    def __int__(self):
        self.session = requests.session()

    def run(self, method, url, data, params, **kwargs):
        return self.session.request(method=method, url=url, params=params, json=data, **kwargs)

    def close_session(self):
        self.session.close()


def get_method_url(paltform, api_name, api='api'):
    paltform = paltform.upper()
    yaml_data = ReadFile().read_yaml(paltform)[paltform]
    url = yaml_data['host']+yaml_data[api_name][api]
    method = yaml_data[api_name]['method']
    return {"method": method, "url": url}


class ReadFile(object):
    def __int__(self):
        self.fc_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/fc_api.yaml')

    def read_yaml(self, path):
        with open(path, encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.Loader)

    def read_json(self,path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
