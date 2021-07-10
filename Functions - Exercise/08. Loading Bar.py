percentage_loaded = int(input())


def loading_bar(a):
    percent_symbol_to_be_repeated = int(a/10)
    loading_bar = ""
    for percent_symbols in range(percent_symbol_to_be_repeated):
        loading_bar += "%"
    for dot_symbols in range(10 - percent_symbol_to_be_repeated):
        loading_bar += "."
    if percent_symbol_to_be_repeated == 10:
        print(f"{percentage_loaded}% Complete!")
        print(f"[{loading_bar}]")
    else:
        print(f"{percentage_loaded}% [{loading_bar}]")
        print("Still loading...")


loading_bar(percentage_loaded)