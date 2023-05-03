# ameblo-notify-v2
* maintainer: [Asha](https://github.com/asha-ndf)
* 試験運用中
* 追記予定
## 概要
* [SSSRCのアメブロ](https://ameblo.jp/sssrc/)に新規投稿があれば、TwitterとSlackに自動投稿するBotです。
* TwitterのAPI変更に伴い新しくしました。

## セットアップ
### ローカル
* `pip install -r requiremnts.txt`で必要なパッケージをインストールしてください。
* [.env_example](.env_example)を参考に`.env`を作成してください。
* `ACCESS_TOKEN`と`ACCESS_TOKEN_SECRET`が未発行の場合は、`init.py`を実行して発行してください。
### GitHub上
* `.env`の環境変数をGitHub Secretに設定してください。


## 注意
* `.env`や`.token`はgitignoreしていますが、誤って鍵を載せることの無いように注意してください。