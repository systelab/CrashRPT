conan export-pkg conanfile_crashrpt.py --name=crashrpt --version=1.5.0 --profile:host=.conanprofile -s build_type=Debug -of int
conan export-pkg conanfile_crashrpt.py --name=crashrpt --version=1.5.0 --profile:host=.conanprofile -s build_type=Release -of int

conan export-pkg conanfile_crashsender.py --name=crashsender --version=1.5.0 --profile:host=.conanprofile -s build_type=Debug -of int
conan export-pkg conanfile_crashsender.py --name=crashsender --version=1.5.0 --profile:host=.conanprofile -s build_type=Release -of int

conan export-pkg wtl/ --name=wtl --version=8.1.9127 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg tinyxml/ --name=tinyxml --version=2.6.1 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg minizip/ --name=minizip --version=1.1 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg libtheora/ --name=theora --version=1.1.1 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg libpng/ --name=libpng --version=1.2.7 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg libogg/ --name=ogg --version=1.3.0 --profile:host=.conanprofile -s build_type=Debug
conan export-pkg jpeg/ --name=libjpeg --version=8b --profile:host=.conanprofile -s build_type=Debug
conan export-pkg dbghelp/ --name=dbghelp --version=6.3.9600.17237 --profile:host=.conanprofile -s build_type=Debug

conan export-pkg wtl/ --name=wtl --version=8.1.9127 --profile:host=.conanprofile -s build_type=Release
conan export-pkg tinyxml/ --name=tinyxml --version=2.6.1 --profile:host=.conanprofile -s build_type=Release
conan export-pkg minizip/ --name=minizip --version=1.1 --profile:host=.conanprofile -s build_type=Release
conan export-pkg libtheora/ --name=theora --version=1.1.1 --profile:host=.conanprofile -s build_type=Release
conan export-pkg libpng/ --name=libpng --version=1.2.7 --profile:host=.conanprofile -s build_type=Release
conan export-pkg libogg/ --name=ogg --version=1.3.0 --profile:host=.conanprofile -s build_type=Release
conan export-pkg jpeg/ --name=libjpeg --version=8b --profile:host=.conanprofile -s build_type=Release
conan export-pkg dbghelp/ --name=dbghelp --version=6.3.9600.17237 --profile:host=.conanprofile -s build_type=Release