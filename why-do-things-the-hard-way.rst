Just now I faced a question -- "Why do you do things 'THE HARD WAY' all the time?" My answer then seemed unsatisfying to me myself. But after that 'hard way' (Copying files across user accounts using rsync than a fancy 'GUI application' - which loads up too many routines into memory and behaves as a big brother than letting me understand what goes wrong and why), now here I am.. 

'Could not update the ICEauthority file: /home/shashank/.ICEauthority'

Steps I followed (unsuccessful):
--------------------------------

ctrl + alt + f1

Login as a differnet user

   * sudo rm /home/shashank/.ICEauthority (Didn't work)
   * sudo rm /home/.Xauthority (Didn't work)

   1. sudo cp .ICEauthority /home/shashank/
   2. sudo cp .Xauthority /home/shashank/
   3. Logout and login as 'shashank' (still from the command line)
   4. sudo chown shashank .ICEauthority
   5. sudo chgrp shashank .ICEauthority
   6. sudo chown shashank .Xauthority
   7. sudo chgrp shashank .Xauthority

No use so far! Now heading to see what this .ICEauthority should actually be...
