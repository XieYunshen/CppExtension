// src/classes.cpp
#include <pybind11/pybind11.h>

class Calculator {
public:
    Calculator(int value) : m_value(value) {}

    int getValue() const { return m_value; }

    void setValue(int value) { m_value = value; }

private:
    int m_value;
};

// 绑定类和成员函数到 Python
PYBIND11_MODULE(MyPythonClasses, m) {
    pybind11::class_<Calculator>(m, "Calculator")
        .def(pybind11::init<int>())
        .def("getValue", &Calculator::getValue)
        .def("setValue", &Calculator::setValue);
}
