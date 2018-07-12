ch = input()
vow = ['a','e','i','o','u','A','E','I','O','U']
cons = ['b','c','d','f','g','h','p','j','k','l','m','n','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if(ch in vow):
	print("Vowel")
elif(ch in cons):
	print("Consonant")
else:
    print("Invalid")
