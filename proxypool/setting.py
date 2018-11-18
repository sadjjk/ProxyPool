# Redis数据库地址
REDIS_HOST = 'XX.XXX.XX.XXX'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'XXXX'

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 60
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 5000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 600

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5000

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 50
