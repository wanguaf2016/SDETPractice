import pytest
import yaml


class TestAdd:
    def __init__(self):
        self.type = 'add'

    def get_data(self):
        with open('./data/data.yaml', 'r') as f:
            data = yaml.safe_load(f)
            return data.get(self.type).get('data')

    def get_ids(self):
        with open('./data/data.yaml', 'r') as f:
            data = yaml.safe_load(f)
            return data.get(self.type).get('ids')

    @pytest.fixture(scope='class', params=get_data(), ids=get_ids())
    def set_calculator(self, request, get_calculator):
        calc = get_calculator()
        a = request.param[0]
        b = request.param[1]
        expect = request.param[2]
        calc.set_values(a, b)
        return calc, expect

    def test_add(self, show_exe_info, set_calculator, request):
        print('测试数据：{}'.format(request.id))
        expect, calc = set_calculator()
        assert calc.add() == expect



