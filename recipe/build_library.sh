set -eu
COMPILER=g++
STD_VER='-std=c++11'
mkdir build
cd build
cmake -DCMAKE_CXX_COMPILER=${COMPILER} -DSTANDARD_VERSION:STRING=${STD_VER} ..
make
ctest --output-on-failure