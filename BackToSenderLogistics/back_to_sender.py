amount_per_parcel = [160, 200, 250, 500]
base_pay = 5000


def get_price(number):
    validate_input(number)

    if number < 50:
        return number * amount_per_parcel[0] + base_pay
    elif number < 60:
        return number * amount_per_parcel[1] + base_pay
    elif number < 70:
        return number * amount_per_parcel[2] + base_pay
    else:
        return number * amount_per_parcel[3] + base_pay


def validate_input(number):
    if not isinstance(number, int):
        raise TypeError(f"{number} is not a valid number")

    if number < 0:
        raise ValueError("Number of parcels cannot be negative")
