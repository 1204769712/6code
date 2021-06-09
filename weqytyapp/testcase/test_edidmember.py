from weqyapp.pages.app import App
from time import sleep

class TestEditMember:

    def setup(self):
        self.app = App()

    def test_delete_member(self):
        name = "a08"
        searchmemberpage = self.app.goto_main().goto_addresslist().search()
        searchmemberpage.search_member_sendkeys(name)
        editmemberpage = searchmemberpage.search_member_click()
        sleep(2)
        p2 = editmemberpage.top_right_click()
        p2.edit_member_click()
        editmemberpage.delete_member_click()
        editmemberpage.determine_click()










