'''class Employee:
    def setuid(self,id):
        self.id=id
    def getuid(self):
        return self.id






class clerk(Employee):
    def setclerkdesignation(self,desig):
        self.desig=desig
    def getclerkdesignation(self):
        return self.desig

    
class faculty(Employee):
    def setcourse(self,cou):
        self.cou=cou
    def getcourse(self):
        return self.cou
 
c1=clerk()
c2=faculty()
c1=c1.setuid(1200)
print(c1.getuid())
c1.setclerkdesignation("acc")
print(c1.getclerkdesignation())
c2.setcourse("python")
print(c2.getcourse())



class Engine:
    def setengine(self,engine):
        self.engine=engine
    def getengine(self):
        return self.engine
    



class Tyre:
    def settyre(self,tyre):
        self.tyre=tyre
    def gettyre(self):
        return self.tyre
    



class Car:
    def setcar(self,car):
        self.car=car
    def getcar(self):
        return self.car



class Honda(Engine,Tyre,Car):
    def sethonda(self,honda):
        self.honda=honda
    def gethonda(self):
        return self.honda
c1=Honda()
c1.setengine("1500cc")
print(c1.getengine())
c1.settyre("MRF")
print(c1.gettyre())
c1.setcar("Mustang")
print(c1.getcar())'''









    










class Brandname:
    def setbrandname(self,brandname):
        self.brandname=brandname
    def getbrandname(self):
        return self.brandname
class Accord(Brandname):
    def setbrandname(self,brandname):
        self.brandname=brandname
    def getbrandname(self):
        return self.brandname
    
    def setmodel(self,model):
        self.model=model
    def getmodel(self):
        return self.model

    

c1=Accord()
c1.setbrandname("Mustang")
print(c1.getbrandname())
c1.setmodel("GT")
print(c1.getmodel())








