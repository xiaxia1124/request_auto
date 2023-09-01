# import requests
#
#
# class Common(object):
#     def __int__(self,  url_boot):
#         self.url_root = url_boot
#
#     def get(self, uri, params=''):
#         url = self.url_root + uri + params
#         res = requests.get(url)
#         return res
#
#     def post(self, uri, params):
#         url = self.url_root + uri
#         if len(params) > 0:
#             res = requests.post(url, data=params)
#         else:
#             res = requests.post(url)
#         return res
#
#
# url_boot = "https://auto-manage-test.leqee.com/"
# com = Common(url_boot)
# com.get('/')
# import time
# from functools import wraps
#
#
# def timelog(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start =time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, func.__module__, end-start)
#         # return result
#     return wrapper
#
#
# @timelog
# def countdown(n):
#     while n > 0:
#         n-=1
#         print(n)
#
#
# countdown(2)

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


print(add(1, 2))



import pytest

# @pytest.fixture
# def parametrized_username():
#     print("fixture1")
#     return 'overridden-username'


@pytest.fixture(params=['one', 'two', 'three'])
def non_parametrized_username(request):
    print(request.param)
    return request.param


def test_username(parametrized_username):
    assert parametrized_username == 'overridden-username1'


def test_parametrized_username(non_parametrized_username):
    print(non_parametrized_username)
    assert non_parametrized_username in ['one', 'two', 'three']


@pytest.mark.parametrize('username1', ['directly-overridden-username',"aa"])
def test_username(username1):
    print(username1)
    assert username1 in ['directly-overridden-username',"aa"]


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(other_username):
    assert other_username == 'other-directly-overridden-username-other'





@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)


def test_0(otherarg):
    print("  RUN test0 with otherarg", otherarg)


def test_1(modarg, a=1):
    print(a)
    print("  RUN test1 with modarg", modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))

class Fruit:
    def __init__(self, name):

        self.name = name

def __eq__(self, other):
    return self.name == other.name



import pytest


class App:
    def __init__(self, smtp_connection):
        self.smtp_connection = smtp_connection


@pytest.fixture(scope="module")
def app(smtp_connection):
    return App(smtp_connection)


@pytest.mark.parametrize("app", ['aaa'])
def test_smtp_connection_exists(app):
    assert app in ['aaa']


@pytest.fixture(scope="function")
def monitor_init():
    print("可以用这行代替之前框架的setUp")
    a = 1
    yield a
    print("可以用这行代替之前框架的tearDown")

@pytest.mark.usefixtures("monitor_init")
@pytest.mark.usefixtures("parametrized_username")
def test_one():
    print("执行用例A")


# 上面这一段等同于
def test_one1(monitor_init):
    print("执行用例A", monitor_init)