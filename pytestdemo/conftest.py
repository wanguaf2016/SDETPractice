import pytest

from pytestdemo.code_to_be_testing.calculator import Calculator


@pytest.fixture()
def get_calculator():
    return Calculator()


@pytest.fixture(autouse=True)
def show_exe_info():
    print('测试开始')
    yield
    print('测试结束')
