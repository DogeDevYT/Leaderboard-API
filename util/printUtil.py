from colorama import Fore, Style

class TextPrinter:
    @staticmethod
    def print_text_in_color(text_to_print, color):
        if color == 'green':
            print(f"{Fore.GREEN}{text_to_print}{Style.RESET_ALL}")
        elif color == 'red':
            print(f"{Fore.RED}{text_to_print}{Style.RESET_ALL}")
        else:
            print(text_to_print)  # Print without color if not green or red