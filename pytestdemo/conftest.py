import time

import pytest
from PIL import ImageGrab

from pytestdemo.code_to_be_testing.calculator import Calculator


@pytest.fixture(scope='class')
def get_calculator():
    return Calculator


@pytest.fixture(autouse=True)
def show_exe_info():
    print('测试开始')
    yield
    print('测试结束')


@pytest.fixture()
def capture(request):
    """
    截图

    :return:
    """
    # root_dir = request.config.rootdir
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    pic_name = '.\\output\\capture\\{}.png'.format(now)
    im = ImageGrab.grab()
    im.save(pic_name, 'png')
    # print(root_dir + pic_name[1:])
    return str(pic_name)


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    root_dir = request.config.rootdir
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = root_dir + '/cases/output/logs/{}.log'.format(now)
    print(log_name)
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)
