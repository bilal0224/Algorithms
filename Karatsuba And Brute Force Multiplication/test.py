import time
from algo import bruteforce,divANDcon
import matplotlib.pyplot as plt

def choice1():
	print("\n BruteForce Algorithm")
	print("< Enter Both Integers >")
	n1 = int(input("Integer 1: "))
	n2 = int(input("Integer 2: "))
	start = time.time()
	prod = bruteforce(n1,n2)
	end = time.time()
	print("Product Result : ", prod)
	print("Time Taken : ",abs(end-start))
	return 

def choice2():
	print("\n Divide And Conquer Algorithm")
	print("< Enter Both Integers! >")
	n1 = input("Integer 1: ")
	n2 = input("Integer 2: ")
	l = max(len(n1),len(n2))
	n1 = int(n1)
	n2 = int(n2)
	start = time.time()
	prod = divANDcon(n1,n2,l)
	end = time.time()
	print("Product Result : ", prod)
	print("Time Taken : ",abs(end-start))
	return

def choice3():
	arr = []
	print("Generating numbers ...")
	for i in range(10):
		arr.append(10**(1000*(i+1)))

	print("\nGenerated!")

	divcon_time = []
	brute_time = []
	digi = []
	for i in range(10):
		start = time.time()
		a = divANDcon(arr[i],arr[i],1000*(i+1))
		end = time.time()
		digi.append(1000*(i+1))
		b = arr[i] * arr[i]
		divcon_time.append(end-start)
		print("Div & Conq time for :".format(1000*(i+1)),end-start)
		start = time.time()
		b = bruteforce(arr[i],arr[i])
		end = time.time()
		brute_time.append(end-start)
		print("Brute Force time for :".format(1000*(i+1)),end-start)
	plt.plot(digi,divcon_time,label="Divide & Conq")
	plt.plot(digi,brute_time,label="Brute Force")
	plt.show()
	return

def main(opt):
	if opt=="1":
		choice1()
	elif opt=="2":
		choice2()
	elif opt=="3":
		choice3()
	elif opt=="4":
		return False
	else:
		print("Please make a valid choice! \n")
	return True

def stdin(opp,n1,n2,length):
	if opp=="B":
		start = time.time()
		prod = bruteforce(n1,n2)
		end = time.time()
		print("Product Result : ", prod)
		print("Time Taken : ",abs(end-start))
	elif opp=="D":
		start = time.time()
		prod = divANDcon(n1,n2,length)
		end = time.time()
		print("Product Result : ", prod)
		print("Time Taken : ",abs(end-start))

if __name__ == '__main__':
	# generating array of number of containing 1000,2000, .... , 10000 digits
	choose = """
	< standrad input format>
	B/D
	number1
	number2

	Enter B or D for standard input format or enter Menu for manual options:\n
	"""
	choose2 = """
	Continue with one of the options or enter 4 to exit!
	1. Brute Force Algorithm
	2. Divide and Conquer Algorith
	3. Graph Generating for digits upto 10000 digits
		3rd Might Take some time!!
	4. Quit
	Your Choice: """
	p = input(choose)
	p = p.upper()
	if p == 'MENU':
		should_run = True
		while should_run:
			o = input(choose2)
			should_run = main(o)
	elif p == 'B' or p == 'D':
		num1 = input("\t")
		num2 = input("\t")
		length = max(len(num1),len(num2))
		n1 = int(num1)
		n2 = int(num2)
		stdin(p,n1,n2,length)
	else:
		print("Please run again and enter in valid format!")