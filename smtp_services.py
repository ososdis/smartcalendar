import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# =========================
# SERVICE SMTP
# =========================

class SMTPService:

    def __init__(
        self,
        smtp_server,
        smtp_port,
        email,
        password,
    ):

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password


    # =========================
    # ENVOI EMAIL
    # =========================

    def envoyer_email(
        self,
        destinataire,
        sujet,
        message,
    ):

        try:

            # =========================
            # CREATION MESSAGE
            # =========================

            msg = MIMEMultipart()

            msg["From"] = self.email
            msg["To"] = destinataire
            msg["Subject"] = sujet

            msg.attach(
                MIMEText(
                    message,
                    "plain"
                )
            )

            # =========================
            # CONNEXION SERVEUR SMTP
            # =========================

            serveur = smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
            )

            serveur.starttls()

            # =========================
            # AUTHENTIFICATION
            # =========================

            serveur.login(
                self.email,
                self.password,
            )

            # =========================
            # ENVOI MESSAGE
            # =========================

            serveur.send_message(msg)

            # =========================
            # FERMETURE
            # =========================

            serveur.quit()

            print(
                "Email envoyé avec succès"
            )

            return True

        except Exception as e:

            print(
                "Erreur email :",
                e
            )

            return False