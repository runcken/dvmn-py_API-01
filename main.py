import requests


LOCATIONS = ['SVO', 'London', 'Череповец']

ARGUMENTS = {
    'lang': 'ru',
    'm': '',
    'n': '',
    'q': '',
    'M': '',
    'T': ''
    }


def print_weather():
    for location in LOCATIONS:
        url = (
            'http://wttr.in/{location}'
            .format(location=location)
            )
        response = requests.get(url, params=ARGUMENTS)
        response.raise_for_status()
        print(response.text)


def main():
    print_weather()


if __name__ == '__main__':
    main()
