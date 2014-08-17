Why can't regex be simple? -- ComposedRegex
--------------------------------------------

http://martinfowler.com/bliki/ComposedRegex.html
Mr Martin Fowler deals with this well. The idea is to make regex 'readable' no more than the directive to produce 'human readable code' in the discipline of Software Engineering.

Ideas:

- The approach dealt with is more of 'introducing programming language specific patterns in regular expressions'.
- That the parts of a regex can be split and individually assigned meaningful names is revolutionary. This way the final regex can be seen simply as a meaningful collection of tokens.
- Moreover, having individual tokens with specific names makes them reusable.
- This way, the approach presented is a way of improving "readability as well as reusability in Regular Expressions by implementing Programming Language specific design guidelines"

NOTE: The approach is of making the Regular Expressions more of a human-understandable peices as today's programming language implementations than arcane and archaic collections of weird symbols
