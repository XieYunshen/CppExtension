mkdir build && cd build 
cmake .. -DWITH_COVERAGE=ON -DWITH_TESTING=ON 
make 
ctest 
lcov --ignore-errors gcov --capture -d ./ -o coverage.info --rc lcov_branch_coverage=0 
lcov --extract coverage.info \
    '/workspace/CppExtension/item1/file1.cpp' \
    -o coverage-full.tmp \
    --rc lcov_branch_coverage=0

mv coverage-full.tmp coverage.info
genhtml coverage.info --output-directory cpp-coverage-full 
