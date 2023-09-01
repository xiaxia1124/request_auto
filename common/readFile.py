import os.path
import yaml, xlrd, xlwt
from common.logs import Log


class ReadFile(object):
    log = Log()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/testcase.xls')
        self.sql_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/sql.yaml')
        self.fc_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/fc_api.yaml')

    def read_yaml(self, path_type):
        """
        读取yaml文件
        :param path_type:
        :return:
        """
        try:
            if path_type == 'FC':
                file_path = self.fc_yaml_path
            elif path_type == 'SQL':
                file_path = self.sql_yaml_path
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.Loader)
        except Exception as e:
            self.log.error("读取yaml文件报错{}".format(e))

    def read_excel(self, sheet_name, function, casename=None):
        """
        读取excel文件
        :param sheet_name:
        :param function: 表格中function列数据值
        :param casename:  表格中casename列数据值
        :return:
        """
        try:
            book = xlrd.open_workbook(self.excel_path)
            sheet = book.sheet_by_name(sheet_name)
            param = []
            for i in range(0, sheet.nrows):
                if casename == None:
                    if sheet.row_values(i)[0] == function and sheet.row_values(i)[3] == 1:
                        param.append(sheet.row_values(i))
                else:
                    if sheet.row_values(i)[0] == function and sheet.row_values(i)[1] == casename and sheet.row_values(i)[3] == 1:
                        param.append(sheet.row_values(i))
            return param
        except Exception as e:
            self.log.error("读取excel文件报错{}".format(e))

