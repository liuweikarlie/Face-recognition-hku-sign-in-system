# HKU Face Recognition Sign in System

This project is designed based on the 2021 HKU COMP3278 Assignment. This work is worked by [@Jiayuan Feng](https://github.com/JiayuanFengSkyler) ，[@fuzezeze](https://github.com/fuzezeze), [@uniwxy](https://github.com/uniwxy), [@liuweikarlie](https://github.com/liuweikarlie), @yuanye

So based on the face recognition, instead of using password, student use the camera to log in into the system. Inside the system, it provides full information about the class information, timetable and their assignment deadline with nice interactive UI.

## Required Libraries
- numpy
- opencv-python
- opencv-contrib-python
- mysql-connector-python
- pyttsx3
- Pillow
- pysimplegui

## Install
- Install the required libraries
``````
pip install -r requirements.txt
``````
- Install the Mysql and create the tabel using the code in `430table.sql`

- Input the data into the table using the code `430data.sql`(you can change with your own data)

- Open the terminal and run the code
````
    python main.py
````
