from conans import ConanFile, tools

class CrashRptConan(ConanFile):
	name = "CrashRpt"
	description = "C++ library to generate crash reports"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "crash", "report", "dump")
	license = "BSD 3-Clause"
	generators = "visual_studio"
	settings = "os", "compiler", "build_type", "arch"

	def package(self):
		self.copy("CrashRpt.h", dst="include/crashrpt", src="include")
		self.copy("CrashRpt1403%s.lib" % ("d" if self.settings.build_type == "Debug" else ""), dst="lib", src=("lib"))
		self.copy("*.dll", dst="bin", src=("bin/Win32/%s/" % self.settings.build_type + "CrashRpt"))
		self.copy("*.pdb", dst="bin", src=("bin/Win32/%s/" % self.settings.build_type + "CrashRpt"))

	def package_info(self):
		self.cpp_info.libs = tools.collect_libs(self)
		self.cpp_info.bindirs = ['bin']