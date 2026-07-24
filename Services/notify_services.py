from datetime import datetime
from Models.data import NotificationDTO


class NotifyService:

    def __init__(self):
        self.history = []

    def send_notification(
        self,
        notification_type: str,
        destinataires: list[str],
        message: str
    ):

        notification = NotificationDTO(
            id_notif=len(self.history) + 1,
            type=notification_type,
            destinataires=destinataires,
            message=message,
            date_envoi=datetime.now()
        )

        self.history.append(notification)

        print("Notification envoyée")
        print(f"Type : {notification.type}")
        print(f"Destinataires : {notification.destinataires}")
        print(f"Message : {notification.message}")

        return notification

    def get_history(self):
        return self.history