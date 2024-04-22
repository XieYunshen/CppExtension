// src/functions.cpp
#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

double multiply(double a, double b) {
    return a * b;
}

// 绑定函数到 Python
PYBIND11_MODULE(MyPythonModule, m) {
    m.def("add", &add, "A function which adds two numbers");
    m.def("multiply", &multiply, "A function which multiplies two numbers");
}
