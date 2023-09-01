import pytest

from common.logs import Log
from common.publicMethods import get_api_url_param_method, json_read


@pytest.mark.usefixtures("login_fc")
class TestNotice(object):

    def setup_class(self):
        """
        数据初始化
        :return:
        """
        self.log = Log()

    def test_notice_list(self, login_fc):
        """
        消息列表
        :param login_fc: 登录
        :return:
        """
        # 获取接口数据
        self.log.info('获取消息接口数据')
        api_data = get_api_url_param_method(platform_type='FC', api_name='fc_notice_list', api='api')
        self.log.info('获取消息接口参数')
        params = json_read('/data/fc_notice_list.json')
        get_notice_list = login_fc.run_main(method='get', url=api_data['url'], params=params)
        assert get_notice_list.json()['code'] == 200
        assert 'list' in get_notice_list.json()['result'].keys()


if __name__ == "__main__":
    pytest.main(['-s', 'test_fc_notice.py'])