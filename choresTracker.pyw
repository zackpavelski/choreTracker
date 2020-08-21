#python chore tracker
import datetime
from datetime import date
def main():
    import sys
    from datetime import date

    text = getResult()
    emails = ["zack88690@gmail.com", "kelspels1@gmail.com", "s8petesfnest@yahoo.com", "eli@edibleelegancebyeli.com"]
    week = getWeek()
    if datetime.date.today().weekday() == 0:
        sendEmailMultiple(week, text, emails)
        sys.exit()
    else:
        sys.exit()
def getWeek():
    from datetime import date
    import datetime
    import sys
    d1 = date(2020, 6, 16)
    d = datetime.date.today()
    day = d.day
    month = d.month
    year = d.year
    d2 = date(year, month, day)
    result = (d1-d2).days//7
    return result

def getResult():
    from datetime import date
    import datetime
    import sys
    d1 = date(2020, 6, 16)
    d = datetime.date.today()
    day = d.day
    month = d.month
    year = d.year
    d2 = date(year, month, day)
    result = (d1-d2).days//7
    chores = ["load.", "unload and trash."]
    
    if result%2 == 0: 
        #sendEmail(result, chores[0], "zack88690@gmail.com")
        #sendEmail(result, chores[1], "kelspels1@gmail.com")
        #Zack's chore is load
        #kelsey is trash and unload
        return "Kelsey's chore is to unload the dishwasher and take out the trash. Zack's chore is to load."
    else:
        return "Kelsey's chore is to load the dishwasher. Zack's chore is the unload and take out the trash."
        
def sendEmail(week, result, email):
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "zack88690@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "Tanjiro1!"
    message = """\
    Subject: Chores Assignment Week %s

    %s.""" %(week, result)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def sendEmailMultiple(week, result, emails):
    import smtplib, ssl
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "zack88690@gmail.com"
    for email in emails:
        receiver_email = email
        password = "Tanjiro1!"
        message = """\
        Subject: Chores Assignment Week %s

        %s.""" %(week, result)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

main()
