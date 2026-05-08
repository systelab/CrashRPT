from conan import ConanFile
from conan.tools.files import copy, collect_libs
from conan.tools.microsoft import MSBuildToolchain, MSBuild
from conan.errors import ConanInvalidConfiguration
import os

class CrashRptConan(ConanFile):
    name = "crashrpt"
    description = "C++ library to generate crash reports"
    license = "BSD-3-Clause"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "crash", "report", "dump")

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

    def generate(self):
        msbuild_tc = MSBuildToolchain(self)
        msbuild_tc.generate()

    def _get_platform(self):
        arch_map = {"x86": "Win32", "x86_64": "x64"}
        arch = str(self.settings.arch)
        if arch not in arch_map:
            raise ConanInvalidConfiguration(f"CrashRpt does not support '{arch}' architecture")
        return arch_map[arch]

    def build(self):
        msbuild = MSBuild(self)
        msbuild.platform = self._get_platform()
        msbuild.build(os.path.join(self.source_folder, "CrashRpt.sln"), targets=["CrashRpt"])

    def package(self):
        copy(self, "CrashRpt.h", dst=os.path.join(self.package_folder, "include", "crashrpt"),
                                 src=os.path.join(self.source_folder, "include"))

        platform = self._get_platform()
        lib_pattern = "CrashRpt*d.lib" if self.settings.build_type == "Debug" else "CrashRpt*.lib"
        copy(self, lib_pattern, dst=os.path.join(self.package_folder, "lib"),
                                src=os.path.join(self.source_folder, "lib", platform, str(self.settings.build_type)))

        for pattern in ("*.dll", "*.pdb"):
            copy(self, pattern, dst=os.path.join(self.package_folder, "bin"),
                                src=os.path.join(self.source_folder, "bin", platform, str(self.settings.build_type), "CrashRpt"))

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        self.cpp_info.bindirs = ["bin"]