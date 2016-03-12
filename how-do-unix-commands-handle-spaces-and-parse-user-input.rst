NOTE 1: As always, when I say Unix commands, I mostly mean the equivalent GNU/Linux commands; more precisely, The GNU utilities and/or bash (or similar shell) utilities.

NOTE 2: All the source code listings cited hereafter in this article are obtained from the 'Source code of ddrescue from the package "gddrescue" ' with due respect to the original author(s).

It is always advisable to 'backup all the existing data before you start a new work'. Yeah, especially while you are in a research environment where you don't know where the current process would end up (and equivalently in any other dont-know-whats-going-to-happen environment). The single-board-computers I've to use now are borrowed for the time being from another laboratory and befiore I play around with it, I better backup all the existing work (probably done by specialists from that lab) into a safe place. Hence I lookup 'bit by bit copy linux' and end up finding about 'ddrescue' utility. While it is being heralded over its predecessor 'dd' (Oh.. I always loved it very much..!) for its indication of progress (err.. Bad bad 'dd' :P) and simple logging I get intrigued by 'what makes 'the ddresue "the ddrescue" '?

apt-get source gddrescue

(Yeah, you don't need 'sudo' to get the source.. <3)

<img-1>

There are just 4 pairs of '.h' and '.cc' files and 5 additional '.cc' files. Whoa!

<img-2>
As can be inferred from the above, the users input time is being checked for the presence of *optional* day, month, hour and seconds units via a 'switch-case'.

Now, notice the 'parse()' ?? What is it doing ?

The 'Rational' brings us to 'rational.h' and 'rational.cc'

<img-3>

How elegant!!
Read the user input as a single 'const char *' string.
If none is supplied, return.
numerator = 0, denominator = 1
c = 0 // Wait for its real use later
assume a non-negative number

**As long as there are spaces, skip them !!**
If you find a 'positive sign', go ahead ?? Remember, we initially assumed that it is non-negative!
Else, change our assumption (no more an assumption :D ) to 'negative'
If immediately after skipping all the spaces (irrespective of the presence of any sign), what you got is not a digit or a decimal point, no way you got any meaningful number; Hence return.

Now as long as you are getting digits, handle each digit.
If you happen to come out of this loop for that you got a 'decimal point', go ahead and do the same code as earlier.

*IMPORTANT* Observe that the same code which was written before the decimal is repeated. Many of us would think of avoiding this repetetion by some or the other way. However, the approach of 'repeating' here, looks natural indeed. What's your take on this?

Thereafter, is the code for handling percentages and so on..

Finally the normalization is attempted for the constructed, (numerator, denominator) pair which is written in the same file.

Hence, I got my answers to a few questions I had earlier:
1) How can commands ignore spaces?
2) How can commands (in their 'man pages') say that the units are optional and yet handle them (especially when they can be permutations and combinations of numerous as here - days, months, hours etc.)?
3) How can commands handle the presence (or absence thereof) decimals?

Answers:
- by using 'switch-case' statements
- by gracefully abstracting out the handling pieces of code and applying modularity to the entire code structure (breaking down into different files)
