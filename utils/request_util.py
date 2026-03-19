"""
HTTP 请求封装工具
统一处理 API 请求
"""
import requests
import json
from utils.logger import log_request, log_response, log_error
from utils.yaml_util import YamlUtil

class RequestUtil:
    def __init__(self):
        self.session = requests.Session()
        self.config = YamlUtil.read_config()
        self.base_url = self.config.get('base_url', '')
        self.timeout = self.config.get('timeout', 30)

    def send_request(self, method, url, **kwargs):
        """发送 HTTP 请求"""
        # 拼接完整 URL
        if not url.startswith('http'):
            url = self.base_url + url

        # 设置默认超时
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout

        # 记录请求日志
        log_request(method, url, **kwargs)

        try:
            response = self.session.request(method, url, **kwargs)
            log_response(response)
            return response
        except Exception as e:
            log_error(f"请求失败: {str(e)}")
            raise

    def get(self, url, **kwargs):
        """GET 请求"""
        return self.send_request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        """POST 请求"""
        return self.send_request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        """PUT 请求"""
        return self.send_request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        """DELETE 请求"""
        return self.send_request('DELETE', url, **kwargs)

    def send_api_request(self, case_data):
        """根据用例数据发送请求"""
        request_data = case_data.get('request', {})
        method = request_data.get('method', 'GET').upper()
        url = request_data.get('url', '')

        # 构建请求参数
        kwargs = {}
        if 'headers' in request_data:
            kwargs['headers'] = request_data['headers']
        if 'params' in request_data:
            kwargs['params'] = request_data['params']
        if 'json' in request_data:
            kwargs['json'] = request_data['json']
        if 'data' in request_data:
            kwargs['data'] = request_data['data']

        return self.send_request(method, url, **kwargs)

# 全局请求实例
request_util = RequestUtil()
