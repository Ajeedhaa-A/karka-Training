days=["sunday","monday","tuesday","wednesday","Thursday","Friday","saturday"]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
def user(d):
        if d>=7:
          return (days[d-1])
def m(month):
        if month>30:
           return(months[month-1])
def y(year):
        if year>2020:
          return year
d=int(input("day"))
month=int(input("month"))
year=int(input("year"))       
print(f"Yes You are in {days[d-1]},{months[month-1]},{year}")       
