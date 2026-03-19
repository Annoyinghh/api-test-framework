"""
日志工具模块
记录测试执行日志
"""
from loguru import logger
import sys
from pathlib import Path

# 日志目录
log_dir = Path(__file__).parent.parent / 'logs'
log_dir.mkdir(exist_ok=True)

# 移除默认处理器
logger.remove()

# 控制台输出
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# 文件输出
logger.add(
    log_dir / "test_{time:YYYY-MM-DD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="00:00",
    retention="30 days",
    encoding="utf-8"
)

# 错误日志单独记录
logger.add(
    log_dir / "error_{time:YYYY-MM-DD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="ERROR",
    rotation="00:00",
    retention="30 days",
    encoding="utf-8"
)

def log_info(message):
    """记录信息日志"""
    logger.info(message)

def log_debug(message):
    """记录调试日志"""
    logger.debug(message)

def log_warning(message):
    """记录警告日志"""
    logger.warning(message)

def log_error(message):
    """记录错误日志"""
    logger.error(message)

def log_request(method, url, **kwargs):
    """记录请求信息"""
    logger.info(f"发送请求: {method} {url}")
    if kwargs:
        logger.debug(f"请求参数: {kwargs}")

def log_response(response):
    """记录响应信息"""
    logger.info(f"响应状态码: {response.status_code}")
    logger.debug(f"响应内容: {response.text}")
