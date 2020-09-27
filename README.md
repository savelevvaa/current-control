# 🔍current-control
<img src="https://img.shields.io/badge/language%20-python-blue" alt="Python3 Language"> <img src="https://img.shields.io/badge/python-v3.8.3-blue" alt="version">   
This is a console application for checking the current situation in the country due to a coronavirus infection. Adapted for a specific site whose page the app parses to get information. Relevant to the * 04.09.2020

## functionality 
1. app making request to get a new info about covi
    - if info has been changed (since last logged request), it prints notification console
    - if there is nothing new, it trying to joke
2. prints last parsed info into console
3. sends e-mail
    - it sends e-mail if there is smth new 
    - it will warn you that there is nothing to send
4. prints all logged results of previous request (data.txt file)

## images
**navigation menu:**             
<img src="/images/0.jpg" width="50%">

**making request:**             
| _respond 1_                 | _respond 2_                 |
|:---------------------------:|:---------------------------:|
| <img src="/images/1_1.jpg"> | <img src="/images/1_2.jpg"> |
|           success           |   nothing new, stpd joke    |

**printing result of last request:**             
<img src="/images/2.jpg" width="50%">

**sending email:**             
| _respond 1_                 | _respond 2_                 |
|:---------------------------:|:---------------------------:|
| <img src="/images/3_1.jpg"> | <img src="/images/3_2.jpg"> |
|           success           |     nothing new to sent     |

**printing out hole data log:**             
<img src="/images/4.jpg" width="50%">

---
> P.S. this application is written exclusively for educational purposes, learning the Python language and applied use of popular packages.
