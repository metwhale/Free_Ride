#点点兼职签到 
# cron 40 9 * * *
#变量 s_ddjz  api_auth_uid#api_auth_code  多账号用@分割
#const $ = new Env('久益阅读');
import os
import random
import requests
import time

def get_vars():
    data = os.getenv('s_ddjz')
    if data:
        accounts = data.split('@')
        return [dict(zip(['api_auth_uid', 'api_auth_code'], account.split('#'))) for account in accounts]
    return []

def rand_id():
    ids = ["2383", "2257", "2194", "2167", "2129", "2076", "2055", "1970", "1893", "1807"]
    return random.choice(ids)

def sign_in(full_url, id, wcs):
    post_data = {
        'id': id,
        'fblx': 1,
        'wcs': wcs,
        'theway': 'signin',
        'search': 1
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(full_url, data=post_data, headers=headers)
    return response.json()

def main():
    accounts = get_vars()
    
    for account in accounts:
        full_url = f"https://mili.shensemiao.com/index.php?v=1&appid=4&appsecret=PHPCMF19F5DF41B263B&api_auth_code={account['api_auth_code']}&api_auth_uid={account['api_auth_uid']}&s=member&app=Yhxcx&c=qd&m=sign_in"

        first_id = rand_id()
        result = sign_in(full_url, first_id, 0)
        print(f"第一次浏览：{result}")
        
        time.sleep(10)

        if result.get('msg') == '您今日已签到':
            print("今天已签到，跳过第二次浏览")
            continue

        second_id = rand_id()
        second_result = sign_in(full_url, second_id, 1)
        print(f"第二次浏览：{second_result}")

        time.sleep(10)

if __name__ == "__main__":
    main()
