date=int(input("enter your date of born:"))
max_date=31
month=int(input('enter your birthday month(1-12) :'))
max_month=12
year=int(input("enter your year of born:"))
max_year=2025
if date>max_date or month>max_month or year>max_year:
    print("enter valid date of birth ")
if (month==3 and 21<=date<=31) or (month==4 and 1<=date<=19):
    print("your zodiac sign is ARIES")
if (month==4 and 20<=date<=31) or (month==5 and 1<=date<=20):
    print("your zodiac sign is TAURUS")
if (month==5 and 21<=date<=31) or (month==6 and 1<=date<=20):
    print("your zodiac sign is GEMINI")
if (month==6 and 21<=date<=31) or (month==7 and 1<=date<=22):
    print("your zodiac sign is CANCER")
if (month==7 and 23<=date<=31) or (month==8 and 1<=date<=22):
    print("your zodiac sign is LEO")
if (month==8 and 23<=date<=31) or (month==9 and 1<=date<=22):
    print("your zodiac sign is VIRGO")
if (month==9 and 23<=date<=31) or (month==10 and 1<=date<=22):
    print("your zodiac sign is LIBRA")
if (month==10 and 23<=date<=31) or (month==11 and 1<=date<=21):
    print("your zodiac sign is SCORPIO")
if (month==11 and 22<=date<=31) or (month==12 and 1<=date<=21):
    print("your zodiac sign is SAGITTARIUS")
if (month==12 and 22<=date<=31) or (month==1 and 1<=date<=19):
    print("your zodiac sign is CAPRICON")
if (month==1 and 20<=date<=31) or (month==2 and 1<=date<=18):
    print("your zodiac sign is AQUARIUS")
if (month==2 and 19<=date<=29) or (month==3 and 1<=date<=20):
    print("your zodiac sign is PISCES")

