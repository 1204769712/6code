from weqyapp.pages.app import App
from time import sleep

class TestAddmember:

    def setup(self):
        self.app = App()

    def test_addmember(self):
        name = "a04"
        phonenum = "17656787567"
        addmemberpage = self.app.goto_main().goto_addresslist().click_addcontract().addcontract_menul()
        addmemberpage.add_member(name,phonenum)



