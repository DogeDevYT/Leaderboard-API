from colorama import Fore, Back, Style

def print_text_in_green(text_to_print):
    print(f"{Fore.GREEN}{text_to_print}{Style.RESET_ALL}")
def print_text_in_red(text_to_print):
    print(f"{Fore.RED}{text_to_print}{Style.RESET_ALL}")