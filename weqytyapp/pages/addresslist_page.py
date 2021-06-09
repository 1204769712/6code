
from weqytyapp.pages.basepage import BasePage
from weqytyapp.pages.searchmember_page import SearchMemberPage


class AddressListPage(BasePage):

    def search_click(self):
        # 搜索
        self.parse_action("../pages/addresslist_page.yaml","search_click")
        return SearchMemberPage(self.driver)







