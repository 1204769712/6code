from weqyapp.pages.basepage import BasePage


class EditMemberPage(BasePage):

    def delete_member_click(self):
        self.parse_action("../pages/editmember_page.yaml","delete_member_click")

    def determine_click(self):
        self.parse_action("../pages/editmember_page.yaml", "determine_click")

    