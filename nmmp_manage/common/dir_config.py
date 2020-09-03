# --^_^-- coding:utf-8 --^_^--
# @Remark:路径配置

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 日志目录
logs_dir = os.path.join(base_dir, "output/logs")

# 截屏目录
screenshot_dir = os.path.join(base_dir, "output/screenshots")

# 测试数据目录
testdatas_dir = os.path.join(base_dir, "pages/datas")

# 测试用例目录
testcases_dir = os.path.join(base_dir, "cases")

# 测试报告目录
htmlreport_dir = os.path.join(base_dir, "output/reports")
