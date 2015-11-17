Epic failure!! [Untested]

http://stackoverflow.com/questions/5199359/why-do-people-still-use-primitive-types-in-java/5199425#5199425

Why does (3) return true and (4) return false?

Because they are two different objects. The 256 integers closest to zero [-128; 127] are cached by the JVM, so they return the same object for those. Beyond that range, though, they aren't cached, so a new object is created. -- As stated in the answer above
