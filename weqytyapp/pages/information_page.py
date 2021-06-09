from weqytyapp.pages.addresslist_page import AddressListPage
from weqytyapp.pages.basepage import BasePage


class InformationPage(BasePage):

    def goto_addresslist(self):
        # 进入通讯录
        self.parse_action("../pages/information_page.yaml", "goto_addresslist")
        return AddressListPage(self.driver)

