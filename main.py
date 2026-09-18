import argparse
from time import perf_counter

import requests


def main():
    parser = argparse.ArgumentParser(description="Замер скорости: 10 скачиваний подряд.")
    parser.add_argument(
        "url", nargs="?",
        default="https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
        help="Прямая ссылка на файл (по умолчанию — большая фотография).",
    )
    url = parser.parse_args().url
    total_bytes = 0
    total_time = 0
    headers = {"Accept-Encoding": "identity", "User-Agent": "InternetSpeedMeter/1.0"}

    for number in range(1, 11):
        print(f"Запрос {number}/10...", flush=True)
        size = 0
        started = perf_counter()
        try:
            with requests.get(url, headers=headers, stream=True, timeout=(10, 30)) as response:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=65536):
                    size += len(chunk)
            elapsed = perf_counter() - started
        except requests.RequestException as error:
            print(f"Ошибка запроса: {error}")
            raise SystemExit(1)

        total_bytes += size
        total_time += elapsed
        print(f"  {size / 1_000_000:.2f} МБ за {elapsed:.3f} с")

    print(f"\nСреднее время запроса: {total_time / 10:.3f} с")
    print(f"Скачано всего: {total_bytes:,} байт ({total_bytes / 1_000_000:.2f} МБ)")
    print(f"Скорость: {total_bytes / total_time / 1_000_000:.2f} МБ/с")


if __name__ == "__main__":
    main()
