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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(sys.path)

# -- Project information -----------------------------------------------------

project = 'METplus-Training'
author = 'UCAR/NCAR, NOAA, and CSU/CIRA'
version = '3.1'
release = f'{version}'
release_year = '2020'
release_date = f'{release_year}0810'
copyright = f'{release_year}, {author}'

# -- Software version covered by the tutorial --------------------------------
# Update these for each new METplus release. Every |placeholder| below is
# replaced throughout the docs, including inside code blocks and link URLs
# (see substitute_versions() at the bottom of this file).
metplus_version = '13.0.0'   # shared by all METplus components (MET, METplotpy, ...)

def _short(v):
    """'13.0.0' -> '13.0'"""
    return '.'.join(v.split('.')[:2])

version_substitutions = {
    '|metplus_version|': metplus_version,                     # 13.0.0
    '|metplus_short|':   _short(metplus_version),             # 13.0
    '|metplus_branch|':  f'main_v{_short(metplus_version)}',  # main_v13.0
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc','sphinx.ext.intersphinx','sphinx_copybutton']

# Add copy buttons to code blocks, except sample output
copybutton_selector = (':not(.admonition-sample-output)'
                       ' > div[class^="highlight-"] div.highlight pre')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'Flowchart',
    'modules/template.rst',
    'Featured_Topics/Environment/index.rst',
    'Featured_Topics/MET/index.rst',
    'Featured_Topics/METplus/index.rst',
    'Featured_Topics/METviewer/index.rst',
    'Featured_Topics/template.rst',
    'Featured_Topics/Environment/aws.rst',
    'Featured_Topics/Environment/cheyenne.rst',
    'Featured_Topics/Environment/docker.rst',
    'Featured_Topics/Environment/manage_externals.rst',
    'Featured_Topics/Environment/met_installation.rst',
    'Featured_Topics/Environment/metplus_installation.rst',
    'Featured_Topics/MET/met_tool_gen_vx_mask.rst',
    'Featured_Topics/METplus/common_config_part1.rst',
    'Featured_Topics/METplus/common_config_part2.rst',
    'Featured_Topics/METplus/metplus_configuration.rst',
    'Featured_Topics/METplus/use_case_brightness_temperature_distance_map.rst',
    'Featured_Topics/METplus/use_case_example_wrapper.rst',
    'Featured_Topics/METplus/use_case_mode_brightness_temperature.rst',
    'Featured_Topics/METplus/use_case_track_and_intensity.rst',
    'Featured_Topics/METviewer/docker.rst',
    'Featured_Topics/MET/met_tool_gen_vx_mask.rst',
    'Featured_Topics/METplus/common_config_part2.rst',
    'Featured_Topics/METplus/use_case_brightness_temperature_distance_map.rst',
    'Featured_Topics/METplus/use_case_example_wrapper.rst',
    'Featured_Topics/METplus/use_case_mode_brightness_temperature.rst',
    'Featured_Topics/METplus/use_case_track_and_intensity.rst',
    'Tutorial/tutorial_setup/tutorial_setup_1.rst',
    'Tutorial/tutorial_setup/tutorial_setup_2a.rst',
    'Tutorial/tutorial_setup/tutorial_setup_2b.rst',
    'Tutorial/tutorial_setup/tutorial_setup_3.rst'    
]

# Suppress certain warning messages
suppress_warnings = ['ref.citation']

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
html_js_files = [ ]
html_css_files = ["theme_override.css", "custom.css"]

# of the sidebar.
html_logo = os.path.join('_static','METplus_logo.png')

# For Read the Docs themes (sphinx_rtd_theme)
html_theme_options = {
    'navigation_depth': 6,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
}

# Also set the global TOC depth
html_sidebars = {
    '**': ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}

# This ensures deep nesting is preserved
html_theme_options['globaltoc_maxdepth'] = 5

# -- Intersphinx control -----------------------------------------------------
intersphinx_mapping = {'numpy':("https://docs.scipy.org/doc/numpy/", None)}

numfig = True

numfig_format = {
    'figure': 'Figure %s',
}

# -- Include the CSS -------------------------------------------------------------------
def substitute_versions(app, docname, source):
    """Replace version placeholders in the raw source before parsing.

    Unlike rst_epilog substitutions, this also works inside code blocks,
    parsed-literals, inline literals, bold text and hyperlink URLs.
    """
    text = source[0]
    for placeholder, value in version_substitutions.items():
        text = text.replace(placeholder, value)
    source[0] = text

def setup(app):
    app.add_css_file("custom.css")
    app.connect('source-read', substitute_versions)
    app.connect('include-read',
                lambda app, path, docname, content:
                    substitute_versions(app, docname, content))
    # Registering the values makes Sphinx rebuild every page when they change.
    app.add_config_value('metplus_version', metplus_version, 'env')

# -- linkcheck builder configuration ----------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 8

linkcheck_ignore = []

linkcheck_anchors = True
linkcheck_anchors_ignore = ['^!']
    
# -- Export variables --------------------------------------------------------

rst_epilog = """
.. |copyright|    replace:: {copyrightstr}
.. |release_date| replace:: {release_datestr}
.. |release_year| replace:: {release_yearstr}
""".format(copyrightstr    = copyright,
           release_datestr = release_date,
           release_yearstr = release_year)

