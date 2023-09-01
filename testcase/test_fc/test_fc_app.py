import pytest

from common.logs import Log
from common.publicMethods import get_api_url_param_method, json_read


@pytest.mark.usefixtures("login_fc")
class TestApp(object):

    def setup_class(self):
        """
        数据初始化
        :return:
        """
        self.log = Log()
        self.app_path = '/data/fc_app_list.json'

    def test_app_list(self, login_fc):
        """
        测试应用管理列表
        :param login_fc:
        :return:
        """
        self.log.info('获取应用列表接口数据')
        api_data = get_api_url_param_method(platform_type='fc', api_name='fc_app_list')
        self.log.info('获取应用列表接口入参')
        app_data = json_read(self.app_path)
        app_result = login_fc.run_main(api_data['method'], api_data['url'], json=app_data)

    def test_app_search_status(self, login_fc):
        """
        查询已启用的应用
        :param login_fc:
        :return:
        """
        self.log.info("获取应用列表接口数据")
        api_data = get_api_url_param_method(platform_type='fc', api_name='fc_app_list')
        self.log.info('获取应用列表接口入参')
        app_data = json_read(self.app_path)
        self.log.info('查询已启用的应用')
        app_data['status'] = 'ENABLE'
        search_status_result = login_fc.run_main(method=api_data['method'], url=api_data['url'], json=app_data)
        for i in range(len(search_status_result.json()['result']['list'])):
            assert search_status_result.json()['result']['list'][i]['status'] == 'ENABLE'

    def test_app_search_data(self, login_fc):
        """
        查询已启用的应用
        :param login_fc:
        :return:
        """
        self.log.info("获取应用列表接口数据")
        api_data = get_api_url_param_method(platform_type='fc', api_name='fc_app_list')
        self.log.info('获取应用列表接口入参')
        app_data = json_read(self.app_path)
        self.log.info('查询已启用的应用')
        app_data['status'] = 'ENABLE'
        search_status_result = login_fc.run_main(method=api_data['method'], url=api_data['url'], json=app_data)
        for i in range(len(search_status_result.json()['result']['list'])):
            assert search_status_result.json()['result']['list'][i]['status'] == 'ENABLE'

