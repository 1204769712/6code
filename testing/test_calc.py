from calculator.calc import Calculator

class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    def test_add(self):
        pass

    def test_div(self):
        pass



