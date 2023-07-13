p=1000
n=10
r=5
#interest=calculation(p,n,r)
#print(calculation(p,n,r))

def calculation(principal,next_year,rate_of_interest):
    interest=principal*next_year*rate_of_interest
    return interest
interest=calculation(p,n,r)
print(calculation(p,n,r))
