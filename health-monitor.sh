#!/bin/bash
# Health-Monitor Script
# Author-Moses
# Created-24/10/2025

timestamp=$(date '+%Y-%m-%d %H:%M:%S')
output_dir="reports"
mkdir -p $output_dir

report_file="$output_dir/health_report.txt"

echo "--------------------------------------" > $report_file
echo "System Health - CPU, Memory, DiskSpace, Uptime, Network details - $timestamp" >> $report_file
echo "--------------------------------------" >> $report_file


echo -e "\n CPU Usage" >> $report_file
top -bn1 | grep "Cpu(s)" >> $report_file

echo -e "\n Memory Usage" >> $report_file
free -h >> $report_file

echo -e "\n Disk Space" >> $report_file
df -h >> $report_file

echo -e "\n Uptime" >> $report_file
uptime >> $report_file

echo -e "\n Network Details" >> $report_file
ip addr >> $report_file

echo -e "\n Report saved at: $report_file"
