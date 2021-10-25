from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None, ele_last=None):
        """
        构造函数

        :param driver: 已有的浏览器驱动
        :param ele_last: find() 方法在调用深度查询时使用，默认为 None
        """
        self.ele_last = ele_last
        if not driver:
            self.driver = webdriver.Edge()
            self.driver.implicitly_wait(5)
            self.driver.get(self._url)
        else:
            # 复用已有 driver
            self.driver = driver

    def find(self, by: By or tuple, locator: str = None, multiple: bool = False, deep_find: bool = False):
        """
        查找元素封装
        注：若使用深度查找，且 multiple 为 True 时，再次查找时 by 只能传入定位方式(By)，locator 只能传入一个
        multiple 为 True 时，不建议对获取到的元素列表进行复杂操作

        :param deep_find: 是否需要深度查找（找到元素后在元素中继续查找），默认为 False
        :param multiple: 是否要查找多个元素，默认为 False
        :param by: 定位方式(By) 或 定位方式与定位符(tuple)
        :param locator: by为定位方式时，此为定位符
        :return: WebElement or list
        """
        if self.ele_last:
            # 深度查找逻辑
            if type(self.ele_last) == WebElement:
                ele = self.ele_last.find_elements(by, locator)
                self.ele_last = ele
                return self
            elif type(self.ele_last) == list:
                ele = []
                for i in self.ele_last:
                    ele.append(i.find_element(by, locator))
                # 原本想实现获取到元素列表后再实现链式调用，难度过大，放弃
                # 睡觉
                # self.ele_last = ele
                # return self
                return ele

        if multiple:
            # 查找多个元素
            if locator is None:
                ele = self.driver.find_elements(*by)
            else:
                ele = self.driver.find_elements(by, locator)
            if deep_find:
                self.ele_last = ele
                return self
            return ele

        if locator is None:
            ele = self.driver.find_element(*by)
        else:
            ele = self.driver.find_element(by, locator)
        if deep_find:
            self.ele_last = ele
            return self
        return ele

    def wait_for_element(self, by: By or tuple, locator: str = None, timeout: int = 10):
        """
        等待元素出现
        查看代码之后（确实忘了。。），大概找到后 until() 会直接将元素返回

        :param timeout: 超时时间，默认 10 秒
        :param by: 定位方式(By) 或 定位方式与定位符(tuple)
        :param locator: by为定位方式时，此为定位符
        :return: bool or WebElement
        """
        if locator is None:
            locator = by
        else:
            locator = (by, locator)
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def scroll_into_view(self, by: By or tuple, locator: str = None):
        """
        将页面滚动到元素可见位置

        :param by: 定位方式(By) 或 定位方式与定位符(tuple)
        :param locator: by为定位方式时，此为定位符
        :return: bool
        """
        target = self.find(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
