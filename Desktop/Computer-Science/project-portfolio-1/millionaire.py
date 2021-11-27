#Who wants to be a millionaire game. 
"""

Question number	Question value
1	£100
2	£200
3	£300
4	£500
5	£1,000 * guranteed cash
6	£2,000
7	£4,000
8	£8,000
9	£16,000
10	£32,000 * guranteed cash
11	£64,000
12	£125,000
13	£250,000
14	£500,000
15	£1,000,000
"""
# Greeting

print("Hello, what's your name?")
name = input()
print("Do you want to be a millionaire " + name + "?")
answer = input("Y/N ")
answer.upper()
if answer == "Y":
    print("Then lets play! Good luck!")
else:
    print("Then you should play another game. Goodbye!")





