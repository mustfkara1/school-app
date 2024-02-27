class Class:
    def __init__(self,id,name,teacherid):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.name=name
        self.teacherid=teacherid

    @staticmethod
    def CreateClass(obji):
        list=[]

        for i in obji:
            list.append(Class(i[0],i[1],i[2]))

        return list
