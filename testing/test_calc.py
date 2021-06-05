import pytest
import yaml
from calculator.calc_new import Calculator

with open(r"../datas/calc_new.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    add_datas = datas["add_datas"]
    div_datas = datas["div_datas"]
    myid = datas["myid"]

class TestCalc:

    def setup_class(self):
        print(20*'*' + "开始计算" + 20*'*')
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print(20*'*' + "结束计算" + 20*'*')

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=myid
    )
    def test_add(self,a,b,expect):
        # 调用add方法
        result = self.calc.add(a,b)
        # 判断result是浮点数，保留2位小数
        if isinstance(result,float):
            result = round(result,2)
        # 断言
        assert result == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas,ids=myid
    )
    def test_div(self,a,b,expect):
        # 调用div方法
        result = self.calc.div(a,b)
        # 断言
        assert result == expect



