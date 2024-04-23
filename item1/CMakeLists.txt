cmake_minimum_required(VERSION 3.12)
project(example)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(WITH_COVERAGE "Compile PaddlePaddle with code coverage" OFF)
option(WITH_TESTING "compile with unit testing" OFF)

if(WITH_COVERAGE)
    include(cov.cmake)
endif()


# 设置 pybind11 路径
set(PYBIND11_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/pybind11)
add_subdirectory(${PYBIND11_DIR})

set(Python_ADDITIONAL_VERSIONS 3.10)
find_package(PythonInterp 3.10 REQUIRED)
message(STATUS "Python executable: ${PYTHON_EXECUTABLE}")


# 添加要编译的源文件
add_library(example MODULE file1.cpp)

# 链接 pybind11 库
target_link_libraries(example PRIVATE pybind11::module)

set_target_properties(example PROPERTIES PREFIX "")
if(WITH_TESTING)
    enable_testing()
    add_subdirectory(tests)
endif()