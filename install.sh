#!/bin/bash

pattern='s?PATH?'`pwd`'?g'
echo $pattern

sed -i $pattern start.sh
sed -i $pattern ytb-downloader.desktop
sudo desktop-file-install ytb-downloader.desktop
