import random
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from podemo.pages.base_page import BasePage


class AddMemberPage(BasePage):
    _username = ''

    def add_member(self):
        """
        添加成员

        :return:
        """
        username = '测试用户' + str(random.randint(100, 999))
        self._username = username
        acct_id = str(uuid.uuid4())
        email = f'{random.randint(0, 999)}@{random.randint(0, 999)}.c'

        self.wait_for_element((By.ID, 'username')).send_keys(username)
        self.find((By.ID, 'memberAdd_acctid')).send_keys(acct_id)
        self.find((By.ID, 'memberAdd_mail')).send_keys(email)
        # 取消 通过邮件或短信发送企业邀请 复选框
        send_invite = self.find((By.NAME, 'sendInvite'))
        if send_invite.is_selected():
            send_invite.click()
        self.find((By.CLASS_NAME, 'js_btn_save')).click()
        return ContactPage(driver=self.driver, username=username)

    def add_member_fail(self):
        """
        添加成员失败

        :return:
        """
        pass


class ContactPage(BasePage):
    def __init__(self, driver: WebDriver = None, username: str = None):
        self._username = username
        super(ContactPage, self).__init__(driver)

    def get_member(self):
        """
        获取成员列表

        :return:
        """
        # 好不容易封装出来能实现链式调用的 find 方法，不用一下有点亏。。所以定位方式写的稍复杂
        cols = self.find(by=(By.CLASS_NAME, 'member_colRight_memberTable_tr'), multiple=True, deep_find=True)
        member = cols.find(by=By.CSS_SELECTOR, locator='td:nth-child(2)')
        members = []
        for i in member:
            # print(i.tag_name)
            members.append(i.get_attribute('title'))
        return members

    def get_add_member_name(self):
        """
        获取添加的成员姓名

        :return: str
        """
        return self._username
