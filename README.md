# sentry-practice-with-python-01 - sentryのテスト
## Setup & Run
/src/.envファイルを作成し、SENTRYのDNSを下記の通り記載
```
SENTRY_DNS='ここにSENTRYのDNS'
```

dockerコンテナを起動
```
docker-compose up -d
```

dockerコンテナに入る
```
docker exec -it sentry-test /bin/bash
```

python実行
```
python sentry-test.py
```

## Reference source
* [エラー監視には Sentry が超便利！](https://qiita.com/Chanmoro/items/a9cbde57fd6c0926b5b4)

