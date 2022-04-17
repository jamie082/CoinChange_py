price_amount = 1.30

quarters = .50
nickle = .05
penny = .01
fifty_piece = .50

thisdict = {'quarters': 10, 'nickle': 5, 'penny': 6, 'fifty_piece': 1}

quarters_p = ["quarters"]

num = []

i = 1
while i < 2:
    for i in thisdict:
       num = quarters + nickle + penny + fifty_piece # add up key int's
       print(num)
       if i == 2:
           break
       i += 2
