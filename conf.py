# -- Project information -----------------------------------------------------

project = 'Cpp-Programming-Style-Guideline'
copyright = '2021, Guoning-Chen'
author = 'Guoning-Chen'

# for Markdown
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']


# -- General configuration ---------------------------------------------------

extensions = ['myst_parser', 'sphinx_markdown_tables']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------


# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']