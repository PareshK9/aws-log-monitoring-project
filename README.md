# AWS Automated Log Processing & Monitoring System

##  Project Overview

A cloud-based log processing and monitoring system built using AWS, Python, Docker, and Git.

The application retrieves log files from Amazon S3, processes log entries on an Amazon EC2 Linux server inside a Docker container, generates a summary report, and sends application logs to Amazon CloudWatch for monitoring.

##  Architecture

S3 → EC2 → Docker → Python Log Processor → CloudWatch

### Workflow

1. Log file is stored in Amazon S3.
2. EC2 accesses S3 using an IAM Role.
3. The log file is downloaded to the EC2 server.
4. Docker runs the Python log-processing application.
5. The application analyzes INFO, WARNING, and ERROR messages.
6. A summary report is generated.
7. CloudWatch Agent sends application logs to CloudWatch Logs.
8. CloudWatch monitors EC2 CPU utilization and triggers an alarm when CPU exceeds 80%.

##  Technologies Used

- AWS EC2
- Amazon S3
- AWS IAM
- Amazon CloudWatch
- Docker
- Python
- Linux
- AWS CLI
- Git & GitHub

##  Security

- IAM Role used for EC2-to-S3 access
- Least-privilege S3 permissions
- No AWS credentials stored on the EC2 server
- S3 public access blocked
- SSH access restricted to the administrator's IP address
- Private SSH key excluded from Git using `.gitignore`

##  Sample Log Analysis

The application processes logs and generates a report:

```text
===== LOG PROCESSING REPORT =====

INFO     : 4
WARNING  : 1
ERROR    : 3

===============================
```

## Project Structure
```text
aws-log-monitoring-project/
│
├── app/
│   └── log_processor.py
├── logs/
│   └── sample.log
├── output/
│   └── report.txt
├── Dockerfile
├── .gitignore
└── README.md
```
## Docker

### Build the image:

docker build -t log-monitoring-app .

### Run the application:

docker run --name log-monitoring-container \
-v "$(pwd)/logs:/app/logs" \
log-monitoring-app

## Monitoring

### CloudWatch provides:

-Application log collection
-EC2 CPU monitoring
-High CPU alarm

### Alarm:

-Alarm: EC2-High-CPU-Alarm
-Threshold: CPU Utilization > 80%
-Period: 5 minutes
-Statistic: Average

## Key Learning Outcomes

-AWS EC2 deployment
-Amazon S3 integration
-IAM Roles and least-privilege access
-Docker containerization
-AWS CLI
-CloudWatch monitoring and alarms
-Linux administration
-Troubleshooting AWS and Docker issues
-Git/GitHub version control

## Future Improvements

-Automate S3 log retrieval
-Add GitHub Actions CI/CD
-Add Terraform infrastructure provisioning
-Add SNS notifications
-Process multiple log files automatically