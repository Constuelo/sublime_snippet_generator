sublime_snippet_generator
==========

``sublime_snippet_generator`` is a script to generate sublime snippet files.


Requires
------------
Supports Python 3.6.7


How to
------------

1. copy the files into the ``convert_me`` folder (the files can be inside folders)
2. run ``python main.py``
3. The output files can be found inside ``snippets``

The tabTrigger is taken from the files name (not including it's extention).
The content is taken from the content of the file.

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