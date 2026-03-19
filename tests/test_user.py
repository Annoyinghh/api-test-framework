"""
用户接口测试
"""
import pytest
import allure
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.yaml_util import YamlUtil
from utils.request_util import request_util
from utils.validator import validator

@allure.feature("用户模块")
class TestUserAPI:

    @pytest.mark.parametrize("case", YamlUtil.get_test_cases("user_api.yaml"))
    def test_user_api(self, case):
        """用户接口测试"""
        case_name = case.get('case_name', '')
        case_desc = case.get('name', '')

        with allure.step(f"执行用例: {case_desc}"):
            # 发送请求
            response = request_util.send_api_request(case)

            # 添加 Allure 报告信息
            allure.attach(
                case_name,
                name="用例名称",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                str(case.get('request', {})),
                name="请求信息",
                attachment_type=allure.attachment_type.JSON
            )
            allure.attach(
                response.text,
                name="响应内容",
                attachment_type=allure.attachment_type.JSON
            )

            # 验证响应
            validator.validate_response(response, case)
