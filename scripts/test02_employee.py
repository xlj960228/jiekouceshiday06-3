import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_commom import assert_common


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.api = ApiEmployee()

    # 新增员工
    def test01_post(self, username="xlj960228", mobile="15848681858",workNumber="960415"):
        # 调用新增接口
        r = self.api.api_post_employee(username, mobile, workNumber)
        print("新增员工后结果为: ", r.json())
        # 提取url
        api.user_id = r.json().get("data").get("id")
        print("新增的员工id为: ", api.user_id)
        # 断言
        assert_common(self,r)
    # 更新员工
    def test02_put(self):
        pass
    # 查询员工
    def test03_get(self):
        pass
    # nihao

    # 删除
    def test04_delete(self):
        # 调用删除接口
        r = self.api.api_delete_employee(api.user_id)
        print("删除数据结果为: ",r.json())
        # 断言
        assert_common(self,r)

        # 我不会


        # 烦人