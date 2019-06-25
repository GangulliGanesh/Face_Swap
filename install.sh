sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libx11-dev libatlas-base-dev
sudo apt-get install libgtk-3-dev libboost-python-dev
pip install --upgrade pip
tar xvf dlib-19.17.tar.bz2
cd dlib-19.17/
mkdir build
cd build
cmake ..
cmake --build . --config Release
sudo make install
sudo ldconfig
cd ..
pkg-config --libs --cflags dlib-1
cd dlib-19.17/
python setup.py install
rm -rf dist
rm -rf tools/python/build
rm python_examples/dlib.so
cd ..
sudo chmod +x destroy.sh
pip install -r requirement.txt
pip install stasm



