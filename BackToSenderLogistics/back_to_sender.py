amount_per_parcel = [160, 200, 250, 500]
base_pay = 5000
def get_price(number):
    if number < 50:
         return number * amount_per_parcel[0] + base_pay

    elif number ==  50 and number < 60:
        return number * amount_per_parcel[1] + base_pay

    elif number == 60 and number < 70:
        return number * amount_per_parcel[2] + base_pay

    else:
        return number * amount_per_parcel[3] + base_pay
