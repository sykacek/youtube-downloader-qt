#!/bin/bash

cd src
export PYTHONSTARTUP=$PWD/debug.py
pyuic5 -o ui_MainWindow.py -i 0 gui.ui
python
