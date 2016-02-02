"""
Background
~~~~~~~~~~

The script in this directory calculates the number of rows in a file that
satisfy a certain expression.

The name of the file to process can either be provided to the script from the
command line or on stdin.

Problem
~~~~~~~

Write a program to call out to calculate.py operating on sp500hst_part.txt
in this directory. 

1) Using command line arguments

2) Using a pipe to communicate via stdin

Bonus
~~~~~

The script can actually take an expression to evaluate either as an
additional command line argument or as an additional string passed to
stdin.

Repeat 1) and 2) but change the expression to {6} > 50000

"""


from subprocess import Popen, PIPE

# Part 1

ret = Popen(["python", "calculate.py",
             "sp500hst_part.txt"]).wait()


# Part 2

p = Popen(["python", "calculate.py"], stdin=PIPE, stdout=PIPE)
print p.communicate(input="sp500hst_part.txt")[0].strip()
# or
# p.stdin.write("sp500hst_part.txt")
# p.stdin.close()
# print p.stdout.read().strip()


# Bonus 1

ret = Popen(["python", "calculate.py",
             "sp500hst_part.txt", "{3} < 53.0"]).wait()

# Bonus 2

p = Popen(["python", "calculate.py"], stdin=PIPE, stdout=PIPE)
p.stdin.write('sp500hst_part.txt')
p.stdin.write(' {6} > 50000')
p.stdin.close()
print p.stdout.read().strip()



