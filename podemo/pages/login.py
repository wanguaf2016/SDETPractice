import os

import yaml
from selenium.webdriver.common.by import By

from podemo.pages.base_page import BasePage
from podemo.pages.index import IndexPage


class LoginPage(BasePage):
    # 首页
    _url = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome'

    def login(self, count: int = 0):
        """
        登录

        :param count: 重试次数，默认 0
        :return: IndexPage
        """
        # 判断 cookies 是否存在
        if os.path.exists('../conf/cookies.yaml'):
            for i in yaml.safe_load(open('../conf/cookies.yaml')):
                self.driver.add_cookie(i)
            self.driver.get(self._url)
            return IndexPage(self.driver)
        else:
            if count == 0:
                self.driver.get(self._url)
            # 等待退出按钮出现（登录成功）
            # 疑问：以下处理违背 PO 原则吗？
            # 以下的操作：显式等待 退出 按钮出现，若退出按钮未出现（对应登录中或登录失败），则继续等待；
            # 等待次数超过三次（45 秒）则退出浏览器。此处仅退出，断言语句在用例中（貌似实际上此处已经有一些断言操作了）
            if self.wait_for_element((By.ID, 'logout'), timeout=15):
                with open('../conf/cookies.yaml', 'w') as f:
                    yaml.dump(self.driver.get_cookies(), f)
                # 传入已有的 driver，解决每次跳转页面都新建 driver 的问题
                return IndexPage(self.driver)
            # 若未登录成功，判断重试次数
            elif count < 3:
                count += 1
                # 少于三次，重试登录
                self.login(count=count)
            else:
                print('登录超时')
                self.driver.quit()
