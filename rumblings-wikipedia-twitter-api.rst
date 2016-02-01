Today as I wrote this down in Wikipedia's https://15.wikipedia.org/?pk_campaign=kiwi&pk_keyword=anon page --

the go-to resource to get basic knowledge of a thing & a fact-check database for any historical event http://15.wikipedia.org #wikipedia15

and clicked on 'Tweet', I found that only this was showing up

the go-to resource to get basic knowledge of a thing 

at

https://twitter.com/intent/tweet?text=the+go-to+resource+to+get+basic+knowledge+of+a+thing+&+a+fact-check+database+for+any+historical+event+http://15.wikipedia.org+#wikipedia15&hashtags=wikipedia15&url=http%3A%2F%2F15.wikipedia.org


Obviously, the culprit is the character '&'. Is this a known common programming mistake? Shouldn't the API be properly 'escaping' them?

How would one go about implementing the idea I just conceived?

- Store the data typed by the user into a buffer
- Do appropriate checks and do HTML-encoding and other preprocessing steps
- Then pass it to the destination buffer  
    
