# File that opens the game in new terminal. For now working only in Windows (11 tested)
# TODO: Opening in other os

import os


color_cmd = "color 08"

if __name__ == '__main__':
    os.system(f'start cmd /c "{color_cmd} && python engine.py"')
