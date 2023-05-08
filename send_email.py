import smtplib, ssl


def send_email(message: object) -> object:
    host = "smtp.gmail.com"
    port = 465

    username = "mehercheta1282004@gmail.com"
    password = "jzaqbecnypfssuvl"

    receiver = "mehercheta1282004@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

