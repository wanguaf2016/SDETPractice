import logging

import allure
import pytest
import yaml


def get_data_and_ids(opr):
    with open('../data/data.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data.get(opr).get('data'), data.get(opr).get('ids')


@allure.feature('加')
class TestAdd:

    @pytest.fixture(params=get_data_and_ids('add')[0], ids=get_data_and_ids('add')[1])
    def set_calculator(self, request, get_calculator):
        calc = get_calculator()
        a = request.param[0]
        b = request.param[1]
        expect = request.param[2]
        calc.set_values(a, b)
        return calc, expect

    def test_add(self, show_exe_info, get_calculator, set_calculator, capture):
        calc, expect = set_calculator
        print('测试数据：{}'.format([calc.a, calc.b]))
        logging.info('测试数据：{}'.format([calc.a, calc.b]))
        assert calc.add() == expect
        cap_name = capture
        allure.attach.file(cap_name, name='截图', attachment_type=allure.attachment_type.PNG)


@allure.feature('除')
class TestDivide:
    @pytest.fixture(params=get_data_and_ids('divide')[0], ids=get_data_and_ids('divide')[1])
    def set_calculator(self, request, get_calculator):
        calc = get_calculator()
        a = request.param[0]
        b = request.param[1]
        expect = request.param[2]
        calc.set_values(a, b)
        return calc, expect

    @allure.story('读取数据，验证两数之商')
    @pytest.mark.run(order=1)
    def test_divide(self, show_exe_info, get_calculator, set_calculator, capture):
        calc, expect = set_calculator
        print('测试数据：{}'.format([calc.a, calc.b]))
        logging.info('测试数据：{}'.format([calc.a, calc.b]))
        assert calc.divide() == expect
        cap_name = capture
        allure.attach.file(cap_name, name='截图', attachment_type=allure.attachment_type.PNG)

    @allure.story('除以0')
    @pytest.mark.run(order=0)
    def test_divide_by_0(self, show_exe_info, get_calculator, capture):
        calc = get_calculator()
        calc.set_values(30, 0)
        assert calc.divide() is False
        cap_name = capture
        allure.attach.file(cap_name, name='截图', attachment_type=allure.attachment_type.PNG)
