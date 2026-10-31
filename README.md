# 🌐 Website Uptime & Incident Tracker

<p align="center">
  <strong>A Python-powered website monitoring tool to track uptime, measure response times, and record website incidents.</strong>
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
  ![Requests](https://img.shields.io/badge/Library-Requests-green)
  ![Status](https://img.shields.io/badge/Project-Completed-success)
  ![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)
</p>

---

## 📌 Overview

**Website Uptime & Incident Tracker** is a Python-based monitoring application designed to check the availability of multiple websites, measure their HTTP response times, identify connection failures, and maintain a timestamped monitoring history.

The application provides a simple way to observe website availability and record potential downtime incidents through automated HTTP requests and CSV-based reporting.

## 🎯 Project Objectives

- Monitor multiple websites from a single application.
- Identify whether websites are online or unavailable.
- Measure website response time in milliseconds.
- Capture HTTP status codes and connection errors.
- Maintain historical monitoring records.
- Generate structured CSV reports for further analysis.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🌐 Multi-Website Monitoring | Check multiple website URLs in one execution. |
| 🟢 Availability Detection | Identify online and offline websites. |
| ⚡ Response-Time Measurement | Measure HTTP request duration in milliseconds. |
| 📊 HTTP Status Tracking | Record HTTP response status codes. |
| 🛡️ Error Handling | Handle timeouts and connection-related exceptions. |
| 🕒 Timestamped Records | Store the date and time of every monitoring check. |
| 📁 CSV Reporting | Save monitoring results in a structured CSV file. |
| 📈 Monitoring Summary | Display total websites, online websites, and offline websites. |

## ⚙️ How It Works

The application follows a simple monitoring workflow:

1. **Load Websites** – Read the website URLs configured in the application.
2. **Send HTTP Requests** – Send requests to each website using the Requests library.
3. **Measure Performance** – Calculate the time taken to receive a response.
4. **Check Availability** – Classify successful HTTP responses as UP and unsuccessful responses or request failures as DOWN.
5. **Handle Errors** – Capture request exceptions without stopping the entire monitoring process.
6. **Save Results** – Store monitoring information in a CSV report.
7. **Display Summary** – Show the overall monitoring results.

## 🧰 Technologies & Tools

- **Python 3** – Core programming language.
- **Requests** – Sending HTTP requests and handling responses.
- **CSV** – Storing monitoring history.
- **datetime** – Generating timestamps.
- **time** – Measuring request duration.
- **pathlib** – Managing report file paths.

## 📂 Project Structure

```text
website-uptime-tracker/
│
├── main.py              # Application entry point
├── monitor.py           # Website monitoring logic
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignored files
└── README.md             # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ayushman-ece/website-uptime-tracker.git
```

### 2. Navigate to the Project

```bash
cd website-uptime-tracker
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python main.py
```

## 📊 Sample Output

```text
Website: https://www.google.com
Status: UP
HTTP Code: 200
Response: 145.32 ms

Website: https://www.github.com
Status: UP
HTTP Code: 200
Response: 210.45 ms

Website: https://example.invalid
Status: DOWN
HTTP Code: N/A
Response: N/A

========== SUMMARY ==========
Total websites: 3
Online: 2
Offline: 1
Report saved: uptime_report.csv
```

*Note: Response times and HTTP status codes are illustrative. Actual results depend on network conditions and website availability.*

## 📁 Generated Report

The application automatically creates:

`uptime_report.csv`

The report contains the following fields:

| Column | Description |
|---|---|
| Timestamp | Date and time of the monitoring check |
| URL | Website address |
| Status | HTTP status code |
| Response Time | Request duration in milliseconds |
| Uptime | UP or DOWN classification |
| Error | Error details, if a request fails |

New monitoring results are appended to the existing report instead of replacing previous records.

## 🧠 Python Concepts Practiced

Through this project, I worked with:

- HTTP requests and response handling.
- Exception handling using `try-except`.
- Functions and modular programming.
- Lists and dictionaries.
- CSV file creation and data writing.
- File handling using `pathlib`.
- Performance measurement using `time.perf_counter()`.
- Date and time management.
- Working with external websites and network requests.

## ⚠️ Current Limitations

- Monitoring runs only when the application is executed.
- No continuous background monitoring.
- No email, SMS, or Telegram notifications.
- No database integration.
- Response time may vary depending on network conditions.
- An HTTP availability check does not guarantee that every website feature is functioning correctly.

## 🔮 Future Improvements

Planned enhancements include:

- 🔄 Continuous website monitoring.
- 📩 Email and Telegram downtime notifications.
- 📈 Uptime percentage calculations.
- 🗄️ SQLite database integration.
- 📊 Interactive monitoring dashboard.
- 📉 Historical response-time analysis.
- 🚨 Incident detection and recovery notifications.

## 👨‍💻 Author

**Ayushman Tiwari**

🎓 B.Tech Student | Python Developer | AI & Machine Learning Enthusiast

🔗 **GitHub:** [@ayushman-ece](https://github.com/ayushman-ece)

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Your support motivates me to keep building and improving practical Python projects!

---

<p align="center">
  <strong>🚀 Part of my Daily Python Project Development Journey</strong>
  <br>
  <em>Learning by building. Improving through practice. Growing one project at a time.</em>
</p>