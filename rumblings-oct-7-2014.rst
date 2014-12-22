Batch renaming with a Python program (and the mess one could make !):
--------------------------------------------------------------------

Warning: Do not try this on data you didn't backup! (That's the whole point of this post on the experiment on experiment!!!)

As part of an experiment, we collected readings in real time and named the log files with this convention:

*<distance in no.>* _feet_between_ *<integer 1>* _and_ *<integer 2>* _power *<power level>* .txt

These file names were set manually for every trial. As we are halfway through our trials, it was detected that we were moving at double the intended distance.

With the confidence we entrusted in Python (giggles :) ), we proceeded with the same scheme till the end and finished the experiment.

Now, it is the time to write a Python script that -

- Reads file name of every file in a directory
- Extracts the first digit it finds (the distance)
- Doubles it in place using some regular expression
- Then renames the file

    :: python

import os
import re

count = 0
for filename in os.listdir("."):
    nums = re.findall('\d+', filename)
    if nums:

        newname = re.sub(nums[0], str(int(nums[0])*2), filename)
        os.rename(filename, newname)
        count += 1
        print count, ': Renamed ', filename, ' as ', newname
        print "\n"
    ::

Seemed good at the first sight. Repeted the execution (aware that the numbers are going to be doubled again! You have been warned, aren't you?) but suspected something with the 'count'!

For every repeated execution, the count is getting smaller. Strange !!

The original files we collected were 39. After one execution opf the script, the count was 31, then 29 and 28 !! The script is eating up our data!!

Well, it turns out to be that the numberss that were already doubled matched the existing files and replaced those.. Huh!

Need to tweak the script in some way or work on sets of files such that they don't clash

A similar discussion was found here: http://stackoverflow.com/questions/22199552/python-os-rename-module-deletes-files
