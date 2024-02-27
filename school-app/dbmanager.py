import mysql.connector
# from datatime import datatime
from connection import connection
from Student import student
from Teacher import Teacher
from Class import Class

class DBMamger:
    def __init__(self):
        self.connection=connection
        self.cursor=self.connection.cursor()

    def getStudentById(self,id):
        sql="select * from student where classid=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obji=self.cursor.fetchone()
            return student.CreateStudent(obji)
        except mysql.connector.Error as err:
            print('Error:', err)

    def deleteStudent(self,studentid):
        sql="delete from student where id=%s"
        values = (studentid,)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} Tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)



    def getClasses(self):
        sql="select * from class"
        self.cursor.execute(sql)
        try:
            obji=self.cursor.fetchall()
            return Class.CreateClass(obji)
        except mysql.connector.Error as err:
            print('Error:', err)


    def getStudentsByClassId(self,classid):
        sql="select * from student where classid=%s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obji=self.cursor.fetchall()
            return student.CreateStudent(obji)
        except mysql.connector.Error as err:
            print('Error:', err)
        
    def addoreditStudent(self,Student: student):
        pass
 

    def addStudet(self,student: student):
        sql="INSERT INTO student(studentNumber,Name,Surname,Birtdate,Gender,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (student.studentNumber, student.name, student.surname, student.birtdate, student.gender, student.classid)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} Tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)


    def editStudet(self,student: student):
        sql="update student set studentNumber=%s,name=%s,surname=%s,birtdate=%s,gender=%s,classid=%s where id=%s"
        values = (student.studentNumber, student.name, student.surname, student.birtdate, student.gender, student.classid,student.id)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} Tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def addTeacher(self,Teacher: Teacher):
        pass

    def editTeacher(self,Teacher: Teacher):
        pass
    
    def __del__(self):
        self.connection.close()

# db = DBMamger()

# student=db.getStudentById(7)


# student[0].name = "Çınar"


# db.addStudet(student[0])
# db.editStudet(student[0])

# students=db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[4].name)