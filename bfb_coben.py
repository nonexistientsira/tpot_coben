import random
#defining vote variables
donut_votes = 6409
eraser_votes = 6300
tennisball_votes = 6295
tv_votes = 6287
pen_votes = 6282
golfball_votes = 6267
puffball_votes = 6240
gaty_votes = 5818
barfbag_votes = 4960
pin_votes = 4938
needle_votes = 4929
coiny_votes = 4921

total_votes = 69646
#"total" variables, used for averages
donut_total = 0
eraser_total = 0
tennisball_total = 0
tv_total = 0
pen_total = 0
golfball_total = 0
puffball_total = 0
gaty_total = 0
barfbag_total = 0
pin_total = 0
needle_total = 0
coiny_total = 0
#amt each character loses
donut_loss = 0
gaty_loss = 0
barfbag_loss = 0
pin_loss = 0
needle_loss = 0
coiny_loss = 0
#bracketcounter's margin of error
contestant_se = 300
#other misc variables
total_simulations = 15000
for _ in range(total_simulations):
   donut_random_number = random.uniform(donut_votes-contestant_se, donut_votes+contestant_se)
   gaty_random_number = random.uniform(gaty_votes-contestant_se, gaty_votes+contestant_se)
   barfbag_random_number = random.uniform(barfbag_votes-contestant_se, barfbag_votes+contestant_se)
   pin_random_number = random.uniform(pin_votes-contestant_se, pin_votes+contestant_se)
   needle_random_number = random.uniform(needle_votes-contestant_se, needle_votes+contestant_se)
   coiny_random_number = random.uniform(coiny_votes-contestant_se, coiny_votes+contestant_se)
   randomnumberlist = [donut_random_number, gaty_random_number, barfbag_random_number, pin_random_number, needle_random_number, coiny_random_number] #compiles all the randomly generated numbers together
   min_value = min(randomnumberlist) # finds the minimum number
   #which contestant had the lowest generated number?
   if min_value == donut_random_number:
     donut_loss = donut_loss + 1
   if min_value == gaty_random_number:
     gaty_loss = gaty_loss + 1
   if min_value == barfbag_random_number:
     barfbag_loss = barfbag_loss + 1
   if min_value == pin_random_number:
     pin_loss = pin_loss + 1
   if min_value == needle_random_number:
     needle_loss = needle_loss + 1
   if min_value == coiny_random_number:
     coiny_loss = coiny_loss + 1

   
#calculating the percentages
donut_percentage_loss = (donut_loss/total_simulations)*100
gaty_percentage_loss = (gaty_loss/total_simulations)*100
barfbag_percentage_loss = (barfbag_loss/total_simulations)*100
pin_percentage_loss = (pin_loss/total_simulations)*100
needle_percentage_loss = (needle_loss/total_simulations)*100
coiny_percentage_loss = (coiny_loss/total_simulations)*100
#how many times each contestant had the least votes
print("Percentage of simulations lost")
print(donut_percentage_loss)
print(gaty_percentage_loss)
print(barfbag_percentage_loss)
print(pin_percentage_loss)
print(needle_percentage_loss)
print(coiny_percentage_loss)

 
