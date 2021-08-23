# 被测代码
class Calculator:
    def __init__(self):
        self.a = object
        self.b = object

    def set_values(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """
        返回两个数相加的结果

        :return: Number
        """
        if str(self.a).isdigit() and str(self.b).isdigit():
            return self.a + self.b
        else:
            return False

    def divide(self):
        """
        返回两个数相除的结果

        :return: Number 或 False
        """
        if not (str(self.a).isdigit() and str(self.b).isdigit()):
            return False
        elif self.b == 0:
            return False
        else:
            return self.a / self.b
