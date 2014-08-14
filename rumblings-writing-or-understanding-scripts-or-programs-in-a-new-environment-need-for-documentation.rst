Not a 'How To' of NS3 but of any package/environment - Need for Documentation:
-------------------------------------------------------------------------------
(No familiarity with NS3 needed)

I feel amused when I think of the length this post is going to assume. UPDATE: 'amused' initially becuase I thought this woul;d the shortest. Now that I'm finishing this post, I see it turned out the other way :D (nevertheless, still amused!)

I started out to write a blog post on 'How I found out why my NS-3 scripts are producing weird data as logs though my advisor was alright with what I'm showing'. (Head hurts, huh!?) In short, I 'defined a new Log component' for my script but enabled a different component which of course is used in my current script. Just after a hunch when I modified my script as appropriate I found that a few logging statements I made earlier but never showed up are indeed showing up now!

Feeling great I proceed to make a post on 'how one should begin writing NS3 scripts'  or in fact 'how to understand any first script/program in an environment'. My next was to search over the Internet if anyone has already blogged about it given the fact that NS3 has been in use for many years now (probably before I even knew computers/I was born :P)
https://www.google.com/search?client=ubuntu&channel=fs&q=understanding+an+ns3+script&ie=utf-8&oe=utf-8.

Took the second result. http://www.nsnam.org/support/faq/writing-scripts/ Huh!? NS3 itself wrote about this! Well, is it any different from what I have been observing recently after working with various projects & environments? No. Every project/enironment/whatever has a documentation. Read it people! That should be our 'first point of reference'. All these blogs/tutorials are secondary (Beware! I have not said 'unnecessary'. I'll come to this later). I am pressing on this because of the amazement I experienced after setting up ROS environment in my lab for a motion-tracking Laser device which I hardly had any experience with.

Q) With what courage did I set on to do it?
A) I beleived that if ROS was suggested by the service guy (from the making company of the device) it should have been an established environment which many should be using by now. Hence ROS must be very extensively being used somewhere probably out of my scope so far. So there must be documentation. I read it.. I read it.. I did it.. Oh my! "What a beautifully documented thing!!" I was greatly appreciating the people behind the documentation. I could see which of them we might be needing to play more with in the near future to do our project. All this was due to the 'Documentation'. Documentation, the thing I always felt sorry about when I think that I no longer have access to the original manuscripts the yesteryear researchers and scientists never cared to produce/people of the later years didn't care to preserve and pass on.
*Conclusion:* The 'original documentation' from the 'original manufacturers' should be our 'First point of reference'. If it doesn't serve to be so, the product itself would be 'less usable'

Q) Did I just conclude that all the blogs/articles coming from non-makers are wortheless?
A) This is what I meant to address when I said 'I'll come to this later'

No. Yesterday I was challenged to 'setup a [Apache] web server'. I was aware that I was being given more than the required time to 'just setup a web server software' as literally speaking it takes 15 min when in fact had no limits on how much time I take to do so (my current focus at CyberWVU). I took it as 'setup a webserver such that it is perfectly usable, as indestructible and secure as possible, fine tuned in all possible respects.' Now that is challenging enough given my current experience of 'installing software' (LOL! 'installing' was a big & thrilling enough word a few years ago for me).

Naturally I was at the "Apache's" web pages to 'do just what is requireed to setup a web server software for it to be up and running'. Now, why does my installation say 'No NameServer defined: Defaulting to something my foster parents/forefathers/foremothers knew blah..! blah..! ?? I don't leave such cases. I need to delve into deeper matters to find out 'what I did' but 'what is expected'. This could be a 'configuration issue' that I might be troubling with later OR a 'security issue' which someone would take advantage of later.

Is Apache caring about all this random stuff which random users might be facing? Less likely to expect from an organisation which is handling too many other projects and also when 'Documentation' itself is a task and having presented everything that one needs to 'set things up and running' it would not be fair to blame them for not handling things (also when not many are caring why these are happening that way, spending their resources on these things may not show good ROIs for them!)

Now, who should care to produce the rest of the documentation?
*Bloggers!*
*Users who went through such things already!*
**Document it yourself!!** You might be helping someone who need it/need to know. Do your part and your next generation users would build from there. Unless your previous users (of the same/similar products) cared to do so you wouldn't be doing what you are able to do now this efficiently!
*Conclusion:* The 'notes/tips/thing-to-do-after-installing posts by bloggers' should be our 'next points of reference'. They would dealing with 'general pitfalls', 'corner cases' which are more likely encountered in your later points of usage of that product. If none exist, **Create them yourself**
