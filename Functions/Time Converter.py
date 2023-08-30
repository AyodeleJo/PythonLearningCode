def split_Time(time):
    t, ampm = time.split()
    h, m = t.split(":")
    return get_24hr_format(h, ampm), m


def get_24hr_format(hh, ampm):
    hh = int(hh)
    if ampm == "pm":
        if hh != 12:
            hh = hh + 12
    elif hh == 12:
        hh = "00"

    return hh


# main
answer = 'yes'
while answer == "yes":
    time = input("Enter time in 12 hour format:")
    print("The time in 24 hour format is:", split_Time(time)[0], split_Time(time)[1], 'hours')
    answer = input("Do you want to convert another time (yes/no)?")