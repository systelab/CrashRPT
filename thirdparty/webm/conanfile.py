from conan import ConanFile
from conan.tools.files import copy

class WebmConan(ConanFile):
	name = "libvpx"
	version = "1.3.0"
	homepage = "https://github.com/gcp/libogg/tree/master"
	
	exports_sources = (
		"CMakeLists.TXT",
		"src/*"
	)

	def package(self):
		copy(self, "*", dst="include", src="include")
		copy(self, "*", dst="win32", src="win32")
		copy(self, "CHANGELOG", dst=".", src=".")
		copy(self, "md5sums.txt", dst=".", src=".")
		copy(self, "README", dst=".", src=".")
