has_high_income = False
has_good_credit = True
has_criminal_reord = True

if has_high_income and has_good_credit:
    print("Eligible for loan - 1")

if has_high_income or has_good_credit:
    print("Eligible for loan - 2")

if has_good_credit and not has_criminal_reord:
    print("Eligible for loan - 3")

# AND: both
# OR: At least one
# NOT: Makes True -> False or viceversa
