My 'very productive' encounter with "awk"
-------------------------------------------

Got a 328 MB log file (text) to look at. (emacs is already complaining :P) Interested only in certain definite portions of it. 'grep' tried to help me but 'oh poor! you can only do with 'individual lines' but not 'between the specific lines!' I know that you got -A and -B to consider 'after' and 'before' matched lines but I can't tell you the number of lines "definitely :(

Welcome 'awk'!! I know that you accept scripts and when I think of scripts, I think of "Programmability" :D I can ask you to loop between things - a 'for loop-lik' construct where I specify the 'begin value' and the 'end value'!

Wait!! This guy at http://stackoverflow.com/a/19177808/2135699 does it neatly!

The result - awk '/RoutingTableComputation begin/ {p=1}; p; /RoutingTableComputation end/ {p=0; print "\n"} ' olsr-in-mobile-network-dump-copy.

Short explanation: Here, 'p' acts as a 'condition variable' - set on identifying the successful detection of 'begin token'
                                                            - hence awk is allowed to do its "default" action i.e. 'print it' (Read this again! What a lovely exploitation/apt use of the default behaviour!)
							    - unset on identifying the successful detection of 'end token' (Observe the cute addition of 'printing a newline' at the end :) I love it!)
