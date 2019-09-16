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


@commands.command(
        "process_folder", short_help="Process the folder printing a JSON")
@click.option("--folder", "-f",
              required=False, metavar="str", help="Folder to read")
def process_folder(folder: str):
    print(processor.process_folder(folder))


@commands.command(
    "process_and_generate",
    short_help="Process the folder and generate visualisation"
)
@click.option("--folder", "-f",
              required=False, metavar="str", help="Folder to read")
def process_and_generate(folder: str):
    process_and_generate_visualisations(folder)


def process_and_generate_visualisations(folder: str):
    processed = processor.process_folder(folder)
    kib.generate_and_send_visualisation(folder, processed)
