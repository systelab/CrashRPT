from conan import ConanFile
from conan.tools.files import collect_libs, copy
import os

class DBGHelpConan(ConanFile):
	name = "dbghelp"
	version = "6.3.9600.17237"
	settings = "os"
	homepage = "https://www.dll-files.com/dbghelp.dll.html"

	def package(self):
		copy(self, "*", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "include"))
		copy(self, "*", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.source_folder, "bin"))
		copy(self, "*", dst=os.path.join(self.package_folder, "lib"), src=os.path.join(self.source_folder, "lib"))

	def package_info(self):
		self.cpp_info.libs = collect_libs(self)
		self.cpp_info.bindirs = ['bin']