# Auth 10
ログイン機能を作ってみました。By C 言語ルーキー

対象 IP アドレス:ポート:10.10.10.15:1001

解答方式:flag{************}

## log

````
$ nc "10.10.10.15" 1001
   _____          __  .__      
  /  _  \  __ ___/  |_|  |__   
 /  /_\  \|  |  \   __\  |  \  
/    |    \  |  /|  | |   Y  \ 
\____|__  /____/ |__| |___|  / 
        \/                 \/  

User: admin
Password: pwd
Invalid password...
```

他の問題でダウンロードしたパスワードリストを使ってみます。

```
hydra -L ./SecLists/Passwords/UserPassCombo-Jay.txt -P ./SecLists/Passwords/2020-200_most_used_passwords.txt "ftp://10.10.10.15:1001"
```