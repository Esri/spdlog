from conans import ConanFile


class SPDLogConan(ConanFile):
    name = "spdlog"
    version = "1.9.2"
    url = "https://github.com/Esri/spdlog/tree/runtimecore"
    license = "https://github.com/Esri/spdlog/blob/runtimecore/LICENSE"
    description = "Very fast, header-only/compiled, C++ logging library."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/spdlog/"

        # headers
        self.copy("*.h", src=base + "src", dst=relative + "src")

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
