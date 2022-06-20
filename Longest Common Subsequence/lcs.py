# Using bottom up approach to generate 2d table for both strings
# The time complexity of the function is O(m*n); m is length of first string & n length of 2nd
def lcs(s1,s2):
	check = [[None]*(len(s2) + 1) for i in range(len(s1) + 1)]
	i=0
	j=0
	m = len(s1)
	while(m>-1):
		n=len(s2)
		j=0
		while(n>-1):
			n=n-1
			if i==0 or j==0:
				check[i][j] = 0
			elif s1[i-1]==s2[j-1]:
				check[i][j] = check[i-1][j-1]+1
			else:
				if check[i-1][j] > check[i][j-1]:
					check[i][j] = check[i-1][j]
				else:
					check[i][j] = check[i][j-1]
			j=j+1
		i=i+1
		m=m-1
	return string_lcs(check,s1,s2,len(s1),len(s2))

# To print the Longest Common Subsequence using the table generated in above function
def string_lcs(myarr,s1,s2,m,n):
	string = []
	while m and n:
		if s1[m-1] == s2[n-1]:
			string.append(s1[m-1])
			m=m-1
			n=n-1
		elif myarr[m-1][n] < myarr[m][n-1]:
			n=n-1
		else:
			m=m-1
	mystr = ""
	for i in reversed(string):
		mystr = mystr + i
	return mystr

def main():
	check = 'Y'
	while check=='Y':
		print("Enter both of the strings: \n")
		str1 = input("String 1: ")
		str2 = input("String 2: ")
		output = lcs(str1,str2)
		print('LCS of the provided strings:',output)
		c = input('''\n To continue finding LCS, Enter 'Y' or any other key otherwise:''')
		check = c[0].upper()
		print()
	print('Exiting...')
	return

if __name__ == "__main__":
	main()