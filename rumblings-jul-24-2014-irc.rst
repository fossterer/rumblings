 
15:13*** fossterer joined #gnome-love
For developers who want to become GNOME hackers
Topic set by gpoo on Tue Feb 11 2014 16:07:47 GMT-0500 (EST)
15:13fosstererHi! How to build & install gnome-common?
15:14fosstererI did a 'configure' and 'make'. What else?
15:14*** sig9 quit (Ping timeout: 600 seconds)
15:19*** ljubak joined #gnome-love
15:21andre_make install.
15:23*** rashi joined #gnome-love
15:24fosstererandre_: Done!
15:24fosstererproceeding to gnome-screenshot
15:25fosstererError: No package 'libcanberra-gtk3' found
15:25fosstererandre_: --^
15:26andre_fossterer, so what do you think?
15:26andre_and do you have a question?
15:26fosstererIt's already installed..
15:26fosstererconfirmed from 'apt-cache policy'
15:27fosstererWhy does it say 'not found'?
15:29fossterer-dev file?
15:29fosstererDo I need it installed rather?
15:34*** aday quit (Ping timeout: 600 seconds)
15:34*** brion quit (brion)
15:34fosstererAlright! build completed till 'make'
15:35fosstererNow where would the executable be?
15:35fosstererHelp!!!
15:37*** vkmc joined #gnome-love
15:37fosstererandre_: --^
15:37andre_I have no idea what you are doing and what your question is.
15:37andre_steps to reproduce welcome.
15:38fosstererI built gnome-screenshot using 'make'. That was successful
15:38andre_In general, if you compile and develop on software, you need to have the corresponding development packages installed.
15:38andre_so if no package 'libcanberra-gtk3' is found, you need to make sure that the development package for that package is installed.
15:38andre_is it?
15:39andre_and the executable is where you defined the output in the parameters that you passed in the configure call.
15:39fosstereryeah.. ok. I did that
15:39fosstererNow, where is that 'final executable' of gnome-screenshot to run
15:39fossterer?
15:39andre_and the executable is where you defined the output in the parameters that you passed in the configure call.
15:39fosstererI ran './autogen.sh' and 'make'
15:39andre_which documentation are you actually following to do this?
15:39fosstererDidn't specify any output directory
15:40andre_then it's in the default.
15:40fossterer'default'? define please
15:41andre_I don't know your system, so I don't know your default.
15:41andre_well.
15:41fosstererUbuntu
15:41andre_again: which documentation are you actually following to do this?
15:41andre_shrug. I don't know Ubuntu.
15:41fossterernone.
15:41andre_great.
15:42fosstererI am not using 'jhbuild'
15:42andre_then I do recommend to find and read a guide.
15:42andre_configure and make and make install on one page are recommendable search terms.
15:42*** saurabh_P quit (Read error: 145 (Connection timed out))
15:43andre_I'm not sure if you intentionally wanted to overwrite your stable system binaries and libraries anyway to make your system unstable.
15:43fosstererI just did a make.. not 'make install'. Now how do I know where that executable went?
15:44andre_the output of make should have told you.
15:44fosstererI am not able to find the development page for gnome (Not the one which pushes 'jhbuild' to me)
15:45andre_why would you want to find a development page for gnome?
15:45andre_I don't really get the connection.
15:45fosstererI meant the page - 'which documentation you are using'
15:46andre_I use jhbuild when I compile stuff.
15:47andre_and https://developer.gnome.org is the central resource.
15:48fosstererIt went into src/
15:51fossterer'src/gnome-screenshot' is working. My screen flashes but I don't see a dialog box asking me to save!
15:51andre_as intended.
15:52fosstererWhy?
15:52andre_~/Pictures
15:52andre_by design.
15:52fosstererDoes that mean the 'Ubuntu variant' alone shows the dialog box?
15:54andre_likely.
15:54andre_there's no dialog in upstream by default.
15:55fosstererIn that case, what should I make of this?
15:55fosstererhttps://bugzilla.gnome.org/show_bug.cgi?id=688061
15:55ServicesBug 688061: minor, Normal, ---, gnome-screenshot-maint, VERIFIED FIXED, When opening gnome-screenshot via hotkey, the name field is highlighted but does not have text focus.
15:55andre_what does "make of this" mean?
15:56fosstererIsn't that "the" dialog box?
15:56andre_it's a bug report that was closed.
15:56andre_what's the question?
15:56fosstererI mean:
15:56hashemandre_, fossterer if you run gnome-screenshot it doesn't show the ui
15:56andre_ah. that 3.8.1 should have the dialog.
15:56hashemyou have to run gnome-screenshot -i
15:56andre_yeah. parameter. hashem knows better than I do.
15:56fossterer"the above bug report is about 'missing focus in a dialog box'. So where is "that dialog box"?
15:57fosstererohh.. Thanks hashem:
15:57*** maweki quit (Leaving.)
15:57hashemfossterer, I have no idea. You should ask cosimoc in #gnome-hackers
15:57andre_it's not displayed by default.
15:58hashemthat ticket may be old and not applicable any more
15:58andre_plus you're looking at a bug report for 3.6 and 3.8
15:58hashemit's hard to tell from the description
15:58andre_yeah. that's more than one year ago.
15:58andre_things change.
15:58fosstererok.. hashem.. -i did the thing
15:59fosstererand the bug report.. that was just a pointer to explain 'my idea of the dialog box'.. Don't mind
15:59fossterer
15:59fosstererThanks andre_:
15:59andre_sure
16:00fosstererOne more question!
16:01fossterer1. On my regular Ubuntu system, gnome-screenshot alone display the "Where to save" dialog box
16:02fossterer2. gnome-screenshot -i displays a 'choose what to capture' dialog box before beginning the capture too, in addition to the second dialog as said above
16:02andre_Ubuntu patches?
16:02andre_(my guess)
16:03fossterer"Ubuntu patches"... andre_: Now you tell me to go to Launchpad and compare them on my own?
16:03andre_no, I just told you that likely Ubuntu has custom patches that change the behavior.
16:03andre_that's all.
16:03andre_I didn't tell you to analyze anything on your own, but I won't stop you from that either
16:03fosstererOk..
16:03fossterer
16:07fosstererI did an 'apt-get source gnome-screenshot' to find a file "gnome-screenshot-3.10.1/debian/patches/ubuntu_interactive_screenshots.patch' !!!
16:08fosstererIt has two occurrences of "- if (screenshot_config->interactive) "
16:08fossterer[A deletion]
16:10andre_yeah, that might be it
16:11fosstererHeyy! Today I learned 'to read the output of "make" ' and 'that Ubuntu's variants ship with certain patches by default'!
16:12fosstererIf I am getting started with bug fixing, is this the right to channel to stay in?
16:12andre_heh, definitely!
16:12fosstererThank you
16:13andre_but I really recommend to not overwrite your stable system binaries but to "make install" to another place
16:13andre_(of course you can if you know what you're doing)
16:13fosstererDoes make isntall take 'arguments'?
16:13andre_configure and autogen.sh do
16:14fosstererohh
16:14andre_(I think. As I said, I normally use jhbuild which also handles dependencies)
