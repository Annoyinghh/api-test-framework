@echo off
REM Windows 运行测试脚本

echo ========== API 自动化测试开始 ==========

REM 清理旧报告
if exist reports\allure-results rmdir /s /q reports\allure-results
if exist reports\allure-report rmdir /s /q reports\allure-report

REM 运行测试
pytest -v --alluredir=./reports/allure-results

REM 生成 Allure 报告
if %errorlevel% equ 0 (
    echo 测试执行完成，生成测试报告...
    allure generate ./reports/allure-results -o ./reports/allure-report --clean
    echo 报告生成完成，位置: ./reports/allure-report/index.html
) else (
    echo 测试执行失败
    exit /b 1
)

echo ========== API 自动化测试结束 ==========
pause
