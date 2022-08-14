import os
import logging
import sentry_sdk
from dotenv import load_dotenv

# .envの読み込み
load_dotenv()

# Sentryの設定
sentry_sdk.init(os.environ['SENTRY_DNS'])

logging.debug('DEBUG レベルのログ')
logging.info('INFO レベルのログ')
logging.warning('WARN レベルのログ')
logging.error('ERROR レベルのログ')

# 例外
raise Exception('エラーおきたよ！！')
