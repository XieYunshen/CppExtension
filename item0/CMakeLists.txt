cmake_minimum_required(VERSION 3.12)
project(PyBindExample LANGUAGES CXX)

set(CMAKE_PREFIX_PATH "/usr/local/python/3.10.13/lib/python3.10/site-packages/pybind11/")

# 查找 Pybind11 库
find_package(pybind11 REQUIRED)

# 设置源文件列表
set(SRC_LIST
    src/functions.cpp
    src/classes.cpp
)

# 添加共享库构建
pybind11_add_module(MyPythonModule ${SRC_LIST})

# 设置安装路径
install(TARGETS MyPythonModule
    LIBRARY DESTINATION lib
)