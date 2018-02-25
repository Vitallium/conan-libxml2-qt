import platform
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="vitallium", channel="testing")
    # NOTE: icu/59.1@bincrafters/stable doesn't have debug libraries
    if platform.system() == "Windows":
        builder.add(settings={"arch": "x86", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MT"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MT"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MD"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MD"},
                    options={}, env_vars={}, build_requires={})
    else:
        builder.add_common_builds(shared_option_name="libxml2:shared", pure_c=True)
    builder.run()