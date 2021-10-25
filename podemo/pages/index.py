from selenium.webdriver.common.by import By

from podemo.pages.contact import AddMemberPage
from podemo.pages.base_page import BasePage


class IndexPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        跳转到添加成员页面

        :return:
        """
        self.driver.get(self._url)
        self.wait_for_element((By.ID, 'logout'))
        self.find((By.CSS_SELECTOR, 'span.ww_indexImg_AddMember')).click()
        return AddMemberPage(self.driver)
