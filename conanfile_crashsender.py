from conan import ConanFile
from conan.tools.files import copy, collect_libs
import os

class CrashSenderConan(ConanFile):
    name = "crashsender"
    description = "Application to send crash reports"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "crash", "report", "dump")
    license = "BSD 3-Clause"

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = (
        "include/*",
        "CMakeLists.txt",
        "CrashRpt.sln",
        "version.props",
        "lang_files/**",
        "processing/**",
        "reporting/**",
        "tests/**",
        "thirdparty/**",
        "demos/**"
    )

    def requirements(self):
        self.requires("dbghelp/6.3.9600.17237")
        self.requires("libjpeg/8b")
        self.requires("ogg/1.3.0")
        self.requires("libpng/1.2.7")
        self.requires("minizip/1.1")
        self.requires("theora/1.1.1")
        self.requires("tinyxml/2.6.1")
        self.requires("wtl/8.1.9127")
        self.requires("zlib/1.3.1")
        # self.requires("libvpx/1.3.0@") vpx / webm is in thirdparty folder but it's not used. Code stating it creates a webm video uses theora to create a .ogg

    def package(self):
        
        crashrpt_src = os.path.join(self.source_folder, "bin", "Win32", str(self.settings.build_type), "CrashRpt")
        crashsender_src = os.path.join(self.source_folder, "bin", "Win32", str(self.settings.build_type), "CrashSender")
        
        bin_dst = os.path.join(self.package_folder, "bin")
        pdb_dst = os.path.join(self.package_folder, "pdb")
        
        copy(self, "crashrpt_lang.ini", dst=bin_dst, src=crashsender_src)
        copy(self, "*.dll", dst=bin_dst, src=crashrpt_src)
        
        copy(self, "*.exe", dst=bin_dst, src=crashsender_src) 
        copy(self, "*.pdb", dst=pdb_dst, src=crashsender_src)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
