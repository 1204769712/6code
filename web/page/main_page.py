from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMemberPage
from web.page.base_page import BasePage





class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)


















