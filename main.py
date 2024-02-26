import requests

def link(token):
    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    }

    response = requests.post("https://discord.com/api/v9/users/@me/invites", headers=headers)

    if response.status_code == 200:
        invite_code = response.json()["code"]
        print(f"こちらがフレンド申請のリンクです: discord.gg/{invite_code}")
    else:
        print(f"エラーが発生しました: {response.text}")

token = input("tokenを入力してください: ")

link(token)
