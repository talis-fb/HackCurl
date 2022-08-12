import requests


def main(msg: str):
    a = requests.get("https://pokeapi.co/api/v2/")
    print(a.json())
    print(msg)


if __name__ == "__main__":
    main("funcionou")
