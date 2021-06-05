from weqyapp.pages.addresslist_page import AddressListPage
from weqyapp.pages.basepage import BasePage


class InformationPage(BasePage):

    def goto_addresslist(self):
        self.parse_action("../pages/information_page.yaml", "goto_addresslist")
        return AddressListPage(self.driver)

