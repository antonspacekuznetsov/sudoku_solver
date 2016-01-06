#!/usr/bin/python
#Автор Кузнецов Антон
#Если у вас есть вопросы, пожелания вы можете связаться со мной по e-mail:as.ky@ya.ru или посетить мой блог 1kuznetsov.ru
#Описание программы в фале README 
#Версия 1.0
#Author Kuznetsov Anton
#If you have any questions, offers you may concat at my e-mail:as.ky@ya.ru or visit my blog 1kuznetsov.ru also I am at facebook.com/mygranysmokesapipe
#Description of programm in file README
#Version 1.0
#				SUDOKU_SOLVER
#=======================================================================================================================================
#~####~~##~~##~#####~~~####~~##~~##~##~~##
###~~~~~##~~##~##~~##~##~~##~##~##~~##~~##
#~####~~##~~##~##~~##~##~~##~####~~~##~~##
#~~~~##~##~~##~##~~##~##~~##~##~##~~##~~##
#~####~~~####~~#####~~~####~~##~~##~~####

#~####~~~####~~##~~~~~##~~##~#####~~#####
###~~~~~##~~##~##~~~~~##~~##~##~~~~~##~~##
#~####~~##~~##~##~~~~~##~~##~####~~~#####
#~~~~##~##~~##~##~~~~~~####~~##~~~~~##~~##
#~####~~~####~~######~~~##~~~#####~~##~~##
import requests as _rq
import copy,os,sys
_id="idstring"
hard=4  #цифра от 0 до 4 определяет уровень сложности или номер 
mm=[]
cntr=0
_detect_count=[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
_pos_val=[]
#=====================================================================
def _prints(mass,string):
	try:
		os.system('clear')
	except:
		os.system('cls')
	print(_id)
	print("\n")
	for i in range(9):
		for j in range(len(mass)):
			if (mass[j][2]==i):
				if(mass[j][3]==0):
					print (str(string), end='   ')
				else:
					print (str(mass[j][3]), end='   ')
		print("\n")
	del mass,i,j
def _check_end():
	for i in range(len(mm)):
		if(mm[i][3]==0):
			return False
	return True
def detect_count(_dt_cnt):
	if _dt_cnt==1:
		_detect_count[0][1]+=1
	elif _dt_cnt==2:
		_detect_count[1][1]+=1
	elif _dt_cnt==3:
		_detect_count[2][1]+=1
	elif _dt_cnt==4:
		_detect_count[3][1]+=1
	elif _dt_cnt==5:
		_detect_count[4][1]+=1
	elif _dt_cnt==6:
		_detect_count[5][1]+=1
	elif _dt_cnt==7:
		_detect_count[6][1]+=1
	elif _dt_cnt==8:
		_detect_count[7][1]+=1
	elif _dt_cnt==9:
		_detect_count[8][1]+=1
	del _dt_cnt

def detect_box(c,m):
	if (c-2<=0 and m-2<=0):
		return 0
	elif (c-2<=0 and (m-2>=1 and m-2<=3)):
		return 1
	elif (c-2<=0 and m-2>=4):
		return 2
#_______________________________________________________
	elif ((c-2>=1 and c-2<=3) and m-2<=0):
		return 3
	elif ((c-2>=1 and c-2<=3) and (m-2>=1 and m-2<=3)):
		return 4
	elif ((c-2>=1 and c-2<=3) and m-2>=4):
		return 5
#_______________________________________________________
	elif (c-2>=4 and m-2<=0):
		return 6
	elif (c-2>=4 and (m-2>=1 and m-2<=3)):
		return 7
	elif (c-2>=4 and m-2>=4):
		return 8
	del c,m

def find_coord(numb):#значение которое может содержаться от 1 до 9
	li=[]
	for i in range(len(mm)):
		if (mm[i][3]==numb):
			li.append(mm[i])
	return li
	
def _method4():
	t=0
	priznak=0
	znach=0
	#hvb=1
	mini_list=[]
	mini=[]
	for hvb in range(3):
		for i in range(9):
			t=0
			znach=0
			mini.clear()
			mini_list.clear()
			for j in range(len(_pos_val)):
				if(_pos_val[j][hvb]==i):
					mini_list.append(_pos_val[j][3][0][:])
			mini_list=sum(mini_list,[]) 
			for h in mini_list:
				if(mini_list.count(h)==1):
					t+=1
					znach=h
			if(t==1 and znach!=0):
				for m in range(len(_pos_val)):
					if(_pos_val[m][hvb]==i):
						mini.append(_pos_val[m][3][0][:])
						mini=sum(mini,[])
						if(mini.count(znach)==1):
							for z in range(len(mm)):
								if(mm[z][0]==_pos_val[m][0] and mm[z][1]==_pos_val[m][1] and mm[z][2]==_pos_val[m][2]):
									mm[z][3]=znach
									priznak+=1
								
						mini.clear()
	if(priznak>0):
		del priznak,mini_list,mini,znach,hvb,t
		return 1
	del mini_list,mini,znach,hvb,t,priznak

def _method3():
	global _pos_val
	tmp=[]
	_list=[]
	peremen=0
	_pos_val.clear()
	for i in range(len(mm)):
		if (mm[i][3]==0):
			for j in range(len(mm)):
				if(mm[i][0]==mm[j][0] and mm[j][3]!=0):
					_list.append(mm[j][3])
				elif(mm[i][1]==mm[j][1] and mm[j][3]!=0):
					_list.append(mm[j][3])
				elif(mm[i][2]==mm[j][2] and mm[j][3]!=0):
					_list.append(mm[j][3])
		priznak=False
		for n in range(1,10):
			priznak=False
			for j in range(len(_list)):
				if (n==_list[j]):
					priznak=True
					break
			if(priznak):
				tmp.append(n)
		if(len(tmp)==8):
			if (mm[i][3]==0):
				for j in range(1,10):
					priznak=True
					for n in tmp:
						if(j==n):
							priznak=False
							break
					if(priznak):
						mm[i][3]=j
						peremen+=1
		else:
			if(mm[i][3]==0):
				_pos_val.append([mm[i][0],mm[i][1],mm[i][2],[tmp[0:]]])			
		tmp.clear()
		_list.clear()

	tmp.clear()
	_list.clear()
	for i in range(len(_pos_val)):
		for j in range(1,10):
			if(not j in _pos_val[i][3][0]):
				tmp.append(j)
		_list.append([_pos_val[i][0],_pos_val[i][1],_pos_val[i][2],[tmp[0:]]])
		tmp.clear()
	_pos_val.clear()
	_pos_val=_list[:]
	#print(_pos_val)
	del tmp,_list,priznak
	if(peremen>=1):
		del peremen
		return 1

def _method2(znach,mm2):
	li=find_coord(znach)
	priznak=False
	priznak2=False
	li2=[]
	li3=[]
	li4=[]
	for j in range(len(mm2)):
		for t in range(len(li)):
			if(mm2[j][0]!=li[t][0]):
				priznak=True
			else:
				priznak=False
				break
		if(priznak and mm2[j][3]==0):
			li2.append(mm2[j])
	counter=0
	for j in range(9):
		for i in range(len(li2)):
			if(j==li2[i][0]):
				counter+=1
		if(counter==2):
			li3.append(j)
			counter=0
		else:
			counter=0
	for i in li3:
		for j in range(len(li2)):
			if(i==li2[j][0] and li2[j][3]==0):
				li4.append(li2[j])
	for i in range(len(li4)):
		if(i==(len(li4)-1)):
			break
		else:
			priznak=False
			priznak2=False
			if (li4[i][0]==li4[i+1][0]):
				for vandh in range(1,3):
					if(li4[i][vandh]==li4[i+1][vandh]):#vertical
						for j in range(len(mm2)):
							if(mm2[j][vandh]!=li4[i][vandh]):
								continue
							for t in range(len(li)):
								if(mm2[j][0]!=li[t][0]):
									priznak=True
								else:
									priznak=False
									break
							for t in range(len(li4)):
								if(mm2[j][0]!=li4[t][0]):
									priznak2=True
								else:
									priznak2=False
									break
							if(priznak and priznak2):
								mm2[j][3]=69
	del znach,li,priznak,priznak2,li2,li3,li4,counter			
	return mm2		

def _method1(znach):
	li=find_coord(znach)
	mm2=copy.deepcopy(mm)
	for cntr in range(9):
		priznak=False
		for t in range(len(li)):
			if(cntr!= li[t][0]):
				priznak=True
			else:
				priznak=False
				break	
		if(priznak):
			for i in range(len(mm)):
				if cntr==mm[i][0]:
					for j in range(len(li)):
						if (li[j][1]==mm[i][1] and mm[i][3]==0):
							mm2[i][3]=69
						elif (li[j][2]==mm[i][2] and mm[i][3]==0):
							mm2[i][3]=69
	mm2=_method2(znach,mm2)
	for i in range(len(mm2)):
		priznak=False
		for j in range(len(li)):
			if(mm2[i][0]!=li[j][0]):
				priznak=True
			else:
				priznak=False
				break
		if(priznak):
			if(mm2[i][3]==0):
				mm2[i][3]=znach*-1
			elif(mm2[i][3]==69):
				mm2[i][3]=0
			priznak=False
		else:
			continue
	for i in range(9):
		t=0
		for j in range(len(mm2)):
			if(i==mm2[j][0]):
				if(mm2[j][3]==znach*-1):
					t+=1
		if(t==1):
			for j in range(len(mm2)):
				if(i==mm2[j][0]):
					if(mm2[j][3]==znach*-1):
						mm[j][3]=znach
						cntr=0
			
	del mm2,znach,priznak,li,t,i,j,cntr
	return 1
		
def _init():
	global _id
	counter=0
	minicounter=0
	try:		
		link=_rq.get('http://sudoku.org.ua/t/map.php?action='+str(hard))
	except:
		print("Check Internet connection or web site is out!")
		sys.exit()
	_id=link.text
	for i in link.text:
		if (i=='I'):
			break
		if(str(i).isdigit()):
				detect_count(int(i))
				mm.append([detect_box(counter,minicounter),counter,minicounter,int(i)])
				minicounter+=1
		if(minicounter==9):
			minicounter=0
			counter+=1
	del link,minicounter,counter


_init()
while(not _check_end()):
	_prints(mm, " ")
	for i in range(1,10):
		if(cntr>150):
			if(_method3()==1):
				cntr=0
				
			elif(_method4()==1):
				cntr=0
			else:
				print("Can't solve!")
				del mm,_detect_count,cntr,_pos_val
				sys.exit()
		else:
			cntr+=_method1(i)
_prints(mm, " ")
