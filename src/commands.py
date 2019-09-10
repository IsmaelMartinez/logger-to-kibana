"""
This file contains the commands available for the program
"""
import click
import src.file_processor as processor
import src.kibana as kib


@click.group()
def commands():
    """
    Process the file provided according to conditions
    """


@commands.command("process", short_help="Process the file returning a JSON")
@click.option("--file", "-f",
              required=True, metavar="str", help="The file to read")
def process(file):
    """
    Process the file and print the processed results
    """
    process_file(file)


def process_file(file: dict):
    print(processor.read_file(file))


@commands.command(
    "process_and_generate",
    short_help="Process the file and generate visualisation"
)
@click.option("--file", "-f",
              required=True, metavar="str", help="The file to read")
def process_and_generate(file: dict):
    """
    Process the file and generates the visualisation in kibana
    """
    process_and_generate_visualisations(file)


def process_and_generate_visualisations(file: dict):
    processed = processor.read_file(file)

    visualisations_to_generate = remove_functions_without_logs(processed)

    for (key, value) in visualisations_to_generate.items():
        kib.generate_visualisation(key, value)


def remove_functions_without_logs(processed_file_content: dict) -> dict:
    """
    Removes the functions without logs from the processes_file_content
    """
    return {
        key: value
        for (key, value) in processed_file_content.items()
        if processed_file_content[key]["logs"]
    }
