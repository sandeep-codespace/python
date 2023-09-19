# area of cirle
# calculated as  πr2
pie = 3.14;
radius = input("Please enter circle radius (cm): ");
radiusValue = int(radius);
circleArea = pie * radiusValue * radiusValue;

print("Area of circle for "+ radius +"(cm) radius is: ", circleArea);


# simple interest
# calculated as  SI= (P × R × T)/100
principal = input("Please enter Principal amount: ");
rate = input("Please enter Rate of Interest in %: ");
time = input("Please enter Time (years): ");
simpleInterest = (int(principal) * int(rate) * int(time))/100;

print("simple interest for P = "+ principal +",R =" +rate+ ", T = "+time+" is: ", simpleInterest);



# swap two number
# with three variables
firstValue,secondValue = 8,21;
print("First Value:", firstValue);

print("Second Value", secondValue);
swapVaribale = secondValue;
secondValue = firstValue;
firstValue = swapVaribale;

print("After swap");
print("First Value:", firstValue);

print("Second Value", secondValue);

# with two variables
firstValue,secondValue = 4,5;
print("First Value:", firstValue);

print("Second Value", secondValue);
secondValue = firstValue + secondValue;
firstValue = secondValue - firstValue;
secondValue = secondValue - firstValue;   

print("After swap");
print("First Value:", firstValue);

print("Second Value", secondValue);

# swap of three numbers

firstValue,secondValue, thirdValue = 4,5,7;
print("First Value:", firstValue);

print("Second Value", secondValue);
print("Third Value", thirdValue);

firstValue = firstValue + secondValue + thirdValue;
thirdValue = firstValue - (secondValue+thirdValue);
secondValue = firstValue - (secondValue+thirdValue);
firstValue  = firstValue - (secondValue+thirdValue);

print("After swap");
print("First Value:", firstValue);

print("Second Value", secondValue);
print("Third Value", thirdValue);
