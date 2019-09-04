import re

results = {}

function_mapping = {
    "detector": r'def',
    "filter": r'(?<=def ).*?(?=\()'
}

log_mapping = [{
    "type": "debug",
    "detector": r'LOG.debug',
    "filter": r'(?<=LOG.debug\(["\']).*?(?=["\'])'
},{
    "type": "info",
    "detector": r'LOG.info',
    "filter": r'(?<=LOG.info\(["\']).*?(?=["\'])'
},{
    "type": "warn",
    "detector": r'LOG.warn',
    "filter": r'(?<=LOG.warn\(["\']).*?(?=["\'])'
},{
    "type": "error",
    "detector": r'LOG.error',
    "filter": r'(?<=LOG.error\(["\']).*?(?=["\'])'
},{
    "type": "critical",
    "detector": r'LOG.critical',
    "filter": r'(?<=LOG.critical\(["\']).*?(?=["\'])'
}]

def readFile(filename: str) -> dict:
    with open(filename) as file:
        function_name = None
        for line in file:
            if re.findall(function_mapping['detector'], line):
                function_name = re.findall(function_mapping['filter'],line)[0]
                results[function_name] = {'function_name': function_name, 'logs': []}
            else:
                process_with_log_mapping(function_name, line)
    return results

def process_with_log_mapping(function_name: str, line: str):
    for mapping in log_mapping:
        if re.findall(mapping['detector'], line):
            message = re.findall(mapping['filter'], line)
            if message:
                results[function_name]['logs'].append({ 'type': mapping['type'], 'message': message[0] })
                return
