import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', type=int, nargs=1)
    parser.add_argument('app_id', type=int, nargs=1)
    parser.add_argument('token', type=str, nargs=1)
    args = parser.parse_args()
    return (args.id,args.app_id,args.token)

if __name__ == "__main__":
    parse_args = parse_args()
    user_id = parse_args[0]
    app_id = parse_args[1]
    token = parse_args[2]

    page = f'https://api.vk.com/method/friends.get?fields=country&fields=city&order=name&access_token={token}&v=5.131'
    req = requests.get(page).json()
    for e in req['response']['items']:
        print(e['first_name'], e['last_name'])

