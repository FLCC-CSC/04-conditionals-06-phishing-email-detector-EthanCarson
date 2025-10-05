# FILE NAME - phishing_email_detector.py

# NAME: Ethan Carson
# DATE: 10/5/2025
# BRIEF DESCRIPTION:  This program will alert the user if their email input could be a scam, via checking for certain strings within the input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

email = input('Enter the email subject line: ')
# Okay, yes. I did some research to use 'or' here, as I didn't want to have to basically double the line count per check. Very intuitive, Python, btw (JS )
if "urgent" in email.lower() or "immediate action required" in email.lower():
    test_result = 'HIGH RISK: Possible phishing attempt.'
elif "win" in email.lower() or "free" in email.lower():
    test_result = 'MEDIUM RISK: Suspicious offer detected.'
elif "password reset" in email.lower():
    test_result = 'LOW RISK: Verify legitimacy with sender.'
else: test_result = "No phishing indicators detected."
print(f'\nSECURITY ASSESSMENT:\n{test_result}\n------------------------\nAnalyzed subject: "{email}"')








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural?

It was very natural and intuitive, especially after coming from JS. the code I wrote looks very close to human speech.





'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[X] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[X] I'm solid. Totally got it.

'''
