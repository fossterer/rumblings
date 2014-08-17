Having become comfortable with 'Mozilla Firefox' bug fixing (15 bugs and counting), I am adding one more project to my list; gnome-screenshot

Know the application powered by this project? Well, this is what appears when you hit the 'PrintScr' button on your keyboard. **Why did I choose this project?** When I was still figuring out my way around various open source projects, I happened to notice one thing in the Ubuntu distro I've been using. I am a fan of making screenshot to capture various scenarios and hence I use the default 'PrintScr' button to make them. The dialog box then appears does highlight the 'File Name to save' entry but my editing does not reflect there! Counter-intuitive., right? In the next few weeks, I figured out that the bug/issue/whatever (my flow of ideas at that time..) is specific to a *package* 'gnome-screenshot' rather than the os 'Ubuntu'.

A few weeks later I became aware of 'apt-get source <pkg-name> usage' and the Bazaar & git workflows. One day while I was going through the 'Update Information' in the regular 'update-manager' GUI, I found a commit message with exactly the same description (which I thought of earlier!!). Excited, I went to the bug number reported and read the 'patches' uploaded. Little did the content in the 'patch' made sense to me but I got a glimpse of various terms there.

Now after all these days and coding for 'Mozilla project' (and seeing my name 15+ times in the commits list!), I see that -

 - Gnome project uses git which is analogous to hg used by Mozilla
 - Gnome uses Bugzilla which is the same for Mozilla (and hence I am familiar with meanings of 'keywords', 'mentors', types of mails to expect in my inbox etc.)

Having found a few feature requests in the projects's Bugzilla page that I can do, now I start my endeavour with a 'git clone...' without a doubt :-)
