# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import inspect
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

import pdfo


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PDFO'
author = 'Tom M. Ragonneau and Zaikun Zhang'
copyright = f'2020\u2013{datetime.now().year}, {author}'

# Full version, including alpha/beta/rc tags.
release = pdfo.__version__

# Short version (including .devX, rcX, b1 suffixes if present).
version = re.sub(r'(\d+\.\d+)\.\d+(.*)', r'\1\2', release)
version = re.sub(r'(\.dev\d+).*?$', r'\1', version)

# Download statistics.
archive = urlopen('https://raw.githubusercontent.com/pdfo/stats/main/archives/total.json')
downloads = json.loads(archive.read())


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'matplotlib.sphinxext.plot_directive',
    'numpydoc',
    'sphinxcontrib.googleanalytics',
    'sphinx_copybutton',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx_favicon',
]

templates_path = ['_templates']

exclude_patterns = []

today_fmt = '%B %d, %Y'

default_role = 'autolink'

add_function_parentheses = False

# String to include at the beginning of every source file.
rst_prolog = f'''
.. |conda_downloads| replace:: {downloads['conda']:,}
.. |pypi_downloads| replace:: {downloads['pypi']:,}
.. |github_downloads| replace:: {downloads['github']:,}
.. |total_downloads| replace:: {sum(downloads.values()):,}
'''


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_css_files = ['pdfo.css']

html_theme_options = {
    'logo': {
        'text': project,
        'image_light': '_static/logo.svg',
        'image_dark': '_static/logo.svg',
    },
    'external_links': [
        {
            'name': 'MATLAB API reference',
            'url': 'https://www.mathworks.com/matlabcentral/fileexchange/75195-pdfo-powell-s-derivative-free-optimization-solvers',
        },
        {
            'name': 'Issue tracker',
            'url': 'https://github.com/pdfo/pdfo/issues',
        },
    ],
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/pdfo/pdfo',
            'icon': 'fa-brands fa-github',
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/PDFO_Software',
            'icon': 'fa-brands fa-twitter',
        },
    ],
    'footer_start': ['copyright', 'sphinx-version', 'theme-version'],
    'footer_end': [],
}

html_context = {
    'github_user': 'pdfo',
    'github_repo': 'pdfo',
    'github_version': 'main',
    'doc_path': 'doc/source',
    'default_mode': 'light',
}

html_static_path = ['_static']

html_title = f'{project} v{version} Manual'

# Output file base name for HTML help builder.
htmlhelp_basename = 'pdfo'


# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    'papersize': 'a4paper',
    'fontenc': r'\usepackage[LGR,T1]{fontenc}',
    'preamble': r'''
% Prevent "LaTeX Error: Too deeply nested."
\usepackage{enumitem}
\setlistdepth{9}

% Increase the default table of content depth.
\setcounter{tocdepth}{2}

% Extra mathematical macros.
\newcommand{\R}{\mathbb{R}}
    ''',
}

latex_documents = [
    ('python/index', 'pdfo-py.tex', 'PDFO Python Reference', author, 'howto'),
    ('user/index', 'pdfo-user.tex', 'PDFO User Guide', author, 'howto'),
]


# -- Math support for HTML outputs -------------------------------------------

mathjax3_config = {
    'tex': {
        'macros': {
            'aeq': r'A_{\scriptscriptstyle E}',
            'aub': r'A_{\scriptscriptstyle I}',
            'beq': r'b_{\scriptscriptstyle E}',
            'bub': r'b_{\scriptscriptstyle I}',
            'ceq': r'c_{\scriptscriptstyle E}',
            'cub': r'c_{\scriptscriptstyle I}',
            'obj': r'f',
            'R': r'{\mathbb{R}}',
            'xl': r'l',
            'xu': r'u',
        }
    }
}


# -- Generate autodoc summaries -----------------------------------------------

autosummary_generate = True


# -- Link to other projects’ documentation ------------------------------------

intersphinx_mapping = {
    'scipy': ('https://docs.scipy.org/doc/scipy/', None)
}


# -- Favicons -----------------------------------------------------------------

favicons = ['logo.svg']


# -- Add external links to source code ----------------------------------------

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None

    # Get the object indicated by the module name.
    obj = sys.modules.get(info['module'])
    if obj is None:
        return None
    for part in info['fullname'].split('.'):
        try:
            obj = getattr(obj, part)
        except AttributeError:
            return None

    # Strip the decorators of the object.
    try:
        unwrap = inspect.unwrap
    except AttributeError:
        pass
    else:
        obj = unwrap(obj)

    # Get the relative path to the source of the object.
    try:
        fn = Path(inspect.getsourcefile(obj)).resolve(strict=True)
    except TypeError:
        return None
    else:
        fn = fn.relative_to(Path(pdfo.__file__).resolve(strict=True).parent)

    # Ignore re-exports as their source files are not within the repository.
    module = inspect.getmodule(obj)
    if module is not None and not module.__name__.startswith('pdfo'):
        return None

    # Get the line span of the object in the source file.
    try:
        source, lineno = inspect.getsourcelines(obj)
        lines = f'#L{lineno}-L{lineno + len(source) - 1}'
    except OSError:
        lines = ''

    repository = f'https://github.com/pdfo/pdfo'
    if 'dev' in release:
        return f'{repository}/blob/main/python/pdfo/{fn}{lines}'
    else:
        return f'{repository}/blob/v{release}/python/pdfo/{fn}{lines}'


# -- Google Analytics ---------------------------------------------------------

googleanalytics_id = 'G-1DD20TL43D'
