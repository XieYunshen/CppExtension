# ccache 清理
ccache --clear 
mkdir -p build && cd build
# 压缩 ccache 中的缓存
ccache -z
cmake .. -DWITH_COVERAGE=ON -DWITH_TESTING=ON  -DWITH_CCACHE=ON 
time make 
# 显示 ccache 的统计信息
ccache -s

rm -rf build

mkdir -p build && cd build 
ccache -z
cmake .. -DWITH_COVERAGE=ON -DWITH_TESTING=ON  -DWITH_CCACHE=ON 
time make 
ccache -s