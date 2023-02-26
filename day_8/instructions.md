# Caesar Cipher

A Caesar cipher is a simple encryption technique where each letter in a message is shifted a fixed number of positions down the alphabet.

### Steps followed to complete the project

#### Challenge 1 - Encryption

* Create a function called `encrypt` that takes the `text` and `shift` as `inputs`.

* Inside the `encrypt` function, shift each letter of the `text` forwards in the alphabet by the shift amount and print the encrypted text.  
e.g.  
`plain_text` = "hello"  
`shift` = 5  
`chipher_text` = "mjqqt"

>What happens if you try to encode the word 'civilization'? 

* Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#### Challenge 2 - Decryption

* Create a different function called `decrypt` that takes the `text` and `shift` as inputs.

* Inside de `decrypt` function, shift each letter of the `text` *backwards* in the alphabet by the shift amount and print the decrypted text.  
e.g.   
`cipher_text` = "mjqqt"  
`shift` = 5  
`plain_text` = "hello"  
print output: "The decoded text is hello"  

* Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.