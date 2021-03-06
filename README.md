# logger-to-kibana

[![Build Status](https://dev.azure.com/ismaelmartinez0550/logger-to-kibana/_apis/build/status/IsmaelMartinez.logger-to-kibana?branchName=master)](https://dev.azure.com/ismaelmartinez0550/logger-to-kibana/_build/latest?definitionId=5&branchName=master)

---

This project is inteded to generate view from the log messages encountered.

The python executable can be found in [https://pypi.org/project/logger-to-kibana/](https://pypi.org/project/logger-to-kibana/)

You will need to install the dependences by running

```bash
pip install -r requirements.txt
```

To get the programs help just type:

```bash
python main.py
```

This returns:

```bash
  Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Process the file provided according to conditions

Options:
  --help  Show this message and exit.

Commands:
  pommands:
  process                    Process the folder
  process_and_generate       Process the folder and generate visualization
  process_generate_and_send  Process the folder, generate visualization and
                             send
```

I have created a dev.to series explaining how this project works and any learning that I have taken from doing so. You can find it in [https://dev.to/ismaelmartinez/setting-up-my-first-opensource-python-project-4k1o](https://dev.to/ismaelmartinez/setting-up-my-first-opensource-python-project-4k1o)

## Default settings

The default settings can be found in the [settings.ini](settings.ini) file. You can provide a different settings
file by specifying it as an environment variable LOGGER_TO_KIBANA_CONFIG

## commands

The current available commands are:

### process

Process a folder and prints out the processed functions/logs in the following format:

```bash
[{'subfolder': '<folder_name>', 'filename': '<filename>', 'function': '<function_name>', 'type': '<log_type>', 'query': 'message: "<log_filter>"', 'label': '<log_type>: <log_filter>'}]
```

To execute the command run:

```bash
python main.py process -f <folder_location>
```

Check the table under [How does it work](https://github.com/IsmaelMartinez/logger-to-kibana#how-does-it-work) section to get more info about log_type and log_filter.

### process_and_generate

Process a folder (as shown in the process section) and generates a table visualization for kibana.

To execute the command run:

```bash
python main.py process_and_generate -f <folder_location>
```

### process_generate_and_send

Process a folder, generates a table visualization for kibana and send it to kibana (currently in localhost:5601)

To execute the command run:

```bash
python main.py process_and_generate -f <folder_location>
```

## How does it work

By default, it scans for files under the folder specified and with the  pattern `app/src/**/*.py`. You can specify another patter in the FilesMatchFilter in the [settings.ini](settings.ini)

This program uses different regex `detectors` to filter logs and files to process.

Those can be changed in the [settings.ini](settings.ini) file.

The current available detectors are:

| Detector                | Default Value                         | Propose                                            |
| ----------------------- | ------------------------------------- | -------------------------------------------------- |
| FilesMatchFilter        | app/src/**/*.py                       | Filter the files to process in the provided folder |
| FunctionMappingDetector | def                                   | Detect a function                                  |
| FunctionMappingFilter   | (?<=def ).*?(?=\()                    | Filter the function name                           |
| LogDebugDetector        | LOG.debug                             | Detect the log debug message                       |
| LogDebugFilter          | (?<=LOG.debug\(["\']).*?(?=["\'])     | Filter the log debug message                       |
| LogInfoDetector         | LOG.info                              | Detect the log info message                        |
| LogInfoFilter           | (?<=LOG.info\(["\']).*?(?=["\'])      | Filter the log info message                        |
| LogWarnDetector         | LOG.warn                              | Detect the log warn message                        |
| LogWarnFilter           | (?<=LOG.warn\(["\']).*?(?=["\'])      | Filter the log warn message                        |
| LogErrorDetector        | LOG.error                             | Detect the log error message                       |
| LogErrorFilter          | (?<=LOG.error\(["\']).*?(?=["\'])     | Filter the log error message                       |
| LogCriticalDetector     | LOG.critical                          | Detect the log critical message                    |
| LogCriticalFilter       | (?<=LOG.critical\(["\']).*?(?=["\'])  | Filter the log critical message                    |
| LogExceptionDetector    | LOG.exception                         | Detect the log exception message                   |
| LogExceptionFilter      | (?<=LOG.exception\(["\']).*?(?=["\']) | Filter the log exception message                   |

Other configuration available in the settings.ini file are:

| Type              | Value                                          | Propose                                                                                   |
| ----------------- | ---------------------------------------------- |------------------------------------------------------------------------------------------ |
| BaseUrl           | [http://localhost:5601](http://localhost:5601) | Kibana base url                                                                           |
| Index             | 59676040-e7fd-11e9-9209-1f165c3af176           | Kibana index                                                                              |
| VisualizationType | metric                                         | Type of visualization to generate. Valid options are metric or table                      |
| AuthType          | None                                           | Authentication Type. You can use 'aws' to use requests_aws4auth to authenticate with aws  |

## The process

The commands for the application are done in the following logical order.

```bash
process -> generate -> send
```

As an example, when processing a file in `tests/unit/resources/example.py` with the content:

```python
def lambda_handler(_event: dict, _context):
    LOG.debug('Initialising')
    LOG.info('Processing')
    LOG.warn('Success')
    LOG.error('Failure')
    LOG.critical('Bananas')
    LOG.exception('Exception')
)
```

Will return the next object:

```python
[{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler', 'type': 'debug', 'query': 'message: "Initialising"', 'label': 'debug: Initialising'},
{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler','type': 'info', 'query': 'message: "Processing"', 'label': 'info: Processing'},
{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler', 'type': 'warn', 'query': 'message: "Success"', 'label': 'warn: Success'},
{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler', 'type': 'error', 'query': 'message: "Failure"', 'label': 'error: Failure'},
{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler', 'type': 'critical', 'query': 'message: "Bananas"', 'label': 'critical: Bananas'},
{'subfolder': 'resources', 'filename': 'example.py', 'function': 'lambda_handler', 'type': 'exception', 'query': 'message: "Exception"', 'label': 'exception: Exception'}]
```

It will generate a metric visualization with filters for all the logs that have found.

Those visualisations will be split by function, then filename and then subfolder.

You can change the type of visualization generated by modifying the VisualizationType in the [settings.ini](settings.ini). The current available values are metric or table. The default value is metric.

To finish, it sends the generated visualization to Kibana with the following name format:

```bash
[Generated - <folder> <subfolder> <filename> <function> ]
```

## Limitations

It does not detect logs assign to variables or constants. They will not appear in your visualizations. [#40](https://github.com/IsmaelMartinez/logger-to-kibana/issues/40) should address this.
