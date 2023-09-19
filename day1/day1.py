print("hello world");

# disable line break
print("FirstName",end=' ');
print("LastName");

print("test for tab \t \t space");

# r act as regular expression will replace special chars 
print(r"Hi \n how are you");
#or not want to user "r" then can do it manually

print("Hi \\n how are you");

print("hello print text in quotes \"text in quotes\"");
# or can we doen using single quotes
print('hello print text in quotes \"text in quotes\"');

# print a lasge tetx on write in multiple lines use tripple quotes """

print(""" test multiple linnes text testfirst
      sendoc 
      
      thskjd
      """);
a= 67;
b= 4.5
print(a);
print(type(a));

print(b);
print(type(b));

# sum of two num

c= a+b;
print("Sum of a and b is ",c);

# delcare veriable in single line
a,b = 11,7;
print("value of a",a);
print("value of b",b);
# assign same value to miltiple varibales
a =b=11;
print("value of a",a);

print("value of b",b);

# get input from user
input1 = input("Enter firstname");
input2 = input("Enter lastName");

print("value of input1",input1);

print("value of input2",input2);
print("FUllNAme",input1 + input2)

# get input from user and parse to int
num1 = input("Enter first num");
num2 = input("Enter second num");
sum= int(num1)+ int(num2);
print("value of num1",num1);

print("value of num2",num2);
print("Sum of num",sum);


