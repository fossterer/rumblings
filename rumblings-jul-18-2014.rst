Understanding NS-3 (Part-1)
---------------------------

**NOTE:** The following series is just a log of how I'm understanding the functioning of NS-3 and hence the flow of the article is mostly inclined towards my thought process. In other words I warn you not to scorn at me for not writing a proper "tutorial" which it is not!

Copied the examples from src/examples/turorials/ to scratch/. I could run them to see the output but am still skeptical if this would be of any help. My goal is to 'implement OLSR on a mobile node network'. How am I going to achieve it?

The questions which I am facing at this point are:

* If I were to implement a truly mobile network how can I be sure that it is "mobile"?
* Can I visually appreciate the 'working of OLSR' onc eimplemented?

All I need is [love? nah:P] 'to have a graphical representation of the things going on'. How do I have **graphical representation**?

Tried running './waf --run scratch/first --vis' but it ran happily without any graphical window!

As http://www.nsnam.org/wiki/Index.php/PyViz states, I need to add two simple lines to any existing program!

.. code:: c++

    CommandLine cmd;
    cmd.Parse(argc, argv);

*Beleive me! I wrote these lines now without looking at the wiki or my implementation; very simple. Aren't they?*

Running again produced this window. Voila!

Now to better appreciate the things going on all I did was to -

* Modify 'DataRate' to as low as 1 Kbps
* Modify/Delete 'Delay' paramater

so that I can *see* things happening in front of my eyes. Yes I did!

The next part of the article focuses on 'how I add mobility to three nodes and **see** them moving while transmitting'!
