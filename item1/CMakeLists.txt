cmake_minimum_required(VERSION 3.12)
project(PyBindExample LANGUAGES CXX)

# 查找 Pybind11 库
find_package(pybind11 REQUIRED)

# 设置源文件列表
set(SRC_FUNCTIONS src/functions.cpp)
set(SRC_CLASSES src/classes.cpp)

# 编译第一个模块的源文件
add_library(MyPythonFunctions MODULE ${SRC_FUNCTIONS})
target_link_libraries(MyPythonFunctions PRIVATE pybind11::module)

# 编译第二个模块的源文件
add_library(MyPythonClasses MODULE ${SRC_CLASSES})
target_link_libraries(MyPythonClasses PRIVATE pybind11::module)

# 设置共享库输出名称
set_target_properties(MyPythonFunctions PROPERTIES PREFIX "")
set_target_properties(MyPythonClasses PROPERTIES PREFIX "")


# 设置安装路径
install(TARGETS MyPythonFunctions MyPythonClasses
    LIBRARY DESTINATION lib
)
