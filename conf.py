# -*- coding: utf-8 -*-

import sys
import os

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Školení GRASS GIS - Úvod do systému'
copyright = u'2014 by Martin Landa a Jáchym Čepický (GISMentors)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'
# The full version, including alpha/beta/rc tags.
release = '%sRC2' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'skoleni-grass-gis-zacatecnik'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
    'preamble': "".join([]),
    'releasename': u'verze',
    'date': 'leden 2015',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '%s-%s.tex' % (htmlhelp_basename, version), project,
     u'GISMentors', u'manual'),
    ]

latex_logo = "images/opengeolabs-logo.png"

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', htmlhelp_basename, project,
     [copyright], 1)
    ]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', htmlhelp_basename, project,
     copyright, htmlhelp_basename, project,
     'Miscellaneous'),
    ]

html_favicon = "images/favicon.ico"

sys.path.append(os.path.join('..', 'sphinx-template'))
from conf_base import *

todo_include_todos = True
html_use_index = True
