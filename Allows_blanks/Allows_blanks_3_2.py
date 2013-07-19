#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 Wolf Halton <wolf@sourcefreedom.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#!/usr/bin/env python
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



def main():
    # build tests into your code
    chk = 'moo'
    while chk == 'moo':
        myvar = ''
        myvar = str(input("enter something for myvar   "))
        bubb = len(myvar)
        print(chk, "Is chk 1,   ", bubb, 'is bibb,  and  ', myvar , "is myvar")
        if bubb < 1 or bubb > 9:
            print("\nplease enter a value for myvar between 1 and 9 characters\n")
            bubb = len(myvar)
            print(chk, "Is chk 2,   ", bubb, 'is bibb,  and  ', myvar , "is myvar")
        else:
            chk = 'Baaaaah'
            print(chk, "Is chk 3,   ", bubb, 'is bibb,  and  ', myvar , "is myvar")

if __name__ == '__main__':
	main()

