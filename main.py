import requests


cities = ['svo', 'london', 'череповец']


def get_weather():
    for city in cities:
        url = (
            'http://wttr.in/{city}?lang=ru&3mnqMT&%20HTTP/1.1'
            .format(city=city)
            )
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


def main():
    get_weather()


if __name__ == '__main__':
    main()
