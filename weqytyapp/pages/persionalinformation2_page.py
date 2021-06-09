from weqyapp.pages.basepage import BasePage
from weqytyapp.pages.editmember_page import EditMemberPage


class PersionalInformation2(BasePage):

    def edit_member_click(self):
        self.parse_action("../pages/persionalinformation2_page.yaml","edit_member_click")
        return EditMemberPage(self.driver)