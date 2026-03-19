# 轻量级 API 自动化测试框架

## 项目简介
为解决手动接口测试重复性高、效率低的问题，独立开发的轻量级 API 自动化测试框架，实现测试用例与数据分离、自动生成测试报告。

## 项目特点
- **数据驱动**: 采用 YAML 文件驱动测试数据，用例与数据完全分离
- **易于维护**: 非开发人员也可维护测试用例
- **自动报告**: 集成 Allure 框架，自动生成可视化测试报告
- **分层设计**: 清晰的架构分层，易于扩展和维护

## 技术栈
- Python 3.8+
- Pytest - 测试框架
- Requests - HTTP 请求库
- Allure - 测试报告框架
- YAML - 数据配置
- Git - 版本管理

## 项目结构
```
api-test-framework/
├── config/              # 配置文件
│   ├── config.yaml     # 环境配置
│   └── headers.yaml    # 请求头配置
├── testcases/          # 测试用例数据
│   ├── user_api.yaml   # 用户接口用例
│   └── order_api.yaml  # 订单接口用例
├── tests/              # 测试脚本
│   ├── test_user.py    # 用户接口测试
│   └── test_order.py   # 订单接口测试
├── utils/              # 工具模块
│   ├── request_util.py # 请求封装
│   ├── yaml_util.py    # YAML解析
│   └── logger.py       # 日志工具
├── reports/            # 测试报告
├── logs/               # 日志文件
└── pytest.ini          # Pytest配置
```

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行测试
```bash
# 运行所有测试
pytest

# 运行指定模块
pytest tests/test_user.py

# 生成 Allure 报告
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## 用例编写示例

### YAML 数据文件
```yaml
test_login:
  name: "用户登录接口测试"
  request:
    method: POST
    url: /api/v1/login
    json:
      username: "testuser"
      password: "123456"
  validate:
    - eq: [status_code, 200]
    - eq: [body.code, 0]
    - contains: [body.message, "成功"]
```

### 测试脚本
```python
@pytest.mark.parametrize("case", get_test_cases("user_api.yaml"))
def test_user_api(case):
    response = send_request(case)
    validate_response(response, case)
```

## 核心功能
- 支持 GET/POST/PUT/DELETE 等 HTTP 方法
- 支持请求头、参数、JSON 数据配置
- 支持多种断言方式（相等、包含、正则等）
- 自动记录请求响应日志
- 失败用例自动截图保存
- 支持环境切换（开发/测试/生产）

## 项目价值
- 提升接口测试效率 80%+
- 降低测试用例维护成本
- 支持持续集成/持续部署
- 可直接应用于实际项目的接口回归测试
# api-test-framework
