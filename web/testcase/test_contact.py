from web.page.main_page import MainPage


class TestContact:

    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        username = "a01"
        account = "a01"
        phonenum = "17656787564"
        page = self.mainpage.goto_add_member()
        page.add_member(username,account,phonenum)
        names = page.get_member()
        assert username in names













