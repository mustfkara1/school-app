from dbmanager import DBMamger
from Student import student
import datetime

class App:
    def __init__(self) :
        self.db=DBMamger()

    def initApp(self):
        msg="*****\n1-ÖĞRENCİ LİSTESİ\n2-ÖĞRENCİ EKLE\n3-ÖĞRENCİ GÜNCELLE\n4-ÖĞRENCİ SİL\n5-ÖĞRETMEN EKLE\n6-SINIFLARA GÖRE DERSLER\nÇIKIŞ(E/Ç)"
        while True:
            print(msg)
            islem = input("SEÇİM: ")
            if islem=='1':
                self.displayStudent()
            elif islem=='2':
                self.addStudent()
            elif islem=='3':
                self.editStudent()
            elif islem=='4':
                self.deleteStudent()
            elif islem=='5':
                pass
            elif islem=='6':
                pass
            elif islem=='E' or islem=='Ç':
                break
            else:
                print("YANLIŞ SEÇİM YAPTINIZ...")

    def deleteStudent(self):
        classid=self.displayStudent()
        studentid=int(input('ÖĞRENCİ iD: '))

        self.db.deleteStudent(studentid)
      

    def editStudent(self):
        classid=self.displayStudent()
        studentid=int(input('ÖĞRENCİ iD: '))

        Student=self.db.getStudentById(studentid)

        Student[0].name = input('AD: ') or student[0].name
        Student[0].surname = input('SOYAD: ') or student[0].name
        Student[0].gender = input('CİNSİYET(E/K): ') or student[0].name
        Student[0].classid = input('SINIF: ') or student[0].name

        year = input("ÖĞRENCİNİN DOĞUM TARİHİ YILI: ") or student[0].birthdate.year
        month = input("ÖĞRENCİNİN DOĞUM TARİHİ AYI: ") or student[0].birthdate.month
        day = input("ÖĞRENCİNİN DOĞUM TARİHİ GÜNÜ : ") or student[0].birthdate.day

        Student[0].birthdate=datetime.date(year,month,day)
        self.db.editStudet(student[0])

    def addStudent(self):
        self.displayclasses()

        classid = int(input('HANGİ SINIFIN KAYDINA BAKMAK İSTERSİNİZ: '))
        number = input('HANGİ NUMARALI ÖĞRENCİ: ')
        name = input('ÖĞRENCİNİN ADI: ')
        surname = input('ÖĞRENCİNİN SOYADI: ')
        year = int(input('ÖĞRENCİNİN DOĞUM YILI: '))
        month = int(input('ÖĞRENCİNİN DOĞUM AYI: '))
        day = int(input('ÖĞRENCİNİN DOĞUM GÜNÜ: '))
        birthdate = datetime.date(year,month,day)
        gender = input('ÖĞRENCİNİN CİNSİYETİ (E/K): ')

        Student =student(None,number,name,surname,birthdate,gender,classid) 
        self.db.addStudet(Student)

    def displayclasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}:{c.name}')

 

    def displayStudent(self):

        self.displayclasses()


        classid = int(input('HANGİ SINIFIN KAYDINA BAKMAK İSTERSİNİZ: '))

        Student = self.db.getStudentsByClassId(classid)
        print("ÖĞRENCİ LİSTESİ")
        for std in Student:
            print(f'{std.id}-{std.name}:{std.surname}')

        return classid


app = App()
app.initApp()

