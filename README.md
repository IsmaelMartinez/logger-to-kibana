# logger_to_kibana

[![Build Status](https://dev.azure.com/ismaelmartinez0550/logger_to_kibana/_apis/build/status/IsmaelMartinez.logger_to_kibana?branchName=master)](https://dev.azure.com/ismaelmartinez0550/logger_to_kibana/_build/latest?definitionId=2&branchName=master)
[![DepShield Badge](https://depshield.sonatype.org/badges/IsmaelMartinez/logger_to_kibana/depshield.svg)](https://depshield.github.io)

---

This project is inteded to generate view from the log messages encountered.

To get the programs help just type:

```bash
main.py
```

This returns:

```bash
  Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Process the file provided according to conditions

Options:
  --help  Show this message and exit.

Commands:
  process               Process the file returning a JSON
  process_and_generate  Process the file and generate visualisation
```

The current available commands are:

## process

Process a file and prints out the processed functions/logs

To execute the command run:

```bash
main.py process -f <file_location>.py
```

## process_and_generate

Process a file and generates a metric visualisation in kibana (currently in localhost:5601)

To execute the command run:

```bash
main.py process_and_generate -f <file_location>.py
```

## How does it work

Currently this program uses regex `detector` to categorise the different lines.

Then, it usses the `filter` to select what part of the line to keep.

It does this in the following order:

| type | detector | filter |
|---|---|---|
| function | `r'def'` | `r'(?<=def ).*?(?=\()'` |
| critical | `r'LOG.critical'` | `r'(?<=LOG.critical\(["\']).*?(?=["\'])'` |
| error | `r'LOG.error'` | `r'(?<=LOG.error\(["\']).*?(?=["\'])'` |
| warn | `r'LOG.warn'` | `r'(?<=LOG.warn\(["\']).*?(?=["\'])'` |
| info | `r'LOG.info'` | `r'(?<=LOG.info\(["\']).*?(?=["\'])'` |
| debug | `r'LOG.debug'` | `r'(?<=LOG.debug\(["\']).*?(?=["\'])'` |

For each function, it will generate an object like the following:

```python
{ '<function_filter>': {
    'function_name': '<function_filter>',
    'logs': [{
        'type': '<type>',
        'filter': 'message: "<filter_message>"'
    },{
        ...
    }]
}}
```

As an example, when processing the following file:

```python
def lambda_handler(_event: dict, _context):
    LOG.debug('Initialising')
    LOG.info('Processing')
    LOG.warn('Success')
    LOG.error('Failure')
    LOG.critical('Bananas')
)
```

Will return the next object:

```python
{
    'lambda_handler': {
        'function_name': 'lambda_handler',
        'logs': [
            {
                'type': 'debug',
                'filter' : 'message: "Initialising"'
            },
            {
                'type': 'info',
                'filter' : 'message: "Processing"'
            },
            {
                'type': 'warn',
                'filter' : 'message: "Success"'
            },
            {
                'type': 'error',
                'filter' : 'message: "Failure"'
            },
            {
                'type': 'critical',
                'filter' : 'message: "Bananas"'
            }
        ]
    }
}
```

After this, it removes any functions without logs, and generates a kibana metric visualisation with the rest.
