from podemo.pages.login import LoginPage


class TestAddMember:
    def test_add_member(self):
        """
        添加成员用例

        :return:
        """
        page = LoginPage().login().goto_add_member().add_member()
        member = page.get_add_member_name()
        members = page.get_member()
        # print(members)
        assert member in members

    def test_add_member_fail(self):
        """
        添加成员失败用例

        :return:
        """
        # 后面再写，睡觉去
        LoginPage().login().goto_add_member().add_member_fail()
