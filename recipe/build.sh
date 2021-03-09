mkdir -p "$PREFIX/include"
cp -r "$SRC_DIR/include" "$PREFIX/include/periortree"
python setup.py install --single-version-externally-managed --record record.txt