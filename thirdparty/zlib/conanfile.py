from conan import ConanFile
from conan.tools.files import copy
import os

class TheoraConan(ConanFile):
	name = "theora"
	version = "1.1.1"
	homepage = "https://gitlab.xiph.org/xiph/theora/-/tree/v1.1.1?ref_type=tags"
	
	exports_sources = (
		"CMakeLists.txt",
		"lib/*"
	)
	
	def package(self):
		copy(self, "*", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "include"))
		copy(self, "*", dst=os.path.join(self.package_folder, "win32"), src=os.path.join(self.source_folder, "win32"))
		copy(self, "AUTHORS", dst=self.package_folder, src=self.source_folder)
		copy(self, "CHANGES", dst=self.package_folder, src=self.source_folder)
		copy(self, "COPYING", dst=self.package_folder, src=self.source_folder)
		copy(self, "LICENSE", dst=self.package_folder, src=self.source_folder)
		copy(self, "README", dst=self.package_folder, src=self.source_folder)
