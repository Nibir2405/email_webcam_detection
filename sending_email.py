import smtplib
import mimetypes
from email.message import EmailMessage

def send_email(image_path):
    EMAIL_ADDRESS = "navidulislam2002@gmail.com"
    PASSWORD = "umszkpohctfmcfvn"
    Receiver = "nibirislam56@gmail.com"
    email_message = EmailMessage()
    email_message["Subject"] = "New movement detected"
    email_message.set_content("Hey, We just saw a new movement in front of the laptop")

    with open(image_path, "rb") as file:
        img_data = file.read()
        mime_type, _ = mimetypes.guess_type(image_path)
        maintype, subtype = mime_type.split('/')
        email_message.add_attachment(img_data, maintype=maintype, subtype=subtype, filename=image_path)

    try:
        debuglevel = True
        mail = smtplib.SMTP("smtp.gmail.com", 587)  # Use port 587 for TLS
        mail.set_debuglevel(debuglevel)
        mail.starttls()
        mail.login(EMAIL_ADDRESS, PASSWORD)
        mail.sendmail(EMAIL_ADDRESS, Receiver, email_message.as_string())
        mail.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending the email: {e}")


if __name__ == "__main__":
    send_email(image_path="images/1.png")