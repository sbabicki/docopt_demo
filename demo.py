# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [arg4]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[arg4]
"""

from docopt import docopt
opt = docopt(__doc__)
print(opt)
print(type(opt))

def main(opt):
    print(opt["<arg4>"])
    print(docopt)
    print(type(docopt))
    
if __name__ == "__main__":
    main(opt)