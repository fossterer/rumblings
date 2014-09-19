The following script is being discarded as I managed to setup:

* 'E-mail' app for university mail
* 'GMail' app for personal mail

on my 3-days ago acquired 'OnePlus One' (shipped with Google Apps).

With duly turned on auto-synchronisation (Thanks to longer battery life - 3100 mAh and my conformance to check-mail-only-at-breaks-rule)

#Script Starts
for i in {'default','communications'}; do firefox --no-remote -P $i & done
#Script Ends
