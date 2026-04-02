import argparse

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

BOLD = "\033[1m"
DIM = "\033[2m"

BOLD_RED = "\033[1;91m"
BOLD_GREEN = "\033[1;92m"
BOLD_YELLOW = "\033[1;93m"
BOLD_BLUE = "\033[1;94m"
BOLD_MAGENTA = "\033[1;95m"
BOLD_CYAN = "\033[1;96m"
BOLD_WHITE = "\033[1;97m"


class ColorHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def format_help(self):
        help_text = super().format_help()
        help_text = help_text.replace("usage:", f"{BOLD}usage:{RESET}")
        help_text = help_text.replace("positional arguments:", f"{BOLD_BLUE}arguments:{RESET}")
        help_text = help_text.replace("options:", f"{BOLD_BLUE}options:{RESET}")
        help_text = help_text.replace("examples:", f"{BOLD_BLUE}examples:{RESET}")
        # colorize argument names
        import re
        help_text = re.sub(r'(  -[\w-]+)', f'{BOLD_CYAN}\\1{RESET}', help_text)
        help_text = re.sub(r'\b(markdown_path|output_path)\b', f'{BOLD_CYAN}\\1{RESET}', help_text)
        return help_text