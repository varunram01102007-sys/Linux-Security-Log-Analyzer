# Linux Security Log Analyzer

Linux Security Log Analyzer is a simple Python project that reads Linux security logs and checks for failed and successful SSH login attempts.

I created this project to understand how security logs can be analyzed using Python and how repeated failed login attempts can be detected.

## Features

* Detects failed SSH login attempts
* Detects successful SSH login attempts
* Counts failed login attempts
* Counts successful login attempts
* Shows a warning for multiple failed login attempts
* Uses a sample log file for testing

## Technologies Used

* Python 3
* Linux Security Logs
* Git
* GitHub

## Project Files

```text
Linux-Security-Log-Analyzer/
│
├── log_analyzer.py
├── sample_log.txt
└── README.md
```

## How It Works

The program reads the `sample_log.txt` file and checks each line for login activity.

It looks for:

```text
Failed password
Accepted password
```

If it finds a failed login, it increases the failed login count.

If it finds a successful login, it increases the successful login count.

The program also gives a warning when there are multiple failed login attempts.

## How to Run

### Clone the repository

```bash
git clone https://github.com/varunram01102007-sys/Linux-Security-Log-Analyzer.git
```

### Open the project folder

```bash
cd Linux-Security-Log-Analyzer
```

### Run the program

```bash
python log_analyzer.py
```

## Example

Sample log:

```text
Failed password for student from 192.168.1.20
Failed password for student from 192.168.1.20
Accepted password for student from 192.168.1.10
```

Example output:

```text
Linux Security Log Analyzer

Failed login attempts: 2
Successful login attempts: 1
```

If there are several failed attempts, the program displays a warning.

## Why I Made This

I made this project to practice Python and learn some basic cybersecurity concepts.

It helped me understand how login logs can be checked for suspicious activity and how simple automation can be used for security monitoring.

## Future Improvements

* Detect suspicious IP addresses
* Detect possible brute-force attacks
* Analyze real Linux authentication logs
* Add IP-based statistics
* Generate reports
* Export results to CSV
* Create a web interface

## Important Note

This project is made for learning and educational purposes. It only analyzes log data and does not perform any attacks or unauthorized access.

## Author

**Varun Ram**

B.Tech CSE — Cyber Security & AI & Data Science

GitHub: https://github.com/varunram01102007-sys
