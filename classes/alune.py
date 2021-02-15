import math

class Alune:
    def __init__(self,id,name,missed,p1,p2,p3) -> None:
        self.id = id
        self.name = name
        self.missed = missed
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.average = (self.p1 + self.p2 + self.p3) / 3

    def checkAproved(self):
        
        if self.missed > 15 :
            return "Reprovado por Falta"
        elif self.average < 50 :
            return "Reprovado por Nota"
        elif self.average < 70 :
            return "Exame Final"
        else: 
            return "Aprovado"
    
    def NoteforPass(self):
        if self.average < 70 and self.average >=50 and self.missed <= 15:
            return math.ceil(100 - self.average) 
        else:    
            return 0