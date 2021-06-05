import allure
import pytest
import yaml


with open(r"../datas/calc_new.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    add_datas = datas["add_datas"]
    div_datas = datas["div_datas"]
    sub_datas = datas["sub_datas"]
    mul_datas = datas["mul_datas"]
    myid = datas["myid"]

@pytest.fixture(params=sub_datas,ids=myid)
def get_datas(request):
    # print("开始计算")
    data = request.param
    print(f"减法的测试数据:{data}")
    yield data
    # print("计算结束")

@allure.feature("测试计算器")
class TestCalc:

    @allure.story("测试加法")
    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=myid
    )
    @pytest.mark.run(order=1)
    def test_add(self,calc_init,get_calc,a,b,expect):
        print(f"加法的测试数据：{a,b,expect}")
        # 调用加法add方法
        with allure.step("计算两个数相加"):
            result = get_calc.add(a,b)
        # 判断result是浮点数，保留2位小数
        if isinstance(result,float):
            result = round(result,2)
        # 断言
        assert result == expect

    @allure.story("测试除法")
    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas,ids=myid
    )
    @pytest.mark.run(order=4)
    def test_div(self,calc_init,get_calc,a,b,expect):
        print(f"除法的测试数据：{a, b, expect}")
        # 调用除法div方法
        with allure.step("计算两个数相除"):
            result = get_calc.div(a,b)
        # 断言
        assert result == expect

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_sub(self,calc_init,get_calc,get_datas):
        # print(f"减法的测试数据：{get_datas}")
        # 调用减法sub方法
        with allure.step("计算两个数相减"):
            result = get_calc.sub(get_datas[0], get_datas[1])
        # 判断result是浮点数，保留2位小数
        if isinstance(result,float):
            result = round(result,2)
        # 断言
        assert result == get_datas[2]

    @allure.story("测试乘法")
    @pytest.mark.parametrize(
        "a,b,expect",
        mul_datas,ids=myid
    )
    @pytest.mark.run(order=3)
    def test_mul(self,calc_init,get_calc,a,b,expect):
        print(f"乘法的测试数据：{a, b, expect}")
        # 调用乘法mul方法
        with allure.step("计算两个数相乘"):
            result = get_calc.mul(a, b)
        # 判断result是浮点数，保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == expect









