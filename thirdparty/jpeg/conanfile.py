from conan import ConanFile
from conan.tools.files import copy, collect_libs
import os

class LibJPEGConan(ConanFile):
    name = "libjpeg"
    version = "8b"
    homepage = "https://repository.timesys.com/buildsources/l/libjpeg/libjpeg-8b/"
    settings = "os", "compiler", "build_type", "arch"
    
    def export_sources(self):
        copy(self, pattern="*", dst=self.export_sources_folder, src=self.recipe_folder, excludes=("*.py","*.sh","*.bat"))

    def package(self):
        lib_src = os.path.join(self.source_folder, "..", "..", "lib")
        lib_dst = os.path.join(self.package_folder, "lib")
        
        include_dst = os.path.join(self.package_folder, "include", "libjpeg")
        
        copy(self, "*.h", dst=include_dst, src=self.source_folder)
        
        if self.settings.build_type == "Debug":
            copy(self, "jpegd.lib", dst=lib_dst, src=lib_src)
            copy(self, "jpegd.pdb", dst=lib_dst, src=lib_src)
        else:
            copy(self, "jpeg.lib", dst=lib_dst, src=lib_src)
            copy(self, "jpeg.pdb", dst=lib_dst, src=lib_src)
            
    def package_info(self):
        self.cpp_info.libs = collect_libs(self)