from conan import ConanFile
from conan.tools.files import copy, collect_libs
import os

class LibPNGConan(ConanFile):
    name = "libpng"
    version = "1.2.7"
    homepage = "https://github.com/pnggroup/libpng"
    settings = "os", "compiler", "build_type", "arch"
    
    def export_sources(self):
        copy(self, pattern="*.h", dst=self.export_sources_folder, src=self.recipe_folder)
        copy(self, pattern="*.c", dst=self.export_sources_folder, src=self.recipe_folder)
        copy(self, pattern="*.vcxproj", dst=self.export_sources_folder, src=self.recipe_folder)

    def package(self):
        lib_src = os.path.join(self.source_folder, "..", "..", "lib")
        lib_dst = os.path.join(self.package_folder, "lib")
        
        include_dst = os.path.join(self.package_folder, "include", "libpng")
        
        copy(self, "*.h", dst=include_dst, src=self.source_folder)
        
        if self.settings.build_type == "Debug":
            copy(self, "libpngd.lib", dst=lib_dst, src=lib_src)
            copy(self, "libpngd.pdb", dst=lib_dst, src=lib_src)
        else:
            copy(self, "libpng.lib", dst=lib_dst, src=lib_src)
            copy(self, "libpng.pdb", dst=lib_dst, src=lib_src)
            
    def package_info(self):
        self.cpp_info.libs = collect_libs(self)