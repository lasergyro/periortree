mkdir -p "$PREFIX/include"
cp -r "$SRC_DIR/include" "$PREFIX/include/periortree"
$PYTHON -m pip install . -vv