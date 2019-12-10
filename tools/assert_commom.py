def assert_common(self, response, status_code=200, msg="操作成功！"):
    # 状态码  200
    self.assertEqual(status_code, response.status_code)
    # 断言  success
    self.assertTrue(response.json().get("success"))
    # 断言 code
    self.assertEqual(10000, response.json().get("code"))
    # 断言  msg
    self.assertEqual(msg, response.json().get("message"))
