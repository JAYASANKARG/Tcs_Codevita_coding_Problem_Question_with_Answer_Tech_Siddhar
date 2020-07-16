'''
Problem : Securing Financial Transactions 
Statement:
ABC Corporation's finance team wants to deal with each of their supplier's invoicing details in a more secured way.
Between ABC's and their suppliers' finance systems, ABC wants to build its own encryption/decryption logic.  ABC has a
unique identifier for each of their supplier and wants to use that as part of the sensitive data  that the finance
systems exchange.  You are working as part of the ABC's IT team and are tasked with implementing the functionality based
on logic explained below.
Encryption Logic: 
Encryption comprises of 3 actions in sequence 
1. Get the supplier's id and find its length and append it with Supplier id 
2. Perform the below transformations, 
    a. calculate the Hex code of every character in ASCII format, of the data to be exchanged 
    b. reverse it and 
    c. append it to the String constructed in Step 1
3. Note that every append operation adds the '­' character 
Let's see an example 
Let data to be exchanged be: Good Morning  
Step1  Supplier's Unique Identifier : 33 (provided in input) Length of the Supplier's Unique Identified : 2 (to be computed) 
Step2  Calculate Corresponding Hex Code of characters in ASCII format G: 47, o: 6F, o: 6F, d: 64, SPACE: 20, M: 4D, o: 6F, r: 72, n: 6E, i: 69, n: 6E, g: 67 
Step3  Final Encrypted String: 2-33-74-F6-F6-46-02-D4-F6-27-E6-96-E6-76
Decryption Logic: 
From encryption logic, it is easy to see how supplier id can be extracted from the encrypted string. 
Rest is reversing the steps done during encryption. See example output to get a better understanding of Decryption Logic. 
Input Format: 
First Line should contain E (for Encryption) or D (for Decryption) 
If first line character is E then 
    Second line should contain input string to be encrypted 
    Third line should contain Sender's unique identifier 
Else If First line character is D then 
    Second line should contain string to be decrypted
Output Format: 
If input character is E then 
    Print final encrypted string 
If input character is D then 
    Print Supplier's unique identifier on first line Print Decrypted string on second line
Sample Input and Output:
------------------------------------------------------------------------------------------------+
S No. |    Input                                    |   Output                                  |
------+---------------------------------------------+-------------------------------------------|
      |   E                                         |  2-45-84-56-C6-C6-F6-02-75-F6-27-C6-46    |
1     |   Hello World                               |                                           |
      |   45                                        |                                           |
------+---------------------------------------------+-------------------------------------------+
2     |   D                                         |  45                                       |
      |   2-45-84-56-C6-C6-F6-02-75-F6-27-C6-46     |  Hello World                              |
------+---------------------------------------------+-------------------------------------------+         
'''
m=input()
if(m=="E"):
    s=input()
    id=input()
    res=""
    res+=str(len(id))
    res+="-"
    res+=id
    for i in s:
        res+="-"
        temp=hex(ord(i)).lstrip("0x").upper()
        temp=temp[::-1]
        res+=temp
    print(res)


if(m=="D"):
    l=list(input().split("-"))
    id=l[1]
    res=""
    for i in range(2,len(l)):
        temp=l[i]
        temp=temp[::-1]
        res+=chr(int(temp,16))
    print(id)
    print(res)

