#!/bin/bash

pattern='s?PATH?'`pwd`'?g'

sed -i $pattern start.sh
sed -i $pattern ytb-downloader.desktop
sudo desktop-file-install ytb-downloader.desktop
