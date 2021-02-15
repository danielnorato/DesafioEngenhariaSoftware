import gspread
from classes.alune import Alune

#use your absolute path here for creds.json
gc = gspread.service_account("/home/daniel/workspace/Python/pyxls/venv/src/creds.json")

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/17EXf98TSr63ncpskotkMfVDcAzh9FyA-ikDMG3hhfOY/edit?usp=sharing')

sheet = sh.sheet1

date = sheet.get_all_records(True,3)

list = []

i=0

while i < len(date) :
    #using class alune
    id = int(date[i]['Matricula'])
    name = date[i]['Aluno']
    missed = int(date[i]['Faltas'])
    p1 = int(date[i]['P1'])
    p2 = int(date[i]['P2'])
    p3 = int(date[i]['P3'])
    list.append( Alune(id, name, missed,p1,p2,p3) )
    
    #add in datasheet colune Situação and colune Nota para Aprovação Final 
    sheet.update_cell( i+4,7,list[i].checkAproved() )
    sheet.update_cell( i+4,8,list[i].NoteforPass() )
    
    i+=1