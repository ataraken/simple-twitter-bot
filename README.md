# Simple Twitter bot サービス

Azure Functions を使ったシンプルな Twitter bot です。

## Getting Started

Microsoft 社のドキュメントをご覧ください。

### Twitter へのアクセストークン

ご自身の Twitter アカウントにアクセスするため local.settings.json に値を追加してください。

```json
{
    "TWITTER_ACCESS_TOKEN": "Access Token",
    "TWITTER_TOKEN_SECRET": "Access token secret",
    "TWITTER_API_KEY": "API Key",
    "TWITTER_API_SECRET_KEY": "API secret key",
    "TWITTER_USER_ID": "Twitter User ID"
}
```

## テスト

### 前準備

ローカルで実行する場合は [requirements.txt](./requirements.txt) を使って必要な Python ライブラリをインストールしてください。
venv 環境を作り、そこで [requirements.txt](./requirements.txt) をインストールすることを推奨いたします。

### 実行

単体テストは [test フォルダ](./tests/) に保存しています。次のコマンドで実行してください。

```bash
> python -m tests.<モジュール名>
```

## デプロイ

Microsoft 社のドキュメントをご覧ください。

## Authors

* Yusuke Shinmi

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details

