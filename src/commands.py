import click
import src.file_processor as processor
import src.kibana as kibana

@click.group()
def commands():
    """
    Process the file provided according to conditions
    """

@commands.command("process", short_help="Process the file returning a JSON")
@click.option("--file", "-f", required=True, metavar="str", help="The file to read")
def process(file: str):
    print(processor.readFile(file))

@commands.command("process_and_generate", short_help="Process the file and generate visualisation")
@click.option("--file", "-f", required=True, metavar="str", help="The file to read")
def process_and_generate(file):
    processed_file_content = processor.readFile(file)

    visualisations_to_generate = filter_functions_with_logs(processed_file_content)

    for (key,value) in visualisations_to_generate.items():
        kibana.generate_visualisation(key, value)

def filter_functions_with_logs(processed_file_content: dict) -> dict:
    return {key:value for (key,value) in processed_file_content.items() if processed_file_content[key]['logs']}
