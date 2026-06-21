from datetime import datetime


class NotifyService:

    def envoyer_notification(
        self,
        destinataires,
        message
    ):

        print("========== NOTIFICATION ==========")

        for d in destinataires:
            print(f"Envoi à : {d}")

        print(message)

        print(
            f"Date : {datetime.now()}"
        )

        print("==================================")

    def notifier_modification(
        self,
        email,
        cours
    ):

        message = (
            f"Le cours {cours} a été modifié"
        )

        self.envoyer_notification(
            [email],
            message
        )