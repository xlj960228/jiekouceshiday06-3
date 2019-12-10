import unittest

import api
from api.api_login import ApiLogin


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiLogin对象
        cls.login = ApiLogin()

    # 登录测试方法
    def test01_login(self, mobile="13800000002", password="123456"):
        # 调用业务方法
        r = self.login.api_login(mobile, password)
        # 提取token
        token = r.json().get("data")
        api.headers["Authorization"] = "Bearer " + token
        print("登录成功后的headers值为: ", api.headers)

        # 断言

        print(r.json())
        print(r.status_code)

