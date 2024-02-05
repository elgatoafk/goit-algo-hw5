"""This module provides access to some variables used or maintained 
by the interpreter and to functions that interact strongly with the interpreter. 
"""

import sys
from pathlib import Path
import collections


def parse_log_line(line: str) -> dict:
    """parse_log_line Parse a log line into a dictionary.

    :param line: The log line to parse.
    :type line: str
    :return: A dictionary containing the parsed log information, 
    with keys for "date", "time", "level", and "details".
    :rtype: dict
    """
    line = line.split(" ", 3)
    line_dict = {}
    try:
        line_dict = {
            "date": line[0],
            "time": line[1],
            "level": line[2],
            "details": line[3].replace("\n", ""),
        }
    except IndexError:
        print("Incorrect data format")
    return line_dict


def load_logs(file_path: str) -> list:
    """load_logs Load logs from a file.

    :param file_path: The path to the log file.
    :type file_path: str
    :return: A list of log entries parsed from the file.
    :rtype: list
    """
    log_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as logs:
            while line := logs.readline():
                log_list.append(parse_log_line(line))
    except FileNotFoundError:
        print("File not found, please check filepath")
    return log_list


def filter_logs_by_level(logs: list, user_level: str) -> list:
    """filter_logs_by_level Filter logs by level.

    :param logs: A list of log entries.
    :type logs: list
    :param user_level: The log level to filter by.
    :type user_level: str
    :return: A list of log entries that match the specified log level.
    :rtype: list
    """
    filtered_logs = filter(
        lambda logs: logs["level"].lower() == user_level.lower(), logs
    )
    return list(filtered_logs)


def count_logs_by_level(logs: list) -> dict:
    """count_logs_by_level Count the logs by level.

    :param logs:  A list of log entries.
    :type logs: list
    :return: A dictionary where the keys are log levels and 
    the values are the counts of logs for each level.
    :rtype: dict
    """
    entrances = [item["level"] for item in logs]
    return collections.Counter(entrances)


def display_log_counts(counts: dict) -> None:
    """display_log_counts Display the counts of logs by level.

    :param counts: A dictionary containing the log levels as keys and their corresponding counts as values.
    :type counts: dict
    """    
    print(f"{'Log level' : <10}|{'Quantity' : <10}")
    print("-" * 20)
    for key, value in counts.items():
        print(f"{key : <10}|{value : <10}")


def main():
    """main The main entry point of the program.

    This function reads a file path from the command line arguments, 
    loads logs from the file, displays the count of logs by level, 
    and optionally filters and displays logs based on a user-provided key.

    """
    user_key = "" if len(sys.argv) < 3 else sys.argv[2]
    filepath = Path(sys.argv[1])
    logs_uploaded = load_logs(filepath)
    display_log_counts(count_logs_by_level(logs_uploaded))
    if user_key:
        filtered_info = filter_logs_by_level(logs_uploaded, user_key)
        print(f"Details for log level \'{user_key.upper()}\'")
        for oneline in filtered_info:
            print(f"{oneline["date"]:5} {oneline["time"]:5} - {oneline["details"]:5}")


if __name__ == "__main__":
    main()
