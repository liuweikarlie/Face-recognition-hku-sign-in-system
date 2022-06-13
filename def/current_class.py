myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="project")
date = datetime.utcnow()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cursor = myconn.cursor()

def find_current_class(current_name):
    select = "select C.COURSE_NAME,l.lecturer_name,c.course_id,l.zoom_link,C.course_time,C.course_endTime,C.course_venue,lecture_notes from lecture L, course C, LectureNotes LN where L.course_id=C.course_id and LN.course_id=C.course_id and C.course_id in (select C2.course_id from course C2 where C2.course_id in ( select C1.course_id from course C1 where C1.course_id in (select T.COURSE_ID from take t where t.student_id in (select student.student_id from student where student.name=%s)) and timestampdiff(minute,C1.course_time,now())<60)) group by C.course_id;"
    val =(current_name,)
    cursor.execute(select, val)
    result = cursor.fetchall()
    line=""
    link1=""
    link2=""
    z=0
    if len(result)!=0:
        for j in result:
            for i in j:   
                print(i)
                                
                if type(i) is datetime :
                    line=line+" "+i.strftime("%Y-%m-%d %H:%M:%S")
                if z==3:
                                   
                    link1=i
                    line=line+" "+i
                    line=line+"\n"
                if z==7:
                                   
                    link2=i
                    line=line+" "+i
                    line=line+"\n"
                else: 
                    line=line+" "+str(i)
                    line=line+"\n"
                z=z+1
      
            
    return line, link1, link2
        
        
def send_email(current_name,line):
    select = "SELECT email FROM `student` WHERE name=%s"
    val = (current_name,)
    cursor.execute(select, val)
    student_email = cursor.fetchall()
    stu_email=''
    for i in student_email:
        for j in i:
            stu_email=stu_email+j
    sender = '767288034@qq.com'
    receiver = [stu_email]
    print("line type",type(line))
    message = MIMEText(line, 'plain', 'utf-8')
    message['From'] = Header("System_Generated_Message", 'utf-8')   
    message['To'] =  Header("student", 'utf-8')        
                        
    subject = "[Non-reply] Your Class information"
    message['Subject'] = Header(subject, 'utf-8')
    sucess=False                   
    try:
        smtpObj = smtplib.SMTP('smtp.qq.com')
        smtpObj.starttls()
        smtpObj.login('767288034@qq.com', 'kypeiskcfepdbddj')
            
        smtpObj.sendmail(sender, receiver, message.as_string())
        sucess=True
    except smtplib.SMTPException as e:
        print(e)
        
        sucess=False
        
    return sucess
    

def timetable (current_name):
    select = "select c.course_name, t.course_time as tutorial_time,c.course_time,course_venue from course c, tutorial t where c.course_id =t.course_id and c.course_id in (select t1.course_id from take t1 where t1.student_id in (select m.student_id from student m where m.name=%s));"
            
    val = (current_name,)
    cursor.execute(select,val)
    result = cursor.fetchall()
    line=""
    z=0
    for i in result:
        for j in i:
            if z==0:
                line=line+"Course Name "+j+"\n"
            elif z==1:
                line=line+"tutorial time"+j.strftime("%Y-%m-%d %H:%M:%S")+"\n"
            elif z==2:
                line=line+"Lecture time"+j.strftime("%Y-%m-%d %H:%M:%S")+"\n"
            elif z==3:
                line=line+"Course Venue"+j+"\n"
   
            z=z+1
    return line


def deadline_reminder(current_name):
    select = "select assignment_ddl from course c where timestampdiff(day,assignment_ddl,now())<3 and course_id in (select t.course_id from take t where t.student_id in (select s.student_id from student s where name=%s))"
    val = (current_name,)
    cursor.execute(select, val)
    result = cursor.fetchall()[0]
    line=""
    if len(result)!=0:
        for i in result:
            line=line+i.strftime('%Y-%m-%d %H:%M:%S')+"\n"
            
    
    
    return line
        
    
def email_Finder(classmate):
    select = "SELECT email FROM `student` WHERE name =%s"
    val = (classmate,)
    cursor.execute(select, val)
    result = cursor.fetchall()
    return result


def find_empty_venue():
    select = "SELECT course_venue FROM `course` where timestampdiff(minute,course_time,now())>30"
    cursor.execute(select)
    course = cursor.fetchall()[0]
    line=""
    if len(course)>0:
        for i in course:
            if i !="online":
                line=line+i+", "
    return line
    
    
def update_login(date,current_name,current_time):
    update =  "UPDATE `student` SET login_date=%s WHERE name=%s"
    val = (date, current_name)
    cursor.execute(update, val)
    update = "UPDATE `student` SET login_time=%s WHERE name=%s"
    val = (current_time, current_name)
    cursor.execute(update, val)
    myconn.commit()
     







