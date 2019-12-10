
import unittest
from tools.HTMLTestReportCN import HTMLTestRunner

# 新建测试套件
suite = unittest.defaultTestLoader.discover("./scripts")



with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)
