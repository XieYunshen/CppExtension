import MyPythonModule

print(MyPythonModule.add(3, 5))  # 输出：8
print(MyPythonModule.multiply(2.5, 3.5))  # 输出：8.75

calc = MyPythonModule.Calculator(10)
print(calc.getValue())  # 输出：10

calc.setValue(20)
print(calc.getValue())  # 输出：20
