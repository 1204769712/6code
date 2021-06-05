from weqyapp.pages.addmember_page import AddMemberPage
from weqyapp.pages.basepage import BasePage


class AddContactPage(BasePage):

    def addcontract_menul(self):
        self.parse_action("../pages/addcontact_page.yaml", "addcontact_menual")
        return AddMemberPage(self.driver)
