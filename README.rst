sublime_snippet_generator
==========

``sublime_snippet_generator`` is a script to generate sublime snippet files.


Requires
------------
Python 3.x


How to
------------

1. Copy the files you want to convert into the ``convert_me`` folder (the files can be inside folders)
2. Run ``python main.py``
3. The output files can be found inside ``snippets``

The tabTrigger is taken from the files name (not including it's extention). The case can be inherited or set to lowercase.

``lowercase = True  # Set True or False``

The content is taken from the content of the file.
the scope is set to ``text.html`` by default, the variable can be set inside the main.py file.

``scope = 'text.html'  # Default is text.html``



Example
------------

Input
--------
File Name: p.html

File Contents:
<p>Hello World!</p>


Output
--------
p.sublime.snippet file


<snippet>
	<content><![CDATA[<p>Hello World!</p>]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>p</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>text.html</scope>
</snippet>
