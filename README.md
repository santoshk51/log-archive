# Log Archive Tool

A simple CLI tool to archive logs on a set schedule by compressing them into `.tar.gz` files.  
This helps keep the system clean while preserving logs for future reference.

## Features
- Compresses logs from a given directory into a `.tar.gz` file
- Stores archives in a separate `archives/` folder
- Logs the date and time of each archive in `archive.log`

## Usage
```bash
python3 log_archive.py /var/log
