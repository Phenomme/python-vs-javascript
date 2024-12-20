# get name 

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# def get_name():
#     name = input("What is your name? ")
#     return name

# Write a method that reverses a string. Here’s the javascript:


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

# def reverse_it():
#     string = "a man, a plan, a canal, frenemies!"
#     reverse = ""

#     for i in range(len(string)):
#         reverse += string[len(string) - (i + 1)]

#     print(reverse)

# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

# def swap_em():
#     a = 10
#     b = 30

#     temp = b
#     b = a
#     a = temp

#     print("a is now {a}, and b is now {b}")

# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# def multiply_array(ary):
#     if len(ary) == 0:
#         return 1

#     total = 1

#     for i in range(len(ary)):
#         total = total * ary[i]

#     return total

# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

# def fizzbuzzer(x):
#     if x % (3 * 5) == 0:
#         return "fizzbuzz"
#     elif x % 3 == 0:
#         return "fizz"
#     elif x % 5 == 0:
#         return "buzz"
#     else:
#         return "archer"
