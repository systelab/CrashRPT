from conans import ConanFile, tools

class CrashSenderConan(ConanFile):
	name = "CrashSender"
	description = "Application to send crash reports"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "crash", "report", "dump")
	license = "BSD 3-Clause"
	generators = "visual_studio"
	settings = "os", "compiler", "build_type", "arch"

	def package(self):
		self.copy("crashrpt_lang.ini", dst="bin", src=("bin/Win32/%s/" % self.settings.build_type + "CrashSender"))
		self.copy("*.exe", dst="bin", src=("bin/Win32/%s/" % self.settings.build_type + "CrashSender"))
		self.copy("*.dll", dst="bin", src=("bin/Win32/%s/" % self.settings.build_type + "CrashRpt"))
		self.copy("*.pdb", dst="pdb", src=("bin/Win32/%s/" % self.settings.build_type + "CrashSender"))

	def package_info(self):
		self.cpp_info.bindirs = ['bin']
