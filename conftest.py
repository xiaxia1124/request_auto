import pytest, os, yaml, requests

from common.logs import Log
from common.publicMethods import json_read, get_api_url_param_method
from common.requestSession import RunMethod

log = Log()


@pytest.fixture(scope="class")
def login_fc():
    """
    登录fc管理中心
    :return:
    """
    global fc_request
    fc_request = RunMethod()
    data = json_read('/data/fc_login.json')
    # 读取登录信息
    web_login_data = get_api_url_param_method(platform_type='FC', api_name='fc_login')
    try:
        login_result = fc_request.run_main(method=web_login_data['method'], url=web_login_data['url'], json=data)
        log.info('登录返回结果{}'.format(login_result))
    except Exception as e:
        log.info('登录报错{}'.format(e))
    yield fc_request

    # 读取退出登录数据
    web_logout_data = get_api_url_param_method(platform_type='FC', api_name='fc_logout')
    try:
        headers = {'X-Platform': 'freechess-manage'}
        fc_request.run_main(method=web_logout_data['method'], url=web_logout_data['url'], headers=headers)
        log.info('退出登录成功')
    except Exception as e:
        log.info('退出登录失败{}'.format(e))


@pytest.fixture(params=['one', 'two', 'three'])
def parametrized_username(request):
    return request.param


@pytest.fixture
def non_parametrized_username(request):
    return 'username'


@pytest.fixture
def username1():
    return 'username'


@pytest.fixture(scope='session',)
def other_username(username):
    return 'other-' + username


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)

