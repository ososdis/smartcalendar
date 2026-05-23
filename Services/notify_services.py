from datetime import datetime
from typing import List

from Models.data import UserDTO, SeanceDTO


class NotifyService:

    def __init__(self, smtp_service=None):
        self.smtp_service = smtp_service
        self.notifications: List[str] = []

    # ==========================================
    # NOTIFICATION SIMPLE (INTERNE)
    # ==========================================
    def notifier(self, message: str) -> None:
        timestamped = f"[{datetime.now()}] {message}"
        self.notifications.append(timestamped)

    # ==========================================
    # RAPPEL DE SEANCE
    # ==========================================
    def rappel_seance(self, user: UserDTO, seance: SeanceDTO) -> None:

        message = (
            f"Rappel: cours à {seance.salle} "
            f"de {seance.heure_debut} à {seance.heure_fin}"
        )

        self.notifier(message)

        # si smtp actif
        if self.smtp_service:
            self.smtp_service.send_email(
                destinataire=user.email,
                sujet="Rappel de séance",
                message=message
            )

    # ==========================================
    # ALERTE CONFLIT
    # ==========================================
    def alerte_conflit(self, message: str) -> None:

        self.notifier(f"CONFLIT: {message}")

    # ==========================================
    # HISTORIQUE NOTIFICATIONS
    # ==========================================
    def get_notifications(self) -> List[str]:

        return self.notifications