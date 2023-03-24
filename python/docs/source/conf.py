# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import sys
import os

# sys.path.append(os.path.relpath('../conformance/funtions'))
sys.path.insert(0, os.path.abspath('../../'))

project = 'CONFORMANCETEST-DIOPI'
copyright = '2023, OpenComputeLab'
author = 'OpenComputeLab'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinx_rtd_theme',
              'sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'sphinx.ext.mathjax', ]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'
# language = 'zh_CN'
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
