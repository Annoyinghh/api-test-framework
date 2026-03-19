"""
Pytest 配置文件
定义全局 fixtures 和钩子函数
"""
import pytest
import allure
from pathlib import Path

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """测试环境初始化"""
    print("\n========== 测试开始 ==========")
    yield
    print("\n========== 测试结束 ==========")

@pytest.fixture(scope="function")
def api_client():
    """API 客户端 fixture"""
    from utils.request_util import request_util
    return request_util

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用例执行结果钩子
    失败时截图保存
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 用例失败时的处理
        allure.attach(
            f"用例失败: {item.name}",
            name="失败信息",
            attachment_type=allure.attachment_type.TEXT
        )
