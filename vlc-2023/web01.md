# Basic 10
情報セキュリティ担当のジョナサンは、退職者が利用していたパソコンの通信ログを確認していたところ、Basic 認証でアクセス制限がかけられているhttp://10.10.10.6/Aw6dfLUM/ へアクセスしていることが判明しました。

提供したパソコンの通信ログ(Basic.pcapng)を確認して認証情報を探し出してください。 フラグはその Basic 認証でのログイン後のページにあります。

解答方式:flag{************}

- wiresharkを使って、Basic.pcapngを開く。
- フィルターに`http`を入力する。
- `flag`で検索して、成功したリクエストを見つける。
- `flag:aGyRsqpna3D3`という認証情報が見つかる。
- HTMLに`<h1><a href="aGyRsqpna">flag</a></h1>\n`と書かれており、それに従って以下のコマンドを実行する。

```
$ curl -u flag:aGyRsqpna3D3 http://10.10.10.6/Aw6dfLUM/aGyRsqpna  
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://10.10.10.6/Aw6dfLUM/aGyRsqpna/">here</a>.</p>
</body></html>
jio in 🌐 pop-os in ~/repo/github.com/diohabara/picopico on  main [?] via 🐍 v3.10.6 
$ curl -u flag:aGyRsqpna3D3 http://10.10.10.6/Aw6dfLUM/aGyRsqpna/
flag{d0AqEPxpZpnf}
```