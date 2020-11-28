import requests


def main():
    payload = {
        "title": "webpage title",
        "content": "content of webpage",
        "banners": [
            [600, 200],
            [400, 300],
            [100, 200]
        ]
    }

    session = requests.Session()
    session.verify = False
    result = session.post('https://localhost:8000/get_ad_replacement', data=payload)

    print(result.json)


if __name__ == '__main__':
    main()