#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add, "A function which adds two numbers");
    m.def("subtract", &subtract, "A function which subtracts two numbers");
}
