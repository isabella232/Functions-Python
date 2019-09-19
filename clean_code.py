# Here's more organized and modular code which serves the same purpose as the code in messy_code.py!

temps = {"Cairo": 13.6, "Beijing": -3.1, "Mumbai": 23.7, "Tokyo": 5.2, "Rome": 7.5, "London": 4.3, "New York": 0.6}


def c_to_f(c_temp):
    f_temp = (9.0/5.0)*c_temp + 32
    return f_temp


for t in temps:
    print(t, c_to_f(temps[t]))