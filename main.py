from tkinter import *
from tkinter import messagebox
from datetime import date, time, datetime

from tkcalendar import Calendar

from dao import UserDAO, EventDAO
from data import EtudiantDTO, SeanceDTO, TypeSeance
from smtp_services import SMTPService


# =========================
# DAO
# =========================

user_dao = UserDAO()
event_dao = EventDAO()


# =========================
# EMAIL
# =========================

smtp_service = SMTPService(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email="VOTRE_EMAIL@gmail.com",
    password="VOTRE_MOT_DE_PASSE",
)


# =========================
# FENETRE
# =========================

root = Tk()

root.title("SmartCalendar PRO")
root.geometry("1200x950")
root.configure(bg="#1e1e2f")


# =========================
# TITRE
# =========================

titre = Label(
    root,
    text="SMART CALENDAR PRO",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="#00d4ff",
)

titre.pack(pady=10)


# =========================
# HEURE
# =========================

heure_label = Label(
    root,
    font=("Arial", 12, "bold"),
    bg="#1e1e2f",
    fg="green",
)

heure_label.pack()


def mettre_a_jour_heure():

    heure_actuelle = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    heure_label.config(
        text=f"Heure système : {heure_actuelle}"
    )

    root.after(1000, mettre_a_jour_heure)


mettre_a_jour_heure()


# =========================
# CALENDRIER
# =========================

cal = Calendar(
    root,
    selectmode="day",
    year=2026,
    month=5,
    day=20,
)

cal.pack(pady=15)


# =========================
# UTILISATEURS
# =========================

Label(
    root,
    text="Liste des utilisateurs",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white",
).pack()

frame_users = Frame(
    root,
    bg="#1e1e2f",
)

frame_users.pack()

scroll_users = Scrollbar(frame_users)

users_list = Listbox(
    frame_users,
    width=120,
    height=8,
    bg="#2b2b3c",
    fg="white",
    font=("Consolas", 11),
    yscrollcommand=scroll_users.set,
)

scroll_users.config(
    command=users_list.yview
)

users_list.pack(side=LEFT)

scroll_users.pack(
    side=RIGHT,
    fill=Y,
)


# =========================
# EVENEMENTS
# =========================

Label(
    root,
    text="Liste des événements",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white",
).pack(pady=10)

frame_events = Frame(
    root,
    bg="#1e1e2f",
)

frame_events.pack()

scroll_events = Scrollbar(frame_events)

events_list = Listbox(
    frame_events,
    width=120,
    height=10,
    bg="#2b2b3c",
    fg="white",
    font=("Consolas", 11),
    yscrollcommand=scroll_events.set,
)

scroll_events.config(
    command=events_list.yview
)

events_list.pack(side=LEFT)

scroll_events.pack(
    side=RIGHT,
    fill=Y,
)


# =========================
# STATUT
# =========================

status_label = Label(
    root,
    text="Système prêt",
    bd=1,
    relief=SUNKEN,
    anchor=W,
    bg="#111827",
    fg="white",
    font=("Arial", 10, "bold"),
)

status_label.pack(
    side=BOTTOM,
    fill=X,
)


# =========================
# ACTUALISER
# =========================

def actualiser_listes():

    users_list.delete(0, END)

    events_list.delete(0, END)

    for user in user_dao.afficher_users():

        users_list.insert(
            END,
            f"{user.nom} {user.prenom} - {user.email}",
        )

    for event in event_dao.afficher_events():

        events_list.insert(
            END,
            f"{event.salle} | "
            f"{event.date_seance} | "
            f"{event.heure_debut} - "
            f"{event.heure_fin}",
        )

    status_label.config(
        text=
        f"{len(user_dao.afficher_users())} utilisateurs | "
        f"{len(event_dao.afficher_events())} événements"
    )


# =========================
# AJOUT UTILISATEUR
# =========================

def ajouter_utilisateur():

    nom = entry_nom.get()

    prenom = entry_prenom.get()

    email = entry_email.get()

    if nom == "" or prenom == "" or email == "":

        messagebox.showerror(
            "Erreur",
            "Tous les champs sont obligatoires",
        )

        return

    if user_dao.rechercher_user(email):

        messagebox.showwarning(
            "Attention",
            "Utilisateur déjà existant",
        )

        return

    user = EtudiantDTO(
        id_etudiant=1,
        matricule=f"GI{len(user_dao.afficher_users())+1}",
        nom=nom,
        prenom=prenom,
        email=email,
        promotion_id=101,
    )

    user_dao.ajouter_user(user)

    actualiser_listes()

    entry_nom.delete(0, END)
    entry_prenom.delete(0, END)
    entry_email.delete(0, END)

    messagebox.showinfo(
        "Succès",
        "Utilisateur ajouté",
    )


# =========================
# SUPPRIMER UTILISATEUR
# =========================

def supprimer_utilisateur():

    selection = users_list.curselection()

    if not selection:

        messagebox.showwarning(
            "Attention",
            "Sélectionnez un utilisateur",
        )

        return

    index = selection[0]

    user = user_dao.afficher_users()[index]

    user_dao.supprimer_user(user.email)

    actualiser_listes()

    messagebox.showinfo(
        "Succès",
        "Utilisateur supprimé",
    )


# =========================
# AJOUT EVENEMENT
# =========================

def ajouter_evenement():

    salle = entry_salle.get()

    if salle == "":

        messagebox.showerror(
            "Erreur",
            "Salle obligatoire",
        )

        return

    seance = SeanceDTO(
        id_seance=len(
            event_dao.afficher_events()
        ) + 1,

        date_seance=date.today(),

        heure_debut=time(8, 0),

        heure_fin=time(10, 0),

        salle=salle,

        est_synchro=True,

        cours_id=101,

        type=TypeSeance.COURS_MAGISTRAL,
    )

    event_dao.ajouter_event(seance)

    actualiser_listes()

    entry_salle.delete(0, END)

    messagebox.showinfo(
        "Succès",
        "Evénement ajouté",
    )


# =========================
# SUPPRIMER EVENEMENT
# =========================

def supprimer_evenement():

    selection = events_list.curselection()

    if not selection:

        messagebox.showwarning(
            "Attention",
            "Sélectionnez un événement",
        )

        return

    index = selection[0]

    event_dao.supprimer_event(index)

    actualiser_listes()

    messagebox.showinfo(
        "Succès",
        "Evénement supprimé",
    )


# =========================
# AFFICHER TOUS
# =========================

def afficher_tous():

    actualiser_listes()


# =========================
# RECHERCHE DATE
# =========================

def rechercher_par_date():

    events_list.delete(0, END)

    date_selectionnee = cal.get_date()

    try:

        date_obj = datetime.strptime(
            date_selectionnee,
            "%m/%d/%y"
        )

        date_sql = date_obj.strftime(
            "%Y-%m-%d"
        )

    except:

        date_sql = str(date.today())

    events = event_dao.rechercher_par_date(
        date_sql
    )

    if len(events) == 0:

        messagebox.showwarning(
            "Aucun résultat",
            "Aucun événement trouvé",
        )

        return

    for event in events:

        events_list.insert(
            END,
            f"{event.salle} | "
            f"{event.date_seance} | "
            f"{event.heure_debut} - "
            f"{event.heure_fin}",
        )


# =========================
# RECHERCHE SALLE
# =========================

def rechercher_par_salle():

    salle = entry_recherche_salle.get()

    events_list.delete(0, END)

    events = event_dao.afficher_events()

    trouve = False

    for event in events:

        if event.salle.lower() == salle.lower():

            events_list.insert(
                END,
                f"{event.salle} | "
                f"{event.date_seance} | "
                f"{event.heure_debut} - "
                f"{event.heure_fin}",
            )

            trouve = True

    if not trouve:

        messagebox.showwarning(
            "Aucun résultat",
            "Aucun événement trouvé pour cette salle",
        )


# =========================
# FORM UTILISATEUR
# =========================

frame_user = Frame(
    root,
    bg="#1e1e2f",
)

frame_user.pack(pady=15)

Label(
    frame_user,
    text="Nom",
    bg="#1e1e2f",
    fg="white",
).grid(row=0, column=0)

entry_nom = Entry(frame_user)

entry_nom.grid(row=0, column=1)

Label(
    frame_user,
    text="Prénom",
    bg="#1e1e2f",
    fg="white",
).grid(row=1, column=0)

entry_prenom = Entry(frame_user)

entry_prenom.grid(row=1, column=1)

Label(
    frame_user,
    text="Email",
    bg="#1e1e2f",
    fg="white",
).grid(row=2, column=0)

entry_email = Entry(frame_user)

entry_email.grid(row=2, column=1)

Button(
    frame_user,
    text="Ajouter utilisateur",
    bg="#4CAF50",
    fg="white",
    command=ajouter_utilisateur,
).grid(row=3, column=0, pady=5)

Button(
    frame_user,
    text="Supprimer utilisateur",
    bg="#d9534f",
    fg="white",
    command=supprimer_utilisateur,
).grid(row=3, column=1, pady=5)


# =========================
# EXPORT TXT
# =========================

def exporter_evenements():

    with open(
        "planning.txt",
        "w",
        encoding="utf-8"
    ) as fichier:

        fichier.write(
            "===== SMARTCALENDAR PLANNING =====\n\n"
        )

        for event in event_dao.afficher_events():

            ligne = (
                f"Salle : {event.salle}\n"
                f"Date : {event.date_seance}\n"
                f"Heure : {event.heure_debut} - "
                f"{event.heure_fin}\n"
                f"----------------------------------\n"
            )

            fichier.write(ligne)

    messagebox.showinfo(
        "Export terminé",
        "Le fichier planning.txt a été créé",
    )


# =========================
# FORM EVENEMENT
# =========================

frame_event = Frame(
    root,
    bg="#1e1e2f",
)

frame_event.pack(pady=15)

Label(
    frame_event,
    text="Salle",
    bg="#1e1e2f",
    fg="white",
).grid(row=0, column=0)

entry_salle = Entry(frame_event)

entry_salle.grid(row=0, column=1)

Button(
    frame_event,
    text="Ajouter événement",
    bg="#0275d8",
    fg="white",
    command=ajouter_evenement,
).grid(row=1, column=0, pady=5)

Button(
    frame_event,
    text="Supprimer événement",
    bg="#d9534f",
    fg="white",
    command=supprimer_evenement,
).grid(row=1, column=1, pady=5)

Button(
    frame_event,
    text="Exporter planning",
    bg="#5bc0de",
    fg="white",
    command=exporter_evenements,
).grid(row=1, column=2, padx=5)


# =========================
# RECHERCHE EVENEMENTS
# =========================

frame_search_user = Frame(
    root,
    bg="#1e1e2f",
)

frame_search_user.pack(pady=10)

Label(
    frame_search_user,
    text="Salle",
    bg="#1e1e2f",
    fg="white",
).grid(row=0, column=0)

entry_recherche_salle = Entry(
    frame_search_user
)

entry_recherche_salle.grid(
    row=0,
    column=1,
)

Button(
    frame_search_user,
    text="Afficher tous",
    command=afficher_tous,
).grid(row=0, column=2)

Button(
    frame_search_user,
    text="Recherche date",
    bg="#f0ad4e",
    fg="white",
    command=rechercher_par_date,
).grid(row=0, column=3, padx=5)

Button(
    frame_search_user,
    text="Recherche salle",
    bg="#5cb85c",
    fg="white",
    command=rechercher_par_salle,
).grid(row=0, column=4, padx=5)


# =========================
# INITIALISATION
# =========================

actualiser_listes()


# =========================
# EXECUTION
# =========================

root.mainloop()