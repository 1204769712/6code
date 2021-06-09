from weqyapp.pages.basepage import BasePage
from weqytyapp.pages.persionalinformation2_page import PersionalInformation2


class PersionalInformation1(BasePage):

    def top_right_click(self):
        self.parse_action("persionalinformation1_page.yaml", "top_right_click")
        return PersionalInformation2(self.driver)



