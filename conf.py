# global configuration for every documentation added at the end

import os

# General information about the project.
copyright = u'2012-2017, The Nextcloud developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '13'
# The full version, including alpha/beta/rc tags.
release = '13'


# substitutions go here
rst_epilog =  '.. |version| replace:: %s' % version

html_context = {
	'doc_versions': ['11', '12', '13'],
	'current_doc': os.path.basename(os.getcwd()),
}
