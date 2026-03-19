#!/bin/bash
# 运行测试脚本

echo "========== API 自动化测试开始 =========="

# 清理旧报告
rm -rf reports/allure-results
rm -rf reports/allure-report

# 运行测试
pytest -v --alluredir=./reports/allure-results

# 生成 Allure 报告
if [ $? -eq 0 ]; then
    echo "测试执行完成，生成测试报告..."
    allure generate ./reports/allure-results -o ./reports/allure-report --clean
    echo "报告生成完成，位置: ./reports/allure-report/index.html"
else
    echo "测试执行失败"
    exit 1
fi

echo "========== API 自动化测试结束 =========="
