add_test(
    NAME test_add
    COMMAND 
    ${CMAKE_COMMAND} -E env PYTHONPATH=${CMAKE_BINARY_DIR}/
    ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_add.py
)
add_test(
    NAME test_subtract
    COMMAND 
    ${CMAKE_COMMAND} -E env PYTHONPATH=${CMAKE_BINARY_DIR}/
    ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_subtract.py
)