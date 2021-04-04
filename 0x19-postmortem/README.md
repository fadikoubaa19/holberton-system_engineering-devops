Project 19 - Postmortem

Incident Report : Ecommerce web site
Issue Summary

I was trying to make a log in page when im done , the E-mail blank was refusing to work with regex symboles 

07:22 p.m : created the log in page

08:03 p.m : i made a regex function

08:43 p.m : i set it with e-mail blank 

09:11 p.m : the e-mail blank refused to work

09:49 p.m : i solved it when i found a condition error in my function behind the regex symboles
Root cause and resolution

When i made the regex function , i forgot to add the all symboles inside the quoted the "@" and I didin"t close the quote so, that caused a probleme and a crash in the blank of E-mail .
