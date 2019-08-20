import re

results = {}

def readFile(filename: str) -> dict:
    with open(filename) as file:
        function_name = None
        for line in file:
            if re.findall(r'def', line):
                function_name = re.findall(r'(?<=def ).*?(?=\()',line)[0]
                results[function_name] = {'function_name': function_name, 'logs': []}
            elif re.findall(r'LOG.info', line):
                message = re.findall(r'(?<=LOG.info\(\").*?(?=\")',line)
                results[function_name]['logs'].append({ 'type': 'info', 'message': message })
            elif re.findall(r'LOG.error', line):
                message = re.findall(r'(?<=LOG.error\(\").*?(?=\")',line)
                results[function_name]['logs'].append({ 'type': 'error', 'message': message })
    return results

def strip_log_type_message(line: str, log_type_message: str) -> str:
    message = line.strip(' ').strip(log_type_message)
    message = re.findall(r'.+?(?=\")', message)[0]
    return message
