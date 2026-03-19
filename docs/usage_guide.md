# API 自动化测试框架使用指南

## 环境准备

### 1. 安装 Python
确保安装 Python 3.8 或更高版本

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 安装 Allure（可选）
```bash
# macOS
brew install allure

# Windows
scoop install allure

# 或下载安装包
https://github.com/allure-framework/allure2/releases
```

## 配置说明

### 环境配置 (config/config.yaml)
```yaml
env: test  # 当前环境：dev/test/prod

environments:
  test:
    base_url: http://test-api.example.com
    timeout: 30
```

### 请求头配置 (config/headers.yaml)
```yaml
default:
  Content-Type: application/json
  Authorization: Bearer your_token
```

## 编写测试用例

### 1. 创建 YAML 数据文件
在 `testcases/` 目录下创建 YAML 文件：

```yaml
test_example:
  name: "接口测试示例"
  request:
    method: POST
    url: /api/v1/example
    json:
      key: value
  validate:
    - eq: [status_code, 200]
    - eq: [body.code, 0]
```

### 2. 创建测试脚本
在 `tests/` 目录下创建测试文件：

```python
import pytest
from utils.yaml_util import YamlUtil
from utils.request_util import request_util
from utils.validator import validator

@pytest.mark.parametrize("case", YamlUtil.get_test_cases("example.yaml"))
def test_example(case):
    response = request_util.send_api_request(case)
    validator.validate_response(response, case)
```

## 断言方式

### 相等断言
```yaml
validate:
  - eq: [status_code, 200]
  - eq: [body.code, 0]
```

### 包含断言
```yaml
validate:
  - contains: [body.message, "成功"]
```

### 正则断言
```yaml
validate:
  - regex: [body.phone, "^1[3-9]\\d{9}$"]
```

### JSONPath 断言
```yaml
validate:
  - jsonpath: ["$.data.user_id", "123"]
```

## 运行测试

### 命令行运行
```bash
# 运行所有测试
pytest

# 运行指定文件
pytest tests/test_user.py

# 运行指定标记
pytest -m smoke

# 并行运行
pytest -n 4
```

### 脚本运行
```bash
# Linux/Mac
./run_tests.sh

# Windows
run_tests.bat
```

## 查看报告

### Allure 报告
```bash
# 生成并打开报告
allure serve ./reports/allure-results
```

### HTML 报告
```bash
pytest --html=./reports/report.html
```

## 最佳实践

1. **用例命名**: 使用清晰的命名，如 `test_user_login_success`
2. **数据分离**: 测试数据放在 YAML 文件中，保持代码简洁
3. **断言充分**: 验证关键字段，确保接口正确性
4. **日志记录**: 充分利用日志功能，便于问题排查
5. **环境隔离**: 不同环境使用不同配置，避免污染数据

## 常见问题

### Q: 如何切换测试环境？
A: 修改 `config/config.yaml` 中的 `env` 字段

### Q: 如何添加认证信息？
A: 在 `config/headers.yaml` 中配置 Authorization 头

### Q: 如何处理依赖接口？
A: 使用 pytest fixture 或在用例中保存响应数据

## 持续集成

### Jenkins 集成
```groovy
stage('API Test') {
    steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest --alluredir=./reports/allure-results'
        allure includeProperties: false,
               jdk: '',
               results: [[path: 'reports/allure-results']]
    }
}
```

### GitHub Actions 集成
```yaml
- name: Run API Tests
  run: |
    pip install -r requirements.txt
    pytest --alluredir=./reports/allure-results
```
