CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)

set(glfw_version ${GLFW_VERSION})
rez_set_archive(
    url_glfw glfw/glfw-${glfw_version}.zip
    https://github.com/glfw/glfw/archive/${glfw_version}.zip
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    glfw
    URL ${url_glfw}
    PREFIX glfw
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    #ALWAYS 1
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/glfw.cmake
    DESTINATION .
)
