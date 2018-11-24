import os
from pathlib import Path
import shutil

"""
    tabTrigger = inherits the input files name without the extension, set lowercase = True or False
    scope = default to text.html below, can be changed to any string
    content = is read from the input files contents
"""
scope = 'text.html'  # Default is text.html
lowercase = True  # Set True or False

snippet_ext = '.sublime-snippet'  # Extension name for sublimes snippet files
snippet_template = 'template.sublime-snippet'  # Base template
convert_dir = '/convert'  # Location for input files
snippets_dir = '/snippets'  # Output of files

path = Path(os.path.dirname(__file__))
snippets_path = Path(os.path.dirname(__file__) + snippets_dir)
content_path = Path(os.path.dirname(__file__) + convert_dir)
list_path = os.listdir(content_path)

""" Empty the snippets folder if it already exists """
if os.path.exists(snippets_path):
    shutil.rmtree(snippets_path)
os.makedirs(snippets_path, exist_ok=True)

with open(snippet_template, 'r') as template:
    template_content = template.read()

    for d, s, f in os.walk(content_path):
        for file in f:
            name = file.split(".")[0]

            html = os.path.join(d, file)
            with open(html, 'r') as html:
                content = html.read()
            output = template_content

            try:
                if lowercase:
                    output = output.replace('$name', name.lower())
                else:
                    output = output.replace('$name', name)
            except NameError as error:
                print(f'{error}')

            try:
                output = output.replace('$content', content)
            except NameError as error:
                print(f'{error}')

            try:
                output = output.replace('$scope', scope)
            except NameError as error:
                print(f'{error}')

            with open(Path(snippets_path / str(name + snippet_ext)), 'w') as write_file:
                write_file.write(output)

print(f'All good.')

