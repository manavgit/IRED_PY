#!/bin/sh

VidDir=$PWD/Vid
LogDir=$PWD/Logs
MovedVidDir=$PWD/MovedVid

mkdir -p $LogDir
mkdir -p $VidDir
mkdir -p $MovedVidDir

python "$PWD"/IRED_main_thread.py

