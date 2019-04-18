root_words=['लड़का',         
			'गधा',
			'बच्ची',
			'लड़की',
			'नदी',
			'गली',
			'माला',
			'लता',
	'शाखा',
	'गाथा',
	'माली',
	'जोहरी',
	'कूली',
	'आदमी']
		
inpt_option=['आ','आओं','आयें','इयाँ','इयों','ई','ए','ओं']

ans=[6571537,3946843,857157,3882417]

print("Enter root word index")

#we will get this from..?

i = int(input())

print("you have selected"+root_words[i-1])

rootgrp=0
if i in range(0,2):rootgrp=0
elif i in range(3,7):rootgrp=1
elif i in range(8,11):rootgrp=2
else :rootgrp=3

input_arr=["delsingdr",
	"delpludr",
	"delsingob",
	"delpluob",
	"addsingdr",
	"addpludr",
	"addsingob",
	"addpluob"]

inpt=[None]*8

for itr in range(8):
	print("enter "+input_arr[itr])
	inpt[itr]=int(input())-1

corr_ans=ans[rootgrp]
answer=0
k=1
for i in range(8):
	answer=answer+k*inpt[i]
	k=k*7

print (answer)

if answer==corr_ans :
	print("YES")
else:
	print("NO")	
