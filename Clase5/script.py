import os
branch = os.environ['BRANCH']

for x in range(1,11):
    if x <= 9:
        print("Hello curso desde staging " + branch +  ": " + str(x))
    else:
        print("Bye!")
