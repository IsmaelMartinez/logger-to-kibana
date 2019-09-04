"""
The file_processor is in charge of processing the files
looking for the log_mappings
to generate an object with the function, log_message and level
"""

import re

RESULTS = {}

FUNCTION_MAPPING = {"detector": r"def", "filter": r"(?<=def ).*?(?=\()"}

LOG_MAPPING = [
    {
        "type": "debug",
        "detector": r"LOG.debug",
        "filter": r'(?<=LOG.debug\(["\']).*?(?=["\'])',
    },
    {
        "type": "info",
        "detector": r"LOG.info",
        "filter": r'(?<=LOG.info\(["\']).*?(?=["\'])',
    },
    {
        "type": "warn",
        "detector": r"LOG.warn",
        "filter": r'(?<=LOG.warn\(["\']).*?(?=["\'])',
    },
    {
        "type": "error",
        "detector": r"LOG.error",
        "filter": r'(?<=LOG.error\(["\']).*?(?=["\'])',
    },
    {
        "type": "critical",
        "detector": r"LOG.critical",
        "filter": r'(?<=LOG.critical\(["\']).*?(?=["\'])',
    },
]


def read_file(filename: str) -> dict:
    """
    Reads the file line by line looking for the FUNCTION_MAPPING detector.
    if no FUNCTION_MAPPING detector is found it calls process_with_log_mapping.
    """
    with open(filename) as file:
        function_name = None
        for line in file:
            if re.findall(FUNCTION_MAPPING["detector"], line):
                function_name = re.findall(FUNCTION_MAPPING["filter"], line)[0]
                RESULTS[function_name] = {
                    "function_name": function_name,
                    "logs": []
                }
            else:
                process_with_log_mapping(function_name, line)
    return RESULTS


def process_with_log_mapping(function_name: str, line: str):
    """
    Process the line for each of the LOG_MAPPING detectors
    adding a RESULTS of the function_name if found.
    """
    for mapping in LOG_MAPPING:
        if re.findall(mapping["detector"], line):
            message = re.findall(mapping["filter"], line)
            if message:
                RESULTS[function_name]["logs"].append(
                    {"type": mapping["type"], "message": message[0]}
                )
                return
