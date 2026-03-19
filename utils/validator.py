"""
响应断言工具
验证 API 响应结果
"""
import re
import json
from jsonpath import jsonpath
from utils.logger import log_info, log_error

class Validator:
    @staticmethod
    def validate_response(response, case_data):
        """验证响应结果"""
        validate_list = case_data.get('validate', [])

        for validate_item in validate_list:
            for validate_type, validate_data in validate_item.items():
                if validate_type == 'eq':
                    Validator._validate_equal(response, validate_data)
                elif validate_type == 'contains':
                    Validator._validate_contains(response, validate_data)
                elif validate_type == 'regex':
                    Validator._validate_regex(response, validate_data)
                elif validate_type == 'jsonpath':
                    Validator._validate_jsonpath(response, validate_data)

    @staticmethod
    def _get_value(response, key):
        """获取响应中的值"""
        if key == 'status_code':
            return response.status_code
        elif key.startswith('body.'):
            json_key = key.replace('body.', '')
            try:
                body = response.json()
                keys = json_key.split('.')
                value = body
                for k in keys:
                    value = value[k]
                return value
            except:
                return None
        elif key == 'text':
            return response.text
        return None

    @staticmethod
    def _validate_equal(response, data):
        """相等断言"""
        actual_key, expected = data
        actual = Validator._get_value(response, actual_key)

        assert actual == expected, f"断言失败: {actual_key} 期望值 {expected}, 实际值 {actual}"
        log_info(f"断言成功: {actual_key} == {expected}")

    @staticmethod
    def _validate_contains(response, data):
        """包含断言"""
        actual_key, expected = data
        actual = str(Validator._get_value(response, actual_key))

        assert expected in actual, f"断言失败: {actual_key} 不包含 {expected}"
        log_info(f"断言成功: {actual_key} 包含 {expected}")

    @staticmethod
    def _validate_regex(response, data):
        """正则断言"""
        actual_key, pattern = data
        actual = str(Validator._get_value(response, actual_key))

        assert re.search(pattern, actual), f"断言失败: {actual_key} 不匹配正则 {pattern}"
        log_info(f"断言成功: {actual_key} 匹配正则 {pattern}")

    @staticmethod
    def _validate_jsonpath(response, data):
        """JSONPath 断言"""
        path, expected = data
        try:
            body = response.json()
            result = jsonpath(body, path)
            assert result and expected in result, f"断言失败: JSONPath {path} 未找到 {expected}"
            log_info(f"断言成功: JSONPath {path} 找到 {expected}")
        except Exception as e:
            log_error(f"JSONPath 断言失败: {str(e)}")
            raise

validator = Validator()
