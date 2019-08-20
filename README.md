# KibaVisualIsma

## This project is currently in early development stage. Use it at your own risk

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
