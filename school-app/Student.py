class student:
    def __init__(self,id,studentNumber,name,surname,birtdate,gender,classid):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birtdate=birtdate
        self.gender=gender
        self.classid=classid

    @ staticmethod
    def CreateStudent(obji):
        list=[]

        if isinstance(obji, tuple):
            list.append(student(obji[0],obji[1],obji[2],obji[3],obji[4],obji[5],obji[6]))
        else:
            for a in obji:
                list.append(student(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))

        return list
