from conan import ConanFile
from conan.tools.files import copy
import os

class TinyXMLConan(ConanFile):
	name = "tinyxml"
	version = "2.6.1"
	
	def export_sources(self):
		copy(self, pattern="*", dst=self.export_sources_folder, src=self.recipe_folder, excludes="*.py")

	def package(self):
		copy(self, "*.h", dst=os.path.join(self.package_folder, "include"), src=self.source_folder, excludes="*.py")