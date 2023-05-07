import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "chetanandmeher1282004@gmail.com"
    password = "hnfcbeooatsiwspx"

    receiver = "chetanandmeher1282004@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email("camechoo")