from datetime import date
from enum import Enum, auto
from typing import List


# ==========================================
# ENUMERATIONS
# ==========================================

class StatutReservation(Enum):
    EN_ATTENTE = auto()
    CONFIRMEE = auto()
    ANNULEE = auto()


class ModePaiement(Enum):
    CARTE_BANCAIRE = auto()
    MOBILE_MONEY = auto()
    VIREMENT = auto()
    ESPECES = auto()


class TypeDocument(Enum):
    CONFIRMATION = auto()
    FACTURE = auto()


# ==========================================
# DTO
# ==========================================

class VoyageurDTO:

    def __init__(
        self,
        id_voyageur: int,
        nom: str,
        prenom: str,
        email: str,
        telephone: str,
    ):

        self.id_voyageur = id_voyageur
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone

        self.reservations: List["ReservationDTO"] = []


class OffreDTO:

    def __init__(
        self,
        id_offre: int,
        destination: str,
        description: str,
        prix: float,
        places_disponibles: int,
        date_depart: date,
        date_retour: date,
    ):

        self.id_offre = id_offre
        self.destination = destination
        self.description = description
        self.prix = prix
        self.places_disponibles = places_disponibles
        self.date_depart = date_depart
        self.date_retour = date_retour

        self.reservations: List["ReservationDTO"] = []


class ReservationDTO:

    def __init__(
        self,
        id_reservation: int,
        date_reservation: date,
        statut: StatutReservation,
        voyageur_id: int,
        offre_id: int,
    ):

        self.id_reservation = id_reservation
        self.date_reservation = date_reservation
        self.statut = statut

        self.voyageur_id = voyageur_id
        self.offre_id = offre_id

        self.paiement: "PaiementDTO | None" = None


class PaiementDTO:

    def __init__(
        self,
        id_paiement: int,
        montant: float,
        mode_paiement: ModePaiement,
        statut: str,
        reservation_id: int,
    ):

        self.id_paiement = id_paiement
        self.montant = montant
        self.mode_paiement = mode_paiement
        self.statut = statut
        self.reservation_id = reservation_id

        self.document: "DocumentDTO | None" = None


class DocumentDTO:

    def __init__(
        self,
        id_document: int,
        type_document: TypeDocument,
        date_generation: date,
        reservation_id: int,
    ):

        self.id_document = id_document
        self.type_document = type_document
        self.date_generation = date_generation
        self.reservation_id = reservation_id

     # Relations
        self.paiement = None
