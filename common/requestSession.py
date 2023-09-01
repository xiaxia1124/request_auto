import requests
import urllib3

from common.logs import Log


class RunMethod:
    log = Log()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def run_main(self, method, url, params=None, json=None, **kwargs):
        """
        接口调用
        :param method: get、post、delete、put
        :param url: api地址
        :param params: get请求入参
        :param json: post请求body
        :param kwargs:
        :return:
        """
        return self.session.request(method, url, params=params, json=json, verify=False, **kwargs)

    def close_session(self):
        """关闭session"""
        self.session.close()

