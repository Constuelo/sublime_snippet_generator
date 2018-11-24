import os
from pathlib import Path

"""
    Generates sublime snippets based from files
"""

scope = 'text.html'
name = ''
content = ''
output = None
lowercase = False  # Set True or False to set case in file names

convert_dir = '/convert_me'
snippets_dir = '/snippets'
snippet_template = 'template.sublime-snippet'
snippet_ext = '.sublime-snippet'

path = Path(os.path.dirname(__file__))
snippets_path = Path(os.path.dirname(__file__) + snippets_dir)
content_path = Path(os.path.dirname(__file__) + convert_dir)
list_path = os.listdir(content_path)

with open(snippet_template, 'r') as template:
    template_content = template.read()

    for dir, subdir, files in os.walk(content_path):
        for file in files:
            name = file.split(".")[0]

            html = os.path.join(dir, file)
            with open(html, 'r') as html:
                content = html.read()
            output = template_content

            try:
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

            if lowercase:
                name = name.lower()

            with open(Path(snippets_path / str(name + snippet_ext)), 'w') as write_file:
                write_file.write(output)


