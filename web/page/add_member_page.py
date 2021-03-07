from selenium.webdriver.common.by import By

from web.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self,username,account,phonenum):
        self.find(By.ID,"username").send_keys(username)
        self.find(By.ID,"memberAdd_acctid").send_keys(account)
        self.find(By.ID,"memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return True

    def get_member(self):

        locator = (By.CSS_SELECTOR,".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(2,locator)
        eles_list = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        return names































