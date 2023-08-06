# Festival 10

祭りだ!祭りだ! flag を購入してね。

対象 IP アドレス:ポート:10.10.10.15:1002

解答方式:flag{************}

オーバーフローするように入力すると、flag が出てくる。

```
$ nc 10.10.10.15 1002
___________              __  .__              .__   
\_   _____/___   _______/  |_|__|__  _______  |  |  
 |    __)/ __ \ /  ___/\   __\  \  \/ /\__  \ |  |  
 |     \  ___/ \___ \  |  | |  |\   /  / __ \|  |__
 \___  / \___  >____  > |__| |__| \_/  (____  /____/
     \/      \/     \/                      \/      

Balance : 1000
==Menu==
1. Ramune : 100
2. Yakitori : 200
3. Beer : 300
4. Yakisoba : 500
5. Flag : 1000000000

Staff > What do you want to buy?
Staff > Input menu number.
 You  > 5
Staff > How many?
 You  > 10000000000
Staff > flag{gwAZLDpEHAg6}
```