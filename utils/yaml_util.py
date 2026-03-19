"""
YAML 文件解析工具
读取测试用例数据
"""
import yaml
import os
from pathlib import Path

class YamlUtil:
    @staticmethod
    def read_yaml(file_path):
        """读取 YAML 文件"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def read_testcase(case_name):
        """读取测试用例文件"""
        testcase_dir = Path(__file__).parent.parent / 'testcases'
        file_path = testcase_dir / case_name
        return YamlUtil.read_yaml(file_path)

    @staticmethod
    def read_config():
        """读取配置文件"""
        config_dir = Path(__file__).parent.parent / 'config'
        config_path = config_dir / 'config.yaml'
        return YamlUtil.read_yaml(config_path)

    @staticmethod
    def get_test_cases(yaml_file):
        """获取所有测试用例"""
        data = YamlUtil.read_testcase(yaml_file)
        cases = []
        for case_name, case_data in data.items():
            case_data['case_name'] = case_name
            cases.append(case_data)
        return cases
