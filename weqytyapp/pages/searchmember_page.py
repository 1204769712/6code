from weqytyapp.pages.basepage import BasePage
from weqytyapp.pages.persionalinformation1_page import PersionalInformation1


class SearchMemberPage(BasePage):

    def search_member_sendkeys(self,name):
        self._params["name"] = name
        self.parse_action("../pages/searchmember_page.yaml", "search_member_sendkeys")


    def search_member_click(self):
        self.parse_action("../pages/searchmember_page.yaml","search_member_click")
        return PersionalInformation1(self.driver)

