               # diff between 2 dates #

from datetime import date

fy=int(input("year:"))
fm=int(input("month:"))
fd=int(input("day:"))
f_date=date(fy,fm,fd)
print("the joining date is",f_date)
#ly=int(input("year:"))
#lm=int(input("month:"))
#ld=int(input("day:"))
#l_date=date(ly,lm,ld)

l_date=date.today()
print("the resign date is",l_date)



delta=relativedelta.relativedelta(l_date,f_date)

print(delta.days,'days')