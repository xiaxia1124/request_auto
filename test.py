import json

import websocket as websocket
import xlrd

class Common(object):
    def test(self):
        websocket.WebSocket.send(self, 'hello')
        res = websocket.WebSocket.receive()
        print(res)


class Param(object):
    def __int__(self, paramConf='{}'):
        self.paramConf = json.loads(paramConf)


class XLS(Param):
    """
    """
    def __int__(self, paramConf):
        """
        :param paramConf: xls文件路径
        :return:
        """
        self.paramConf = paramConf
        self.paramFile = self.paramConf['file']
        self.data = xlrd.open_workbook(self.paramFile)
        self.getParamSheet(self.paramConf['sheet'])