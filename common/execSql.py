from common.logs import Log
from common.readFile import ReadFile
import pymysql


class ExecSql(object):
    """
    执行sql语句
    """

    log = Log()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __int__(self):
        """
        初始化mysql配置
        """
        self.sql_conf = None

    def _get_sql_conf(self, project):
        """
        获取mysql配置
        :param project:
        :return:
        """
        try:
            return ReadFile().read_yaml('yaml_path')[project]['mysql']
        except:
            self.log.error("找不到对应项目：{0}".format(project))

    def connect_db(self):
        """
        连接mysql
        :return:
        """
        host = self.sql_conf['host']
        user = self.sql_conf['user']
        pwd = self.sql_conf['pwd']
        test_db = self.sql_conf['test_db']
        try:
            self.conn = pymysql.connect(host=host, user=user, password=pwd, db=test_db, port=3306, charset="utf-8")
        except Exception as e:
            self.log.error("连接mysql失败：{0}".format(e))

    def get_cursor(self):
        """
        获取游标
        :return:
        """
        self.cursor = self.conn.cursor()
        return self.cursor

    def exec_sql(self, project, sql_type, sql):
        """
        执行sql语句
        :param project:
        :param sql_type:
        :param sql:
        :return:
        """
        self.sql_conf = self._get_sql_conf(project)
        try:
            self.connect_db()
            if sql_type == 'select_one':
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchone()
            elif sql_type == 'select_list':
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
            elif sql_type == 'update' or sql_type == 'del' or sql_type == 'insert':
                result = self.get_cursor().execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            return result
        except Exception as e:
            self.log.error('sql执行错误：{0}'.format(e))