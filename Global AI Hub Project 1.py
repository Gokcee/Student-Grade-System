As a Global AI Hub Machine Learning Bootcamp project, I wrote the codes for the student grading system.

import pandas as pd
import numpy as np

Lesson='Math'

def studentsave(Name,Surname,Lesson,Exam1,Exam2,Final,Letter_grade,Situation):
    save = []
    save.append(Name)
    save.append(Surname)
    save.append(Lesson)
    save.append(Exam1)
    save.append(Exam2)
    save.append(Final)
    save.append(Letter_grade)
    save.append(Situation)
    
    return save
    
    
    def data(): 
    Name= input('Enter your Name: ')
    Surname=input('Enter your Surname: ')
    Exam1=int(input('Enter your Exam1: '))
    Exam2=int(input('Enter your Exam2: ')) 
    Final= int(input('Enter your Final note: '))
    result= (Exam1*0.30)+(Exam2*0.30)+(Final*0.40)
    Letter_grade=''
    Situation =''
    
    if (100 >= result >= 90):
        Letter_grade= 'AA'
        Situation= 'Pass'
       
    elif (89 >= result >= 80):
        Letter_grade= 'BA'
        Situation= 'Pass'
        
    elif (79 >= result >= 75):
        Letter_grade= 'BB'
        Situation= 'Pass'
        
    elif (74 >= result >= 70):
        Letter_grade= 'CB'
        Situation= 'Pass' 
    
    elif (69 >= result >= 60):
        Letter_grade= 'CC'
        Situation= 'Pass'
    
    elif (59 >= result >= 50):
        Letter_grade= 'DC'
        Situation= 'Pass'
        
    elif (49 >= result >= 40):
        Letter_grade= 'DD'
        Situation= 'Pass'
     
    elif (39 >= result >= 50):
        Letter_grade= 'FD'
        Situation= 'Fail'
     
    else:
        Letter_grade= 'FF'
        Situation='Fail'
        
    return Name,Surname,Lesson,Exam1,Exam2,Final,Letter_grade,Situation
    
    datas=[]

while True:
    registration=input("Please press 'Y/y' to enter record, 'N/n' to exit or clean data c/C: ")
    if registration=="Y" or registration=="y":
        try:
            a,b,c,d,e,f,g,h=data()
            datas.append(studentsave(a,b,c,d,e,f,g,h))  
            df=pd.DataFrame(datas, columns=["Name","Surname","Lesson","Exam1","Exam2","Final","Letter_grade","Situation"])
            
        except:
            print("Enter correct type")  
            data = {}
            
    elif registration=="C" or registration=="c":
        df = df.drop(range(len(df)))
        print('Data deleting...')
            
    elif registration=="N" or registration=="n":
        break

df
df.to_excel("output.xlsx")



#EXECUTION
Please press 'Y/y' to enter record, 'N/n' to exit or clean data c/C: Y
Enter your Name: Aslı
Enter your Surname: Gül
Enter your Exam1: 78
Enter your Exam2: 88
Enter your Final note: 96
Please press 'Y/y' to enter record, 'N/n' to exit or clean data c/C: Y
Enter your Name: Akın 
Enter your Surname: Tekin
Enter your Exam1: 45
Enter your Exam2: 36
Enter your Final note: 23
Please press 'Y/y' to enter record, 'N/n' to exit or clean data c/C: N
    
# OUTPUT    
    Name	Surname	  Lesson	Exam1	Exam2	Final	Letter_grade	Situation
0	Aslı	Gül	      Math	      78	88	    96	        BA	           Pass
1	Akın	Tekin	  Math	      45	36	    23	        FF	           Fail
