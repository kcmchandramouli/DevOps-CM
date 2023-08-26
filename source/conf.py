# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Docker documentation'
copyright = '2023, Chandra Mouli'
author = 'Chandra Mouli'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'sphinx.ext.todo',
    # "breathe",
    # "exhale",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_tippy",
    "sphinx_togglebutton",
    # "sphinxcontrib.mermaid",
    "sphinx.ext.todo",
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme_options = {
#     'collapse_navigation': False,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False,
#     'style_external_links': True,
#     'analytics_id': 'UA-XXXXXXX',
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_nav_header_background': '#2980B9',
#     'vcs_pageview_mode': '',
#    # 'style_nav_links': 'dark',
# }

html_static_path = ['_static']
# html_css_files = ['custom.css']


# -- Special Configuration (https://www.sphinx-doc.org/en/master/usage/configuration.html)
primary_domain = 'cpp'
highlight_language = 'cpp'

# nitpicky = True
# numfig = True
html_theme = 'default'
# html_theme = 'sphinx-book-theme'

# xml_pretty = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}



myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "strikethrough",
    "deflist",
]




# String that marks the beginning of a prompt line
copybutton_prompt_text = ">>>"

# If the copybutton_prompt_text string is a regex expression
copybutton_prompt_is_regexp = False

# Only copy lines that begin with the copybutton_prompt_text string
copybutton_only_copy_prompt_lines = False

# Remove the copybutton_prompt_text string from the beginning of the prompt lines
copybutton_remove_prompts = True

# Copy empty lines
copybutton_copy_empty_lines = True

# For allowing copy of single line commands represented in multiple lines
# copybutton_line_continuation_character = "\\"

# -- Sphinx Tippy

# -- Sphinx.ext.todo (https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
todo_include_todos = True