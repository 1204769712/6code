from weqyapp.pages.addcontract_page import AddContactPage
from weqyapp.pages.basepage import BasePage


class AddressListPage(BasePage):

    def click_addcontract(self):
        self.parse_action("../pages/addresslist_page.yaml", "click_addcontact")
        return AddContactPage(self.driver)