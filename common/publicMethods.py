import json
import os.path

from common.readFile import ReadFile


def get_api_url_param_method(platform_type, api_name, api='api'):
    """
    根据结果获取URL, 参数， method, header
    :param platform_type: 业务线缩写 如fc
    :param api_name: yaml定义接口名称
    :param api: yaml对应api
    :param token: 登录返回的token
    :return:
    """
    platform_type = platform_type.upper()
    #  获取yaml文件数据
    yaml_data = ReadFile().read_yaml(platform_type)[platform_type]
    # 获取url
    url = yaml_data['host'] + yaml_data[api_name][api]
    # 获取method
    method = yaml_data[api_name]['method']
    return {'url': url, 'method': method}


def json_read(json_file):
    """
    json文件读取
    :param json_file: json文件路径
    :return: json数据
    """
    open_file = os.path.join(os.path.dirname(os.path.dirname(__file__)) + json_file)
    with open(open_file, "r", encoding='utf-8') as f:
        read_data = json.load(f)
    return read_data