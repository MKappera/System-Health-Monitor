#!/usr/bin/env python3
"""
Reads 'health_report.txt' and prints alerts if usage is high.
"""


report_file = "reports/health_report.txt"


CPU_LIMIT = 80
DISK_LIMIT = 85


try:
    with open(report_file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f" File not found: {report_file}")
    exit(1)

cpu_usage = None
disk_usage = []

for line in lines:
    
    if "Cpu(s)" in line:
        parts = line.split(",")
        cpu_part = parts[0].strip()  
        cpu_usage = float(cpu_part.split()[1])
    
    
    if "/dev" in line and "%" in line:
        items = line.split()
        usage = int(items[4].replace("%", ""))
        mount = items[-1]
        disk_usage.append((mount, usage))


print("\n===== SYSTEM HEALTH SUMMARY =====")
if cpu_usage is not None:
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_LIMIT:
        print(f"  High CPU usage detected (> {CPU_LIMIT}%)!")

for mount, usage in disk_usage:
    print(f"Disk Usage on {mount}: {usage}%")
    if usage > DISK_LIMIT:
        print(f"  High Disk usage detected on {mount} (> {DISK_LIMIT}%)!")

print("=================================")

