On first look, it appears "Java Money" is just an enthusiast's excited experimental proposal but just the initial slides the presentation [http://www.slideshare.net/rajmahendra/jsr-354-money-and-currency-api] reminded me of the value of having supported datatypes for every real-life object we use form day-to-day life. In a way it seems the 'Date', 'Time' etc. datatypes provide an easy way of 'abstracting' the real-life utilities which is the very idea of an object-oriented programming approach.

Java Money API is set to be unveiled with Java 9 as per [https://java.net/projects/javamoney/pages/Home]. The Java Specification Request (JSR) 354 is finallized as the day of this writing [Nov 16, 2015] and a dedicated URL [http://javamoney.org] exists to speak of the project.

Usecases?
----------

'ExchangeRate' could be a defined entity in my java code.
This can be a well-supported alternative to defining 'Double exchangeRate' or such

Interesting points are that this project aims to cover even the 'virtual currencies' which didn't occur to me at first -- The Facebook Credits, (Linden Dollars, anyone?), BitCoin etc. By abstracting out many such specificalities, this 'Java Money API' can make dealing with financial aspects easy to a programmer.

Added advantages of having a *dedicated* Money API is that, the handling of precision, rounding etc. aspects stay standardized. This definitely can be a motive for introducing new APIs, isn't it? Otherwise, there would be a lot of inconsistencies among software implementations by different developers/organsiations as they might be handling the rounding of currencies differently and new protocols have to be invented everytime between every two development teams.

Important of all, this topic brought to my attention that - 
 - OpenJDK is not any grassroots attempt but an official Java Project
 - Anyone can submit JSRs; In this case, The 'Java User Group Chennai'(JUGChennai) of India proposed it in 2013 and worked on it until it is going to be made available by default!! (Wait until Java 9)
