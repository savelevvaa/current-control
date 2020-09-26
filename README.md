# 🔍current-control
<img src="https://img.shields.io/badge/language%20-python-blue" alt="Python3 Language"> <img src="https://img.shields.io/badge/python-v3.8.3-blue" alt="version">   
This is a console application for checking the current situation in the country due to a coronavirus infection. Adapted for a specific site whose page the app parses to get information. Relevant to the * 04.09.2020

## functionality 
1. app making request to get a new info about covi
    1.1 if info has been changed (since last logged request), it prints notification console
    1.2 if there is nothing new, it trying to joke
2. prints last parsed info into console
3. sends e-mail
    3.1 it sends e-mail if there is smth new 
    3.2 it will warn you that there is nothing to send
4. prints all logged results of previous request (data.txt file)
