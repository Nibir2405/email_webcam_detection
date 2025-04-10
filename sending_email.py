import smtplib
import imghdr
from email.message import EmailMessage

def send_email(image_path):
    EMAIL_ADDRESS = "navidulislam2002@gmail.com"
    PASSWORD = "umszkpohctfmcfvn"
    Receiver = "nibirislam56@gmail.com"
    email_message = EmailMessage()
    email_message["Subject"] = "New movement dectected"
    email_message.set_content("Hey, We just saw a new movement in front of the laptop")

    with open(image_path, "rb") as file:
        img_data = file.read()
        img_type = imghdr.what(None, img_data)
    email_message.add_attachment(img_data, maintype="image", subtype=img_type, filename=image_path)

    try :
        debuglevel = True
        mail = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        mail.set_debuglevel(debuglevel)
        mail.starttls()
        mail.login(EMAIL_ADDRESS, PASSWORD)
        mail.sendmail(EMAIL_ADDRESS, Receiver, email_message.as_string())
        mail.quit()
        print("Email sent successfully")
    except:
        print("Error sending the email")


if __name__=="__maim__":
    send_email(image_path="images\1.png")