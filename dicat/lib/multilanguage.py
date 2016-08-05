#!/usr/bin/env python
# -*- coding: utf-8 -*-

#read language preference from appdata file
#from utilities import readappdata  #TODO replace and remove
#language = readappdata()[0]

language = "en" #TODO make dynamic

if language == "fr":
    ######################  TOP LEVEL MENU BAR  ######################
    app_title = u"Outils LORIS"
    #APPLICATION menu
    application_menu    = u"Application"
    application_setting = u"Préferences"
    application_quit    = u"Quitter"
    #PROJECT menu
    #menuproject   = u"Projet"    #TODO remove?
    #openproject   = u"Ouvrir un projet"
    #modifyproject = u"Modifier le projet ouvert"
    #newproject    = u"Créer un nouveau projet"
    #CANDIDATE menu
    candidate_menu   = u"Candidat"
    candidate_update = u"Mettre à jour"
    candidate_get_id = u"Obtenir l'identifiant d'un candidat"
    candidate_exclude_include_toggle = u"Inclure/Exclure un candidat"
    #clear_all_field = u"Effacer"
    #ANONYMIZER menu
    anonymizer_menu = u"DICOM"
    anonymizer_run  = u"Anonymizer"
    #CALENDAR menu
    calendar_menu = u"Calendrier"
    calendar_new_appointment = u"Nouveau Rendez-vous"
    #HELP menu
    help_menu     = u"Aide"
    help_get_help = u"Obtenir de l'aide"
    help_about_window = u"A propos de ..."
    ######################### BUTTON BOXES ###########################
    candidate_add = u"Nouveau candidat"
    search    = u"Rechercher"
    visit_add = u"Nouvelle visite"
    ######################  PROJECT INFO PANE  #######################
    project_info_pane   = u"Projet"
    project_detail_pane = u"Détails du Projet"
    visit_detail_pane   = u"Détails des Visites"
    target_recruitment  = u"Cible de recrutement"
    current_recruitment = u"Recrutement actuel"
    project_name  = u"Projet"
    project_start = u"Début"
    project_end   = u"Fin"
    total_visit   = u"Nombre de Visites"
    ####################  MULTI-TAB DATA SECTION  #####################
    calendar_pane  = u"Calendrier"
    candidate_pane = u"Candidats"

    datatable_id    = u"ID"
    datatable_dob   = u"Date de Naissance"
    datatable_phone = u"Téléphone"
    datatable_city  = u"Ville"
    datatable_firstname   = u"Prénom"
    datatable_lastname    = u"Nom de famille"
    datatable_address     = u"Adresse"
    datatable_province    = u"Province"
    datatable_country     = u"Pays"
    datatable_postal_code = u"Code Postal"
    label_candidate_table = u"Faites un double-clic sur l'une des lignes " \
                            u"pour remplir les champs ci-dessus"

    calendar_monday    = u"Lundi"
    calendar_tuesday   = u"Mardi"
    calendar_wednesday = u"Mercredi"
    calendar_thursday  = u"Jeudi"
    calendar_friday    = u"Vendredi"
    calendar_saturday  = u"Samedi"
    calendar_sunday    = u"Dimanche"
    calendar_january   = u"Janvier"
    calendar_february  = u"Février"
    calendar_march     = u"Mars"
    calendar_april     = u"Avril"
    calendar_may       = u"Mai"
    calendar_june      = u"Juin"
    calendar_jully     = u"Juillet"
    calendar_august    = u"Août"
    calendar_september = u"Septembre"
    calendar_october   = u"Octobre"
    calendar_november  = u"Novembre"
    calendar_december  = u"Décembre"

    ################  COLUMN HEADER  ##################
    col_candidate  = u"Candidat"
    col_visitlabel = u"Visite"
    col_visitdate  = u"Date (AAAA-MM-JJ)"
    col_visitwhere = u"Endroit"
    col_visitwithwhom  = u"Avec qui"
    col_visitstartwhen = u"De"
    col_visitendwhen   = u"À"
    col_visitstatus    = u"Status"

    ####################  STATUS  #####################
    status_active    = u"actif"
    status_tentative = u"provisoire"
    #################  DATA WINDOWS  ##################
    data_window_title = u"DATA WINDOW" #TODO trouver un titre français
    ##################  DIALOGBOX  ####################
    # very not sure what to do about that section
    dialog_yes   = u"Oui"
    dialog_no    = u"Non"
    dialog_ok    = u"OK"
    dialog_close = u"Vous êtes sur le point de fermer cette fenêtre sans " \
                   u"sauvegarder!\n\nVoulez-vous continuer?"
    dialog_title_confirm   = u"Veuillez confirmer!"
    dialog_title_error     = u"Erreur"
    dialog_bad_dob_format  = u"La date de naissance doit être formattée en " \
                             u"AAAA-MM-JJ!"
    dialog_bad_date_format = u"La date doit être formattée en AAAA-MM-JJ!"
    dialog_no_data_entered = u"Au moins un des champs doit être entré pour " \
                             u"chercher un candidat."
    warning_filters_set    = u"ATTENTION: des filtres sont en fonction. " \
                             u"Seuls les candidats correspondant aux filtres " \
                             u"sont montrés"
    dialog_candID_already_exists  = u"L'identifiant existe déjà!"
    dialog_missing_cand_info_schedul = u"Les champs 'Identifiant', 'Prénom', " \
                                       u"'Nom de famille', 'Sexe' et "         \
                                       u"'Date de naissance' sont requis!"
    dialog_missing_cand_info_IDmapper = u"Les champs 'Identifiant', "  \
                                        u"'Prénom', 'Nom de famille' " \
                                        u"et 'Date de naissance' sont requis!"
    dialog_missing_visit_info = u"'Le 'nom' et le 'Status' de la visite sont "\
                                u"requis!'"
    dialog_cancel = u"Vous êtes sur le point d'annuler l'édition des données " \
                    u"sans sauver!\n\nVoulez-vous continuer?"
    dialog_delete = u"Vous êtes sur le point de suprimer la visite!\n\n" \
                    u"Voulez-vous continuer?"
    ################  DATA WINDOW  ###################
    schedule_pane    = u"Calendrier"
    candidate_pane   = u"Candidat"
    candidate_dob    = u"Date de naissance (AAAA-MM-JJ)"
    candidate_phone  = u"Téléphone"
    candidate_pscid  = u"ID"
    candidate_status = u"Status"
    candidate_gender = u"Sexe"
    candidate_firstname = u"Prénom"
    candidate_lastname  = u"Nom de famille"

    schedule_visit_label  = u"Visite"
    schedule_visit_rank   = u"#"
    schedule_visit_status = u"Status"
    schedule_visit_when   = u"Date"
    schedule_optional     = u"Optionnel"
    schedule_no_visit_yet = u"Aucune visite de programmé pour ce candidat"

    ############### DROP DOWN OPTIONS #################
    time_options = [
        "05:00", "05:15", "05:30", "05:45",
        "06:00", "06:15", "06:30", "06:45",
        "07:00", "07:15", "07:30", "07:45",
        "08:00", "08:15", "08:30", "08:45",
        "09:00", "09:15", "09:30", "09:45",
        "10:00", "10:15", "10:30", "10:45",
        "11:00", "11:15", "11:30", "11:45",
        "12:00", "12:15", "12:30", "12:45",
        "13:00", "13:15", "13:30", "13:45",
        "14:00", "14:15", "14:30", "14:45",
        "15:00", "15:15", "15:30", "15:45",
        "16:00", "16:15", "16:30", "16:45",
        "17:00", "17:15", "17:30", "17:45",
        "18:00", "18:15", "18:30", "18:45",
        "19:00", "19:15", "19:30", "19:45",
        "20:00", "20:15", "20:30", "20:45",
        "21:00", "21:15", "21:30", "21:45",
        "22:00", "22:15", "22:30", "22:45"
    ]

    visit_status_options = [
        ' ', 'scheduled', 'confirmed', 'to schedule', 'completed', 'cancelled'
    ]

    gender_options = [' ', 'Homme', 'Femme']

    candidate_status_options = [
        ' ',     'actif',      'retiré', 'exclus',
        'décés', 'ineligible', 'terminé'
    ]

elif language == "en":
    app_title = u"LORIS tools"
    #APPLICATION menu
    application_menu    = u"Application"
    application_setting = u"Preferences"
    application_quit    = u"Quit"
    #PROJECT menu
    #menuproject   = u"Project"   #TODO remove?
    #openproject   = u"Open project"
    #modifyproject = u"Modify open project"
    #newproject    = u"New project"
    #CANDIDATE menu
    candidate_menu   = u"Candidate"
    candidate_update = u"Update"
    candidate_get_id = u"Get a canditate ID"
    candidate_exclude_include_toggle = u"Include/Exclude a candidate"
    #clear_all_field = u"Clear"
    #CALENDAR menu
    calendar_menu = u"Calendar"
    calendar_new_appointment = u"New appointment"
    #ANONYMIZER menu
    anonymizer_menu = u"DICOM"
    anonymizer_run  = u"Anonymizer"
    #HELP menu
    help_menu     = u"Help"
    help_get_help = u"Get some help"
    help_about_window = u"About this..."
    #########################  BUTTON BOXES  #########################
    candidate_add = u"New candidate"
    search    = u"Search:"
    visit_add = u"New visit"
    ######################  PROJECT INFO PANE  #######################
    project_info_pane   = u"Project Information"
    project_detail_pane = u"Project Details"
    visit_detail_pane   = u"Visit Details"
    target_recruitment  = u"Recruitment target"
    current_recruitment = u"Current recruitment"
    project_name  = u"Project"
    project_start = u"Start"
    project_end   = u"End"
    total_visit   = u"Total number of Visits"
    ####################  MULTI-TAB DATA SECTION  #####################
    calendar_pane   = u"Calendar"
    candidate_pane  = u"Candidates"
    datatable_id    = u"ID"
    datatable_dob   = u"Date of Birth"
    datatable_phone = u"Phone"
    datatable_city  = u"City"
    datatable_address  = u"Address"
    datatable_province = u"Province"
    datatable_country  = u"Country"
    datatable_firstname   = u"First Name"
    datatable_lastname    = u"Last Name"
    label_candidate_table = u"Double click on row to populate fields above"
    datatable_postal_code = u"Postal Code"

    calendar_monday    = u"Monday"
    calendar_tuesday   = u"Tuesday"
    calendar_wednesday = u"Wednesday"
    calendar_thursday  = u"Thursday"
    calendar_friday    = u"Friday"
    calendar_saturday  = u"Saturday"
    calendar_sunday    = u"Sunday"
    calendar_january   = u"January"
    calendar_february  = u"February"
    calendar_march     = u"Marc"
    calendar_april     = u"April"
    calendar_may       = u"May"
    calendar_june      = u"June"
    calendar_jully     = u"Jully"
    calendar_august    = u"August"
    calendar_september = u"September"
    calendar_october   = u"October"
    calendar_november  = u"November"
    calendar_december  = u"December"

    ################  COLUMN HEADER  ##################
    col_candidate  = u"Candidate"
    col_visitlabel = u"Visit"
    col_visitdate  = u"Date (YYYY-MM-DD)"
    col_visitwhere = u"Visit location"
    col_visitwithwhom  = u"With whom"
    col_visitstartwhen = u"From"
    col_visitendwhen   = u"To"
    col_visitstatus    = u"Visit status"

    ####################  STATUS  #####################
    status_active    = u"active"
    status_tentative = u"tentative"

    #################  DATA WINDOWS  ##################
    data_window_title = u"Data Window"

    ##################  DIALOGBOX  ####################
    # very not sure what to do about that section
    dialog_yes   = u"Yes"
    dialog_no    = u"No"
    dialog_ok    = u"OK"
    dialog_close = u"You are about to close this window without saving!\n\n" \
                   u"Do you want to continue?"
    dialog_title_confirm   = u"Please confirm!"
    dialog_title_error     = u"Error"
    dialog_bad_dob_format  = u"Date of Birth should be in YYYY-MM-DD format!"
    dialog_bad_date_format = u"Date should be in YYYY-MM-DD format!"
    dialog_no_data_entered = u"At least one of the fields needs to be entered " \
                             u"to search_event a candidate."
    warning_filters_set    = u"WARNING: filters are set. Only matching " \
                             u"candidates are shown."
    dialog_candID_already_exists  = u"Identifier already exists!"
    dialog_missing_cand_info_schedul = u"'Identifier', 'Firstname', "         \
                                       u"'Lastname', 'Date of Birth' and " \
                                       u"'Gender' fields are required!"
    dialog_missing_cand_info_IDmapper = u"'Identifier', 'Firstname', "     \
                                        u"'Lastname' and 'Date of Birth' " \
                                        u"fields are required!"
    dialog_missing_visit_info = u"'Visit label and Visit status are required!'"
    dialog_visitLabel_exists  = u"Visit label already exists for this candidate"
    dialog_cancel = u"You are about to cancel edition without saving!\n\n" \
                    u"Do you want to continue?"
    dialog_delete = u"You are about to delete the visit!\n\n Do you want to " \
                    u"continue?"

    ################  DATA WINDOW  ###################
    schedule_pane    = u"Calendar"
    candidate_pane   = u"Candidate"
    candidate_dob    = u"Date of Birth (YYYY-MM-DD)"
    candidate_phone  = u"Phone"
    candidate_pscid  = u"ID"
    candidate_status = u"Status"
    candidate_gender = u"Sex"
    candidate_firstname   = u"Firstname"
    candidate_lastname    = u"Lastname"
    schedule_visit_label  = u"Visit"
    schedule_visit_rank   = u"#"
    schedule_visit_status = u"Status"
    schedule_visit_when   = u"Date"
    schedule_optional     = u"Optional"
    schedule_no_visit_yet = u"No visit scheduled for that candidate yet"

    ############### DROP DOWN OPTIONS #################
    time_options = [
        "05:00 AM", "05:15 AM", "05:30 AM", "05:45 AM",
        "06:00 AM", "06:15 AM", "06:30 AM", "06:45 AM",
        "07:00 AM", "07:15 AM", "07:30 AM", "07:45 AM",
        "08:00 AM", "08:15 AM", "08:30 AM", "08:45 AM",
        "09:00 AM", "09:15 AM", "09:30 AM", "09:45 AM",
        "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM",
        "11:00 AM", "11:15 AM", "11:30 AM", "11:45 AM",
        "12:00 AM", "12:15 AM", "12:30 AM", "12:45 AM",
        "01:00 PM", "01:15 PM", "01:30 PM", "01:45 PM",
        "02:00 PM", "02:15 PM", "02:30 PM", "02:45 PM",
        "03:00 PM", "03:15 PM", "03:30 PM", "03:45 PM",
        "04:00 PM", "04:15 PM", "04:30 PM", "04:45 PM",
        "05:00 PM", "05:15 PM", "05:30 PM", "05:45 PM",
        "06:00 PM", "06:15 PM", "06:30 PM", "06:45 PM",
        "07:00 PM", "07:15 PM", "07:30 PM", "07:45 PM",
        "08:00 PM", "08:15 PM", "08:30 PM", "08:45 PM",
        "09:00 PM", "09:15 PM", "09:30 PM", "09:45 PM",
        "10:00 PM", "10:15 PM", "10:30 PM", "10:45 PM"
    ]

    visit_status_options = [
        ' ', 'scheduled', 'confirmed', 'to schedule', 'completed', 'cancelled'
    ]

    gender_options = [' ', 'Male', 'Female']

    candidate_status_options = [
        ' ',     'active',     'withdrawn', 'excluded',
        'death', 'ineligible', 'completed'
    ]