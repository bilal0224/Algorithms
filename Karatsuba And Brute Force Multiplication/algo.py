import math

def bruteforce(num1,num2):
	#assuming that both numbers are of same length
	multi = 0
	t2 = num2 #temporary number 2
	count = 0
	#takes digit by digit both numbers and adds them togather. just like method learned at school

	# <--------------- Complexity ---------------->
	#there are two while loops that runs for O(n) each and includes all operations corressponding
	# to O(1) making the complexity of the function O(n^2)

	while num1:
		temp = 0
		count2 = 0
		#to take all digits of num1 1 by 1
		a = num1%10 #takes last digit
		num1 = num1//10 #removes last digit
		t2 = num2 #resets t2 with value of num2
		while t2:
			#to take all digits of num2 1 by 1
			b = t2%10
			t2 = t2//10
			#digit multiplication O(1)
			mul = a*b
			#to keep result of one digit multiplying by all digts of num2
			temp = temp + mul * 10**count2
			count2=count2+1
		#to keep the sum of all multiplications
		multi = multi + temp * 10**count
		count = count+1
	return multi

def divANDcon(num1, num2,length):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1 * num2

    mylen = math.ceil(length / 2)

    # divide num1 & num2
    a0 = num1 // 10 ** mylen
    a1 = num1 % (10 ** mylen)
    b0 = num2 // 10 ** mylen
    b1 = num2 % (10 ** mylen)

    # divide and conquer multiplication algorithm.
    ab0 = divANDcon(a0, b0,mylen)
    ab1 = divANDcon(b1, a1,mylen)
    summ = divANDcon(a0 + a1, b0 + b1,mylen) -ab1 -ab0

    return ab0 * (10 ** (mylen*2)) + summ * (10 ** mylen) + ab1