import pytest, os, yaml, requests

from common.publicMethods import json_read, to_obtain_url_param_method
from common.readFile import ReadFile
from common.login import Login

# yaml_data = ReadFile().read_yaml('yaml_path')
from common.requestSession import RunMethod

class TestDemo(object):

    def test_demo(self):
        # 创建session对象
        self.session = requests.session()
        # 登录请求
        data = json_read('/data/fc_login.json')
        # 读取登录信息
        web_login_data = to_obtain_url_param_method(platform_type='FC', api_name='fc_login', api='api')
        login_result = self.session.post(url=web_login_data['url'], json=data)
        print(login_result)
        url = 'https://ee-test.leqee.com/ee/proxy/auto-manage/web/user/system/notice/list?pageNum=1&pageSize=20'
        app_result = self.session.get(url=url)
        print(app_result)

    def test_demo2(self, login_fc):
        # self.fc_request = RunMethod()
        # data = json_read('/data/fc_login.json')
        # 读取登录信息
        # web_login_data = to_obtain_url_param_method(platform_type='FC', api_name='fc_login', api='api')
        # login = self.fc_request.run_main(method=web_login_data['method'], url=web_login_data['url'], json=data)
        get_app_list = login_fc.run_main(method='get', url='https://ee-test.leqee.com/ee/proxy/auto-manage/web/user/system/notice/list?pageNum=1&pageSize=20')
        print(get_app_list)