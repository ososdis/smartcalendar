import flet as ft


# =========================
# DONNEES UTILISATEUR
# =========================
from Models.data import UserDTO


# =========================
# APPLICATION PRINCIPALE
# =========================
def main(page: ft.Page):

    # -------------------------
    # CONFIGURATION PAGE
    # -------------------------
    page.title = "Smart Calendar"
    page.window_width = 1200
    page.window_height = 750
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F172A"

    utilisateur = UserDTO(
        id_user=1,
        role="Étudiant",
        email="",
        logedin=False
    )

    # =========================
    # CHAMPS DE CONNEXION
    # =========================
    champ_email = ft.TextField(
        label="Adresse email",
        width=350,
        border_radius=15,
        prefix_icon=ft.Icons.EMAIL,
        bgcolor="#1E293B",
        border_color="#334155",
        focused_border_color="#3B82F6",
        text_style=ft.TextStyle(
            color="white",
            size=15
        )
    )

    champ_password = ft.TextField(
        label="Mot de passe",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=15,
        prefix_icon=ft.Icons.LOCK,
        bgcolor="#1E293B",
        border_color="#334155",
        focused_border_color="#3B82F6",
        text_style=ft.TextStyle(
            color="white",
            size=15
        )
    )

    # =========================
    # MESSAGE
    # =========================
    texte_info = ft.Text(
        "",
        color="red",
        size=14
    )

    # =========================
    # FONCTION CONNEXION
    # =========================
    def connexion(e):

        if champ_email.value == "":
            texte_info.value = "Veuillez entrer votre email."
            page.update()
            return

        utilisateur.logedin = True
        utilisateur.email = champ_email.value

        afficher_dashboard()

    # =========================
    # DASHBOARD
    # =========================
    def afficher_dashboard():

        page.clean()

        # -------- APPBAR --------
        appbar = ft.AppBar(
            bgcolor="#111827",
            title=ft.Text(
                "SMART CALENDAR",
                weight=ft.FontWeight.BOLD,
                size=24
            ),

            actions=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.CircleAvatar(
                                content=ft.Text("B"),
                                bgcolor="#2563EB"
                            ),

                            ft.Text(
                                utilisateur.email,
                                size=15
                            )
                        ]
                    ),
                    margin=10
                ),

                ft.IconButton(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED
                ),

                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    icon_color="red",
                    on_click=deconnexion
                )
            ]
        )

        page.appbar = appbar

        # -------- CARDS --------
        card1 = creer_card(
            "Cours aujourd'hui",
            "4",
            ft.Icons.SCHOOL,
            "#2563EB"
        )

        card2 = creer_card(
            "Travaux pratiques",
            "2",
            ft.Icons.ENGINEERING,
            "#059669"
        )

        card3 = creer_card(
            "Examens",
            "1",
            ft.Icons.DESCRIPTION,
            "#DC2626"
        )

        card4 = creer_card(
            "Projets",
            "3",
            ft.Icons.COMPUTER,
            "#D97706"
        )

        # -------- CONTENU --------
        contenu = ft.Column(
            controls=[

                ft.Container(height=20),

                ft.Text(
                    "Bienvenue sur votre tableau de bord",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Text(
                    "Gestion intelligente des activités académiques",
                    size=16,
                    color="#94A3B8"
                ),

                ft.Container(height=25),

                ft.ResponsiveRow(
                    controls=[
                        card1,
                        card2,
                        card3,
                        card4
                    ]
                ),

                ft.Container(height=30),

                ft.Container(
                    bgcolor="#1E293B",
                    border_radius=20,
                    padding=25,

                    content=ft.Column(
                        controls=[

                            ft.Row(
                                controls=[
                                    ft.Icon(
                                        ft.Icons.CALENDAR_MONTH,
                                        size=30,
                                        color="#3B82F6"
                                    ),

                                    ft.Text(
                                        "Planning de la semaine",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="white"
                                    )
                                ]
                            ),

                            ft.Divider(color="#334155"),

                            creer_tache(
                                "Maintenance industrielle",
                                "08:00 - 10:00",
                                "#2563EB"
                            ),

                            creer_tache(
                                "Automatique industrielle",
                                "10:30 - 12:30",
                                "#059669"
                            ),

                            creer_tache(
                                "TP Électrotechnique",
                                "14:00 - 17:00",
                                "#D97706"
                            )
                        ]
                    )
                )
            ],

            scroll=ft.ScrollMode.AUTO
        )

        page.add(
            ft.Container(
                content=contenu,
                padding=30,
                expand=True
            )
        )

        page.update()

    # =========================
    # DECONNEXION
    # =========================
    def deconnexion(e):

        utilisateur.logedin = False
        page.clean()
        page.appbar = None
        afficher_login()

    # =========================
    # CARD STATISTIQUE
    # =========================
    def creer_card(titre, valeur, icone, couleur):

        return ft.Container(
            col={"sm": 6, "md": 3},

            content=ft.Card(
                elevation=10,

                content=ft.Container(
                    bgcolor="#1E293B",
                    border_radius=20,
                    padding=20,

                    content=ft.Column(
                        controls=[

                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[

                                    ft.Icon(
                                        icone,
                                        size=40,
                                        color=couleur
                                    ),

                                    ft.Text(
                                        valeur,
                                        size=36,
                                        weight=ft.FontWeight.BOLD,
                                        color="white"
                                    )
                                ]
                            ),

                            ft.Text(
                                titre,
                                size=16,
                                color="#CBD5E1"
                            )
                        ]
                    )
                )
            )
        )

    # =========================
    # LIGNE ACTIVITE
    # =========================
    def creer_tache(cours, heure, couleur):

        return ft.Container(
            margin=10,
            padding=15,
            border_radius=15,
            bgcolor="#0F172A",

            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Row(
                        controls=[

                            ft.Container(
                                width=12,
                                height=50,
                                bgcolor=couleur,
                                border_radius=10
                            ),

                            ft.Column(
                                controls=[

                                    ft.Text(
                                        cours,
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color="white"
                                    ),

                                    ft.Text(
                                        heure,
                                        color="#94A3B8"
                                    )
                                ]
                            )
                        ]
                    ),

                    ft.Icon(
                        ft.Icons.CHEVRON_RIGHT,
                        color="#94A3B8"
                    )
                ]
            )
        )

    # =========================
    # INTERFACE LOGIN
    # =========================
    def afficher_login():

        page.clean()

        logo = ft.Container(
            width=120,
            height=120,
            border_radius=60,
            bgcolor="#2563EB",

            content=ft.Icon(
                ft.Icons.CALENDAR_MONTH,
                size=60,
                color="white"
            ),

            alignment=ft.Alignment(0, 0)
        )

        login_card = ft.Container(
            width=450,
            padding=40,
            border_radius=30,
            bgcolor="#111827",

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color="#000000"
            ),

            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[

                    logo,

                    ft.Container(height=20),

                    ft.Text(
                        "SMART CALENDAR",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "Plateforme intelligente de gestion académique",
                        size=15,
                        color="#94A3B8"
                    ),

                    ft.Container(height=25),

                    champ_email,

                    champ_password,

                    texte_info,

                    ft.Container(height=10),

                    ft.ElevatedButton(
                        "SE CONNECTER",
                        width=350,
                        height=50,

                        style=ft.ButtonStyle(
                            bgcolor="#2563EB",
                            color="white",
                            shape=ft.RoundedRectangleBorder(
                                radius=15
                            )
                        ),

                        on_click=connexion
                    )
                ]
            )
        )

        page.add(
            ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[
                    login_card
                ]
            )
        )

        page.update()

    # =========================
    # DEMARRAGE
    # =========================
    afficher_login()


# =========================
# EXECUTION
# =========================
ft.app(target=main)