import requests


def hello_world() -> None:
    print("Hello World")


def fetch_http_status() -> None:
    response = requests.get("https://httpbin.org/get", timeout=5)
    print(f"HTTP request succeeded: {response.status_code}")


def main() -> None:
    hello_world()
    fetch_http_status()


if __name__ == "__main__":
    main()
