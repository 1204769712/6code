from weqyapp.pages.basepage import BasePage


class AddMemberPage(BasePage):

    def add_member(self,name,phonenum):
        self._params["name"] = name
        self._params["phonenum"] = phonenum
        self.parse_action("../pages/addmember_page.yaml","add_member")


