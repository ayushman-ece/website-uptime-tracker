import requests
import csv
import time
from datetime import datetime
from pathlib import Path

REPORT_FILE = Path("uptime_report.csv")


def check_website(url):
    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=10)
        response_time = round(
            (time.perf_counter() - start) * 1000, 2
        )

        return {
            "url": url,
            "status": response.status_code,
            "response_time_ms": response_time,
            "uptime": "UP" if response.ok else "DOWN",
            "error": ""
        }

    except requests.RequestException as error:
        return {
            "url": url,
            "status": "N/A",
            "response_time_ms": "N/A",
            "uptime": "DOWN",
            "error": str(error)
        }


def save_report(results):
    file_exists = REPORT_FILE.exists()

    with REPORT_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp", "url", "status",
                "response_time_ms", "uptime", "error"
            ]
        )

        if not file_exists:
            writer.writeheader()

        for result in results:
            writer.writerow({
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                **result
            })


def monitor_websites(urls):
    results = []

    for url in urls:
        result = check_website(url)
        results.append(result)

        print(f"\nWebsite: {result['url']}")
        print(f"Status: {result['uptime']}")
        print(f"HTTP Code: {result['status']}")
        print(f"Response: {result['response_time_ms']} ms")

        if result["error"]:
            print(f"Error: {result['error']}")

    save_report(results)

    up_count = sum(r["uptime"] == "UP" for r in results)
    down_count = len(results) - up_count

    print("\n========== SUMMARY ==========")
    print(f"Total websites: {len(results)}")
    print(f"Online: {up_count}")
    print(f"Offline: {down_count}")
    print(f"Report saved: {REPORT_FILE}")


def main():
    websites = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.wikipedia.org",
        "https://example.invalid"
    ]

    monitor_websites(websites)


if __name__ == "__main__":
    main()