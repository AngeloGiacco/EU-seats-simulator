#🇪🇺EU-seats-simulator🇪🇺

A simple script written in Python that will simulate the number of seats given to a particular party.

The rule for assigning the seats to parties is as follows:

the first seat goes to the party with the highest percentage of votes, its percentages
is updated to be its original percentage divided by one plus the number of seats it has (so in this case halved).

the second seat is assigned to the the party with the highest updated percentage.

For example, consider the following results:

BRX = 45%

LD = 20%

LAB = 16%

GREEN = 11%

CON = 6%

UKIP = 2%

Let's say there are five seats to be assigned.

The first is given to BRX whose percentage is now 45/2 = 22.5

The second is given to BRX whose percentage is still highest and their percentage is updated to 45/3 = 15

The third is given to LD whose percentage is now highest and their percentage is updated to 20/2 = 10

The fourth is given to LAB whose percentage is now highest and their percentage is updated to 16/2 = 8

The fifth is given to BRX whose percentage is now highest and their percentage is updated to 45/4 = 11.25

So the results are

BRX 3
LD 1
LAB 1
Rest all get 0.
