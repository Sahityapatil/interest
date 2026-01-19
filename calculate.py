def interest(p=1000, r=5, t=2):
   si = (p*r*t)/100
   ci = p * (1 + r/100)**t
   return si, ci

if __name__ == "__main__":
   print("Simple Interest and Compound Interest:", interest())

 

