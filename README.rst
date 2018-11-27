sublime_snippet_generator
==========

``sublime_snippet_generator`` is a script to generate sublime snippet files.


Requires
------------
Python 3.x


How to
------------

1. copy the files you want to convert into the ``convert_me`` folder (the files can be inside folders)
2. run ``python main.py``
3. The output files can be found inside ``snippets``

The tabTrigger is taken from the files name (not including it's extention).
The content is taken from the content of the file.
the scope is set to text.html by default, the variable can be set inside the main.py file.
``
scope = 'text.html'  # Default is text.html
lowercase = True  # Set True or False
``

Example
------------

Input
--------
p.html
``
<p>Hello World!</p>

``

Output
--------
p.sublime.snippet
``
<snippet>
	<content><![CDATA[
<p>Hello World!</p>
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>p</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>text.html</scope>
</snippet>
``
