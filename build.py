import os
from os.path import join, exists
from xml.etree import ElementTree as ET
import json

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension, fenced_code

boilerplate_beginning = """<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>LSC CS</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="../../base.css">
<link rel="stylesheet" media="screen" type="text/css" href="../monokai.css">
<link rel="stylesheet" media="print" type="text/css" href="../friendly.css">
<link rel='stylesheet' type='text/css' href='../article.css'>
</head>
<body>
<header>
<a class="underline" href="../../index.html">←</a>
</header>
"""

boilerplate_ending = """
</body>
</html>
"""

class UnderlineProcessor(Treeprocessor):
	def run(self, root):
		for anchor in root.iter("a"):
			anchor.attrib["class"] = anchor.attrib.get("class", "") + " underline"

class BoilerplateProcessor(Postprocessor):
	def __init__(self, root, file):
		self.root = root
		self.file = file

	def run(self, text):
		text = "<article>" + text + "</article>"
		series_js = join(self.root, "series.js")
		if exists(series_js):
			text = self.generate_table_of_contents(series_js) + text
		return boilerplate_beginning + text + boilerplate_ending

	def generate_table_of_contents(self, series_js):
		series = None
		with open(series_js, "r") as f:
			series = json.loads(f.read())
		html = "<ul id='tableOfContents'>"
		for v, k in series.items():
			if k == self.file:
				html += "<li><a class='selected'>" + v + "</a></li>"
			else:
				html += f"<li><a href='{k}' class='underline'>" + v + "</a></li>"				
		html += "</ul>"
		return html

class MyExtensions(Extension):
	def __init__(self, root, file):
		self.root = root
		self.file = file

	def extendMarkdown(self, md):
		md.postprocessors.register(BoilerplateProcessor(self.root, self.file), "bp", 1)
		md.treeprocessors.register(UnderlineProcessor(), "underline", 1)

for root, _, files in os.walk("articles/"):
	for file in files:
		if file.endswith(".md"):
			file_path = join(root, file)
			with open(file_path, "r", encoding="utf-8") as md_file:
				html_file_name = file.replace(".md", ".html")
				with open(join(root, html_file_name), "w+", encoding="utf-8") as html_file:
					extension_configs = {
						"codehilite": {
							"guess_lang": False,
						},
					}
					html_file.write(markdown.markdown(md_file.read(), extensions=[MyExtensions(root, html_file_name), "codehilite", "tables"], extension_configs=extension_configs, output_format="html5"))
