# **kwargs Printer 

# w.a.f that accepts any keyword arguments and prints them as "key: value" lines.

def show_info(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Asha", age=25, city ="Kolkata")