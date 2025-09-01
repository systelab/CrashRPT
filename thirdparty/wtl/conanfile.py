from conan import ConanFile
from conan.tools.files import copy
import os

class WTLConan(ConanFile):
	name = "wtl"
	version = "8.1.9127"
	homepage = "https://sourceforge.net/projects/wtl/files/WTL%208.1/WTL%208.1.9127/"
	# No settings/options are necessary, this is header only
	no_copy_source = True
	
	exports_sources = (
		"CPL.TXT",
		"readme.htm"
	)

	def package(self):
		copy(self, "*.h", dst=os.path.join(self.package_folder, "include"), src=self.source_folder)