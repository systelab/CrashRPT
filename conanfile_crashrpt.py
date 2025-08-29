from conan import ConanFile
from conan.tools.files import copy, collect_libs
import os

class CrashRptConan(ConanFile):
    name = "crashrpt"
    description = "C++ library to generate crash reports"
    license = "BSD-3-Clause"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "crash", "report", "dump")

    settings = "os", "compiler", "build_type", "arch"
    generators = "MSBuildDeps", "MSBuildToolchain"
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

    def package(self):
        copy(self, "CrashRpt.h", dst=os.path.join(self.package_folder, "include", "crashrpt"),
                                 src=os.path.join(self.source_folder, "include"))

        suffix = "d" if self.settings.build_type == "Debug" else ""
        copy(self, f"CrashRpt1403{suffix}.lib", dst=os.path.join(self.package_folder, "lib"),
                                                src=os.path.join(self.source_folder, "lib"))
                                                
        for pattern in ("*.dll", "*.pdb"):
            copy(self, pattern, dst=os.path.join(self.package_folder, "bin"),
                                src=os.path.join(self.source_folder, "bin", "Win32", str(self.settings.build_type), "CrashRpt"))

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        self.cpp_info.bindirs = ["bin"]