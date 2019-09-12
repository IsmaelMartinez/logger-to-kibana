"""
The file_processor is in charge of processing the files
looking for the log_mappings
to generate an object with the function, log_message and level
"""

import re
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

function_detector = config.get('file_parsers', 'FunctionMappingDetector')
function_filter = config.get('file_parsers', 'FunctionMappingFilter')
log_debug_detector = config.get('file_parsers', 'LogDebugDetector')
log_debug_filter = config.get('file_parsers', 'LogDebugFilter')
log_info_detector = config.get('file_parsers', 'LogInfoDetector')
log_info_filter = config.get('file_parsers', 'LogInfoFilter')
log_warn_detector = config.get('file_parsers', 'LogWarnDetector')
log_warn_filter = config.get('file_parsers', 'LogWarnFilter')
log_error_detector = config.get('file_parsers', 'LogErrorDetector')
log_error_filter = config.get('file_parsers', 'LogErrorFilter')
log_critical_detector = config.get('file_parsers', 'LogCriticalDetector')
log_critical_filter = config.get('file_parsers', 'LogCriticalFilter')

RESULTS = {}

FUNCTION_MAPPING = {"detector": function_detector, "filter": function_filter}

LOG_MAPPING = [
    {
        "type": "debug",
        "detector": log_debug_detector,
        "filter": log_debug_filter,
    },
    {
        "type": "info",
        "detector": log_info_detector,
        "filter": log_info_filter,
    },
    {
        "type": "warn",
        "detector": log_warn_detector,
        "filter": log_warn_filter,
    },
    {
        "type": "error",
        "detector": log_error_detector,
        "filter": log_error_filter,
    },
    {
        "type": "critical",
        "detector": log_critical_detector,
        "filter": log_critical_filter,
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
                RESULTS[function_name]["logs"].append({
                    "type": mapping["type"],
                    "filter": 'message: "' + message[0] + '"'
                })
                return
