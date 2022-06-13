import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import PySimpleGUI as sg
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from current_class import find_current_class,send_email,timetable,deadline_reminder,email_Finder,find_empty_venue,update_login 

# 1 Create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="project2")
date = datetime.utcnow()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cursor = myconn.cursor()


#2 Load recognize and read label from model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("train.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

# create text to speech
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 175)

# Define camera and detect face
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


# 3 Define pysimplegui setting
layout =  [
    [sg.Text('Setting', size=(18,1), font=('Any',18),text_color='#1c86ee' ,justification='left')],
    [sg.Text('Confidence'), sg.Slider(range=(0,100),orientation='h', resolution=1, default_value=60, size=(15,15), key='confidence')],
    [sg.OK(), sg.Cancel()]
      ]
win = sg.Window('Attendance System',
        default_element_size=(21,1),
        text_justification='right',
        auto_size_text=False).Layout(layout)
event, values = win.Read()
if event is None or event =='Cancel':
    exit()
args = values
gui_confidence = args["confidence"]
win_started = False

# 4 Open the camera and start face recognition
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, w, y, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # predict the id and confidence for faces
        id_, conf = recognizer.predict(roi_gray)

        # If the face is recognized
        if conf >= gui_confidence:
            # print(id_)
            # print(labels[id_])
            font = cv2.QT_FONT_NORMAL
            id = 0
            id += 1
            name = labels[id_]
            current_name = name
            color = (255, 0, 0)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

            # Find the student information in the database.
            select = "SELECT student_id, name, DAY(login_date), MONTH(login_date), YEAR(login_date) FROM `student` WHERE name='%s'" % (name)
            name = cursor.execute(select)
            result = cursor.fetchall()
            # print(result)
            data = "error"

            for x in result:
                data = x
            
            
            # If the student's information is not found in the database
            
            if data == "error":
                message = "The student"+ current_name+ "is NOT FOUND in the database."
                #GUI Window open
                layout = [ [sg.Text(message,size=(50,2),key = '-text1-')],
                    [sg.Text('',size=(50,10),key = '-text2-')],
                    [sg.Button('Next'), sg.Button('Exit')] ]
            
                window = sg.Window('Attendance System', text_justification='left',).Layout(layout)

                # the student's data is not in the database
                
                event, values = window.read()
                if event == 'Exit':
                    window.Close()
                
            # If the student's information is found in the database
            else:
               
                
                # Print welcome message and login time
                message='Welcome,'+ current_name+'! '+"Your login time is:"+now.strftime("%Y-%m-%d %H:%M:%S")
                line,link1,link2=find_current_class(current_name)
                if line!="":
                    text_2_print='Attention! You have class within one hour: '
                    text_3_print=line
                else:
                    line1=timetable(current_name)
                    text_2_print='You have no class within one hour, and this is your timetable: '
                    text_3_print=line1
                layout1 = [ [sg.Text(message,size=(50,2),key = '-text1-')],
                    [sg.Text(text_2_print,size=(50,2),key = '-text2-')],
                    [sg.Multiline(text_3_print,size=(50,10),key = '-text3-')],
                    [sg.Button('Zoom'),sg.Button('Lecture Note'),sg.Button('Send Email')],
                    [sg.Button('Deadline Reminder'),sg.Button('Classmate Email'),sg.Button('empty classroom')],
                    [ sg.Button('Exit')] ]
                window1 = sg.Window('Attendance System', text_justification='left',).Layout(layout1)       
                
                  
                
                a=True
                while a: 
                    event, values = window1.read()
                    if event == 'Exit':
                        a=False
                        window1.Close()
                        win.Close()
                        cap.release() 
                    if event == 'Zoom':
                        if line!="":
                            webbrowser.open_new_tab(link1)
                    if event == 'Lecture Note':
                        if line!="":
                            webbrowser.open_new_tab(link2)
                    if event == 'Send Email':
                        if line!="":
                            a=send_email(current_name,line)
                            if a==True:
                               sg.popup("Send Success")
                            else:
                                sg.popup("Fail")
                    if event == 'Deadline Reminder':
                        line3=deadline_reminder(current_name)
                        if line3 !='':
                            print_str="Due at "+line3
                            sg.popup(print_str)
                        else:
                            sg.popup("you don't have due within 3 days")
                    if event == 'Classmate Email':
                        classmate = sg.popup_get_text('Email Finder', 'Tell us who you want to contact:')
                        result=email_Finder(classmate)
                        sg.popup('His/her Email:', result, classmate)
                    if event =='empty classroom':
                        line4,a =find_empty_venue()
                        if a==False:
                            sg.popup('no empty classroom in current time')
                        else:
                        
                            print_line="Empty Venue: "+line4
                            sg.popup(print_line)
                      
                        
        else: 
            color = (255, 0, 0)
            stroke = 2
            font = cv2.QT_FONT_NORMAL
            cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
            hello = ("Your face is not recognized")
            print(hello)
            engine.say(hello)
            # engine.runAndWait()

    # GUI
    imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
    if not win_started:
        win_started = True
        layout = [
            [sg.Text('Attendance System Interface', size=(30,1))],
            [sg.Image(data=imgbytes, key='_IMAGE_')],
            [sg.Text('Confidence'),
                sg.Slider(range=(0, 100), orientation='h', resolution=1, default_value=60, size=(15, 15), key='confidence')],
            [sg.Exit()]
        ]
        win = sg.Window('Attendance System',
                default_element_size=(14, 1),
                text_justification='right',
                auto_size_text=False).Layout(layout).Finalize()
        image_elem = win.FindElement('_IMAGE_')
    else:
        image_elem.Update(data=imgbytes)

    event, values = win.Read(timeout=20)
    if event is None or event == 'Exit':
        exit_time = datetime.now()
        login_duration = exit_time - now
        
        # Update student's the last login duration, after exit the system
        update = "UPDATE `student` SET login_duration=%s WHERE name=%s"
        val = (login_duration, current_name)
        cursor.execute(update, val)
        myconn.commit()
        break

    gui_confidence = values['confidence']

        
win.Close()
cap.release()       
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    