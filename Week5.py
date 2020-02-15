##The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..
##
##Information about courses
##Line format: Course Code~Course Name~Semester~Year~Instructor
##Information about students
##Line format: Roll Number~Full Name
##Information about grades
##Line format: Course Code~Semester~Year~Roll Number~Grade
##The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8 = (10+6)÷2. If a student has not completed any courses, the grade point average is defined to be 0.
##
##You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.
##
##Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.
##
##Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:
##
##Roll Number~Full Name~Grade Point Average
##Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().
##
##Here is a sample input and its corresponding output.
##
##Sample Input
##
'''
##Courses'''
##TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
##CHAR~Charms~1~2011-2012~Filius Flitwick
##Students
##SLY2301~Hannah Abbott
##SLY2302~Euan Abercrombie
##SLY2303~Stewart Ackerley
##SLY2304~Bertram Aubrey
##SLY2305~Avery
##SLY2306~Malcolm Baddock
##SLY2307~Marcus Belby
##SLY2308~Katie Bell
##SLY2309~Sirius Orion Black
'''
##Grades'''
##TRAN~1~2011-2012~SLY2301~AB
##TRAN~1~2011-2012~SLY2302~B
##TRAN~1~2011-2012~SLY2303~B
##TRAN~1~2011-2012~SLY2305~A
##TRAN~1~2011-2012~SLY2306~BC
##TRAN~1~2011-2012~SLY2308~A
##TRAN~1~2011-2012~SLY2309~AB
##CHAR~1~2011-2012~SLY2301~A
##CHAR~1~2011-2012~SLY2302~BC
##CHAR~1~2011-2012~SLY2303~B
##CHAR~1~2011-2012~SLY2305~BC
##CHAR~1~2011-2012~SLY2306~C
##CHAR~1~2011-2012~SLY2307~B
##CHAR~1~2011-2012~SLY2308~AB
##EndOfInput
'''
##Sample Input
##'''
##SLY2301~Hannah Abbott~9.5
##SLY2302~Euan Abercrombie~7.5
##SLY2303~Stewart Ackerley~8.0
##SLY2304~Bertram Aubrey~0
##SLY2305~Avery~8.5
##SLY2306~Malcolm Baddock~6.5
##SLY2307~Marcus Belby~8.0
##SLY2308~Katie Bell~9.5
##SLY2309~Sirius Orion Black~9.0

def result():
	courses  = []
	students = {}
	grades   = {}

	while True:
		s = input()
		if s == "Courses":
			d = 1
		elif s == "Students":
			d = 2
		elif s == "Grades":
			d = 3
		elif s == "EndOfInput":
			break
		else:
			s = s.split("~")
			if d == 1:
				courses.append(s)
			elif d == 2:
				students[s[0]] = s[1]
				grades[s[0]] = []
			elif d == 3:
				grades[s[-2]].append(s[-1])
	points = {"A":10, "AB":9, "B":8, "BC":7, "C":6, "CD":5, "D":4}
	for idx in sorted(grades):
		p = [points[x] for x in grades[idx]]
		n = len(p) or 1
		marks = str(round(sum(p)/n,2)) if p else "0"
		d = [idx,students[idx],marks]
		print("~".join(d))
result()

'''''''''''&&&&&&&&&&&&&&&&&&&&&&&&&"""""""""""'''''''''''''''''''''

def rowdata():
        data=''
        Courses=[]
        Students={}
        Grades={}
        
        while(data!="EndOfInput"):
                data=input()
                if data=="Cources":
                        datacat='Cource'
                elif data=="Students":
                        datacat='Student'
                elif data=="Grades":
                        data=='Grade'
                else:
                        data=data.split("~")
                        if datacat=='Course':
                                Courses.append(data)

                        elif datacat=='Student':
                                Students[data[0]]= data[1]
                                Grades[data[0]]=[]

                        elif datacat=='Grades':
                                Grades[data[3]].append(data[4])
                                
        Gpoints = {"A":10, "AB":9, "B":8, "BC":7, "C":6, "CD":5, "D":4}
        Sgrade=sorted(Grades)                       
        for points in Sgrade:
                p = [Gpoints[x] for x in Sgrade[points]]
                n = (len(p) or 1)
                if p:
                        marks = str( round( sum(p)/n, 2 ) )
                else:
                        marks = "0"
		d=[points,Students[points],marks]
		print("~".join(d))

rawdata()              


'''
def result():
	courses  = []
	students = {}
	grades   = {}

	while True:
		s = input()
		if s == "Courses":
			d = 1
		elif s == "Students":
			d = 2
		elif s == "Grades":
			d = 3
		elif s == "EndOfInput":
			break
		else:
			s = s.split("~")
			if d == 1:
				courses.append(s)
			elif d == 2:
				students[s[0]] = s[1]
				grades[s[0]] = []
			elif d == 3:
				grades[s[-2]].append(s[-1])
	points = {"A":10, "AB":9, "B":8, "BC":7, "C":6, "CD":5, "D":4}
	for idx in sorted(grades):
		p = [points[x] for x in grades[idx]]
		n = len(p) or 1
		marks = str(round(sum(p)/n,2)) if p else "0"
		d = [idx,students[idx],marks]
		print("~".join(d))
result()
'''
def rawdata():
        
        Courses=[]
        Students={}
        Grades={}
        
        while(True):
          data=input()
          
          if data=="Courses":
            datacat='Course'
          
          elif data=="Students":
            datacat='Student'
          
          elif data=="Grades":
            data=='Grade'
          
          elif data == "EndOfInput":
            break
          
          else:
            data=data.split("~")
            
            if datacat=='Course':
              Courses.append(data)

            elif datacat=='Students':
              Students[data[0]]= data[1]
              Grades[data[0]]=[]

            elif datacat=='Grades':
              Grades[data[3]].append(data[4])

        Gpoints = {"A":10, "AB":9, "B":8, "BC":7, "C":6, "CD":5, "D":4}
        Sgrade=sorted(Grades)                       
        for points in Sgrade:
          p = [Gpoints[x] for x in Sgrade[points]]
          n = len(p) or 1
          marks = str(round(sum(p)/n,2)) if p else "0"
          d = [points,Students[points],marks]
          print("~".join(d))

rawdata()














