# import standard packages
from Tkinter import *
from ttk import *
# import internal packages
import ui.dialogbox as DialogBox
import lib.utilities as Utilities
import lib.multilanguage as MultiLanguage
import lib.datamanagement as DataManagement
from lib.candidate import Candidate
from lib.visit import Visit


# ref: http://effbot.org/tkinterbook/tkinter-newDialog-windows.htm
# TODO this class needs a major clean-up


class DataWindow(Toplevel):

    def __init__(self, parent, candidate=''):
        """
        Initialize the DataWindow class.

        :param parent: parent frame of the data window
         :type parent: object
        :param candidate: candidate ID or 'new' for a new candidate
         :type candidate: str

        """

        Toplevel.__init__(self, parent)

        # Create a transient window on top of parent window
        self.transient(parent)
        self.parent    = parent
        self.candidate = candidate
        #TODO find a better title for the data window
        self.title(MultiLanguage.data_window_title)
        body = Frame(self)

        # Draw the body of the data window
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        # Draw the button box of the data window
        self.button_box()

        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.close_dialog)
        Utilities.center_window(self)
        self.initial_focus.focus_set()
        self.wait_window(self)


    def body(self, master):
        """
        Creates the body of the 'data window'.

        :param master: frame in which to draw the body of the data window
         :type master: object

        """

        # Load the candidate and visitset data
        cand_info = []
        visitset  = []
        if not self.candidate == 'new':
            (cand_info, visitset) = self.load_data()

        ## Create a candidate section in the data window
        self.candidate_pane = Labelframe(
            self,
            text=MultiLanguage.candidate_pane,
            width=250,
            height=350,
            borderwidth=10
        )
        self.candidate_pane.pack(
            side=TOP, expand=YES, fill=BOTH, padx=5, pady=5
        )

        # Draw in the candidate section of the data window
        self.candidate_pane_ui(cand_info)

        # Draw the visit section if self.candidate is not 'new' or 'search'
        if not self.candidate == 'new':
            # Create a calendar section in the data window
            self.schedule_pane = Labelframe(
                self,
                text=MultiLanguage.schedule_pane,
                width=250,
                height=350,
                borderwidth=10
            )
            self.schedule_pane.pack(
                side=TOP, expand=YES, fill=BOTH, padx=5, pady=5
            )
            # Draw in the calendar section of the data window
            self.schedule_pane_ui(visitset)


    def candidate_pane_ui(self, cand_info):
        """
        Draws the candidate section of the datawindow and populates it fields
        based on what is store in cand_info

        :param cand_info: dictionary with the candidate's information
         :type cand_info: dict

        """

        # Initialize text variables that will contain the field values
        self.text_pscid_var     = StringVar()
        self.text_firstname_var = StringVar()
        self.text_lastname_var  = StringVar()
        self.text_dob_var       = StringVar()
        self.text_gender_var    = StringVar()
        self.text_status_var    = StringVar()
        self.text_phone_var     = StringVar()

        # If self.candidate is populated with a candID populate the fields with
        # values available in cand_info dictionary, otherwise populate with
        # empty str or " " in the case of drop down menus
        if self.candidate == 'new':
            self.text_pscid_var.set("")
            self.text_firstname_var.set("")
            self.text_lastname_var.set("")
            self.text_dob_var.set("")
            self.text_gender_var.set(" ")
            self.text_status_var.set(" ")
            self.text_phone_var.set("")
        else:
            self.text_pscid_var.set(cand_info["Identifier"])
            self.text_firstname_var.set(cand_info["FirstName"])
            self.text_lastname_var.set(cand_info["LastName"])
            self.text_dob_var.set(cand_info["DateOfBirth"])
            self.text_gender_var.set(cand_info["Gender"])
            self.text_status_var.set(cand_info["CandidateStatus"])
            self.text_phone_var.set(cand_info["PhoneNumber"])

        # Create widgets to be displayed
        # (typically a label with a text box underneath per variable to display)
        self.label_pscid = Label(     # identifier label
            self.candidate_pane, text=MultiLanguage.candidate_pscid
        )
        self.text_pscid  = Entry(     # identifier text box
            self.candidate_pane, textvariable=self.text_pscid_var
        )
        self.label_firstname = Label( # firstname label
            self.candidate_pane, text=MultiLanguage.candidate_firstname
        )
        self.text_firstname  = Entry( # firstname text box
            self.candidate_pane, textvariable=self.text_firstname_var
        )
        self.label_lastname = Label(  # lastname label
            self.candidate_pane, text=MultiLanguage.candidate_lastname
        )
        self.text_lastname  = Entry(  # lastname text box
            self.candidate_pane, textvariable=self.text_lastname_var
        )
        self.label_dob = Label(       # date of birth label
            self.candidate_pane, text=MultiLanguage.candidate_dob
        )
        self.text_dob  = Entry(       # date of birth text box
            self.candidate_pane, textvariable=self.text_dob_var
        )
        self.label_gender = Label(    # gender label
            self.candidate_pane, text=MultiLanguage.candidate_gender
        )
        self.text_gender  = Combobox( # gender selected from a drop down menu
            self.candidate_pane,
            textvariable=self.text_gender_var, # variable to store the selection
            values=MultiLanguage.gender_options # list of drop down options
        )
        self.label_status = Label(    # candidate status label
            self.candidate_pane, text=MultiLanguage.candidate_status
        )
        #TODO: grep the status_options list from the project information
        self.text_status  = Combobox( # cand. status selected from drop down
            self.candidate_pane,
            textvariable=self.text_status_var, # variable to store the selection
            values=MultiLanguage.candidate_status_options # list of options
        )
        self.label_phone = Label(     # phone number label
            self.candidate_pane, text=MultiLanguage.candidate_phone
        )
        self.text_phone  = Entry(     # phone number text box
            self.candidate_pane, textvariable=self.text_phone_var
        )

        # Change state of combobox to be readonly
        self.text_gender.config(state='readonly')
        self.text_status.config(state='readonly')

        # Draw widgets in the candidate pane section
        self.label_pscid.grid(     # draw identifier label
            column=0, row=0, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_pscid.grid(      # draw identifier text box
            column=0, row=1, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_firstname.grid( # draw firstname label
            column=1, row=0, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_firstname.grid( # draw firstname text box
            column=1, row=1, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_lastname.grid( # draw lastname label
            column=2, row=0, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_lastname.grid(  # draw lastname text box
            column=2, row=1, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_dob.grid(      # draw date of birth label
            column=3, row=0, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_dob.grid(       # draw date of birth text box
            column=3, row=1, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_gender.grid(   # draw gender label
            column=0, row=2, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_gender.grid(    # draw gender text box
            column=0, row=3, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_status.grid(   # draw candidate status label
            column=1, row=2, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_status.grid(    # draw candidate status text box
            column=1, row=3, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_phone.grid(    # draw phone number label
            column=2, row=2, padx=10, pady=5, sticky=N+S+E+W
        )
        self.text_phone.grid(     # draw phone number text box
            column=2, row=3, padx=10, pady=5, sticky=N+S+E+W
        )


    def schedule_pane_ui(self, visitset):

        # If the candidate has not visit set, display a message on the calendar
        # section to say that no visit has been scheduled yet for that candidate
        if not visitset:
            self.label_no_visit = Label(
                self.schedule_pane, text=MultiLanguage.schedule_no_visit_yet
            )
            self.label_no_visit.grid(
                row=0, column=1, columnspan=4, padx=5, sticky=N+S+E+W
            )
            return

        # Create top row (header) widgets
        self.label_visit_label = Label(     # create visit label widget
            self.schedule_pane, text=MultiLanguage.col_visitlabel
        )
        self.label_visit_date = Label(
            self.schedule_pane, text=MultiLanguage.col_visitdate
        )
        self.label_visit_startwhen = Label(      # create visit when widget
            self.schedule_pane, text=MultiLanguage.col_visitstartwhen
        )
        self.label_visit_endwhen = Label(
            self.schedule_pane, text=MultiLanguage.col_visitendwhen
        )
        self.label_visit_where = Label(     # create visit where widget
            self.schedule_pane, text=MultiLanguage.col_visitwhere
        )
        self.label_visit_withwhom = Label(  # create visit withwhom widget
            self.schedule_pane, text=MultiLanguage.col_visitwithwhom
        )
        self.label_visit_status = Label(    # create visit status widget
            self.schedule_pane, text=MultiLanguage.col_visitstatus
        )

        # Draw the top row (header) widgets
        self.label_visit_label.grid(        # draw visit label widget
            row=0, column=1, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_date.grid(
            row=0, column=2, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_startwhen.grid(         # draw visit when widget
            row=0, column=3, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_endwhen.grid(
            row=0, column=4, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_where.grid(        # draw visit where widget
            row=0, column=5, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_withwhom.grid(     # draw visit withwhom widget
            row=0, column=6, padx=10, pady=5, sticky=N+S+E+W
        )
        self.label_visit_status.grid(       # draw visit status widget
            row=0, column=7, padx=10, pady=5, sticky=N+S+E+W
        )

        # Sort visit list based on the VisitDate field
        visit_list = DataManagement.sort_candidate_visit_list(visitset)

        # Show values on ui
        row_nb = 0   # row number index
        # Define text variable arrays to be displayed at row_nb
        self.text_visit_label_var     = []
        self.text_visit_date_var      = []
        self.text_visit_startwhen_var = []
        self.text_visit_endwhen_var   = []
        self.text_visit_where_var     = []
        self.text_visit_status_var    = []
        self.text_visit_withwhom_var  = []
        # Define text widget arrays to be displayed at row_nb
        self.text_visit_date      = []
        self.text_visit_startwhen = []
        self.text_visit_endwhen   = []
        self.text_visit_where     = []
        self.text_visit_status    = []
        self.text_visit_withwhom  = []
        # Define button widget arrays to be displayed at row_nb
        self.button_visit_save   = []
        self.button_visit_edit   = []
        self.button_visit_delete = []
        self.button_visit_cancel = []

        # Loop through visits
        for visit in visit_list:

            # Check if values are set for VisitDate, VisitStartWhen, VisitWhere,
            # VisitWindow & VisitStatus keys. If not, set it to empty string as
            # we need a text to display in the corresponding label widgets.
            self.text_visit_label_var.append(StringVar())
            self.text_visit_label_var[row_nb].set(visit["VisitLabel"])
            self.text_visit_date_var.append(StringVar())
            self.text_visit_startwhen_var.append(StringVar())
            self.text_visit_endwhen_var.append(StringVar())
            self.text_visit_where_var.append(StringVar())
            self.text_visit_status_var.append(StringVar())
            self.text_visit_withwhom_var.append(StringVar())

            if "VisitDate" in visit.keys():
                #TODO: implement automatic range for next visit
                self.text_visit_date_var[row_nb].set(visit["VisitDate"])
            if "VisitStartWhen" in visit.keys():
                self.text_visit_startwhen_var[row_nb].set(
                    visit["VisitStartWhen"]
                )
            if "VisitEndWhen" in visit.keys():
                self.text_visit_endwhen_var[row_nb].set(visit["VisitEndWhen"])
            if "VisitWhere" in visit.keys():
                self.text_visit_where_var[row_nb].set(visit["VisitWhere"])
            if "VisitWithWhom" in visit.keys():
                self.text_visit_withwhom_var[row_nb].set(visit["VisitWithWhom"])
            if "VisitStatus" in visit.keys():
                self.text_visit_status_var[row_nb].set(visit["VisitStatus"])

            # Create the visit row widgets
            label_visit_label= Label(
                self.schedule_pane, text=self.text_visit_label_var[row_nb].get()
            )
            self.text_visit_date.append(      # visit date widget
                Entry(
                    self.schedule_pane,
                    textvariable=self.text_visit_date_var[row_nb]
                )
            )
            self.text_visit_startwhen.append( # visit start when widget
                Combobox(
                    self.schedule_pane,
                    textvariable=self.text_visit_startwhen_var[row_nb],
                    values=MultiLanguage.time_options,
                    width=9
                )
            )
            self.text_visit_endwhen.append(   # visit end when widget
                Combobox(
                    self.schedule_pane,
                    textvariable=self.text_visit_endwhen_var[row_nb],
                    values=MultiLanguage.time_options,
                    width=9
                )
            )
            self.text_visit_where.append(     # visit where widget
                Entry(
                    self.schedule_pane,
                    textvariable=self.text_visit_where_var[row_nb]
                )
            )
            self.text_visit_withwhom.append(  # visit with whom widget
                Entry(
                    self.schedule_pane,
                    text=self.text_visit_withwhom_var[row_nb]
                )
            )
            self.text_visit_status.append(    # visit status widget
                Combobox(
                    self.schedule_pane,
                    textvariable=self.text_visit_status_var[row_nb],
                    values=MultiLanguage.visit_status_options,
                    width=10
                )
            )
            # Disable edition of Entry widgets
            self.text_visit_date[row_nb].config(state=DISABLED)
            self.text_visit_startwhen[row_nb].config(state=DISABLED)
            self.text_visit_endwhen[row_nb].config(state=DISABLED)
            self.text_visit_where[row_nb].config(state=DISABLED)
            self.text_visit_status[row_nb].config(state=DISABLED)
            self.text_visit_withwhom[row_nb].config(state=DISABLED)

            # Create edit and save button widgets
            self.button_visit_edit.append(
                Button(
                    self.schedule_pane,
                    text="Edit",
                    width=5,
                    command=lambda row_nb=row_nb: self.set_row_to_edit_mode(
                        row_nb
                    )
                )
            )
            self.button_visit_save.append(
                Button(
                    self.schedule_pane,
                    text="Save",
                    width=5,
                    command=lambda row_nb=row_nb: self.visit_save_action(
                        row_nb
                    )
                )
            )
            self.button_visit_delete.append(
                Button(
                    self.schedule_pane,
                    text='Delete',
                    width=5,
                    command=lambda row_nb=row_nb: self.visit_delete_action(
                        row_nb
                    )
                )
            )
            self.button_visit_cancel.append(
                Button(
                    self.schedule_pane,
                    text='Cancel',
                    width=5,
                    command=lambda row_nb=row_nb: self.visit_cancel_action(
                        row_nb
                    )
                )
            )

            # Draw the visit row widget
            label_visit_label.grid(
                row=row_nb+1, column=1, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_date[row_nb].grid(
                row=row_nb+1, column=2, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_startwhen[row_nb].grid(
                row=row_nb+1, column=3, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_endwhen[row_nb].grid(
                row=row_nb+1, column=4, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_where[row_nb].grid(
                row=row_nb+1, column=5, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_withwhom[row_nb].grid(
                row=row_nb+1, column=6, padx=10, pady=5, sticky=N+S+E+W
            )
            self.text_visit_status[row_nb].grid(
                row=row_nb+1, column=7, padx=10, pady=5, sticky=N+S+E+W
            )
            self.button_visit_edit[row_nb].grid(
                row=row_nb+1, column=8, padx=5, pady=5, sticky=N+S+E+W
            )
            self.button_visit_save[row_nb].grid(
                row=row_nb+1, column=8, padx=5, pady=5, sticky=N+S+E+W
            )
            self.button_visit_delete[row_nb].grid(
                row=row_nb+1, column=9, padx=5, pady=5, sticky=N+S+E+W
            )
            self.button_visit_cancel[row_nb].grid(
                row=row_nb+1, column=9, padx=5, pady=5, sticky=N+S+E+W
            )
            # Display the edit and delete buttons on top
            self.button_visit_edit[row_nb].lift()
            self.button_visit_delete[row_nb].lift()
            # Hide the save and cancel button below the edit button
            self.button_visit_save[row_nb].lower()
            self.button_visit_cancel[row_nb].lower()

            # Increment row_nb for the next visit to be displayed
            row_nb += 1


    def load_data(self):
        """
        Read the XML data and return the candidate's (self.candidate)
        information as well as its visit information.

        :return cand_data:  data dictionary with candidate information
         :rtype cand_data:  dict
        :return visit_data: data dictionary with visit information
         :rtype visit_data: dict

        """

        try:
            # Read candidate information
            cand_data  = DataManagement.read_candidate_data()
            # Read visit information
            visit_data = DataManagement.read_visitset_data()
            visitset   = {}   # Create a visitset dictionary
            cand_info  = {}   # Create a candidate information dictionary

            # Loop through all candidates
            for cand_key in cand_data:
                # Grep candidate's information from cand_data dictionary
                if cand_data[cand_key]["Identifier"] == self.candidate:
                    cand_info = cand_data[cand_key]
                    break

            # Loop through candidates' visit data
            for cand_key in visit_data:
                # Grep candidate's visit set information from visit_data
                if visit_data[cand_key]["Identifier"] == self.candidate \
                        and 'VisitSet' in visit_data[cand_key]:
                    visitset = visit_data[cand_key]["VisitSet"]
                    break

        except Exception as e:
            print "datawindow.body ", str(e)  # TODO manage exceptions
            return

        return cand_info, visitset


    def button_box(self):
        """
        Draws the button box at the bottom of the data window.

        """

        # add standard button box
        box = Frame(self)

        # description_frame_gui buttons
        ok = Button(
            box, text="OK", width=10, command=self.ok_button, default=ACTIVE
        )
        cancel = Button(
            box, text="Cancel", width=10, command=self.cancel_button
        )

        # draw the buttons
        ok.pack(side=LEFT, padx=5, pady=5)
        cancel.pack(side=LEFT, padx=5, pady=5)

        # bind key handlers to button functions
        self.bind("<Return>", self.ok_button)
        self.bind("<Escape>", self.close_dialog)

        # draw the button box
        box.pack()


    def ok_button(self, event=None):
        """
        Event handler for the OK button. If something was missing in the data
        and it could not be saved, it will pop up an error message with the
        appropriate error message.

        :param event:
         :type event:

        :return:

        """

        message = self.capture_candidate_data()

        if message:
            parent = Frame(self)
            newwin = DialogBox.ErrorMessage(parent, message)
            if newwin.buttonvalue == 1:
                return # to stay on the candidate pop up page after clicking OK

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        #need to call treeview update here
        self.withdraw()
        self.close_dialog()


    def cancel_button(self, event=None):
        """
        Event handler for the cancel button. Will ask confirmation if want to
        cancel, if yes put focus back to the datatable without saving, else put
        focus back to the data window.

        :param event:
         :type event:

        :return:

        """

        parent = Frame(self)
        newwin = DialogBox.ConfirmYesNo(parent, MultiLanguage.dialog_close)
        if newwin.buttonvalue == 1:
            self.close_dialog()
        else:
            return


    def close_dialog(self, event=None):
        """
        Close dialog handler: will put focus back to the parent window.

        :param event:
        :return:

        """

        # put focus back to parent window before destroying the window
        self.parent.focus_set()
        self.destroy()


    def validate(self):
        return 1


    def capture_candidate_data(self):
        """
        Grep the information from the pop up window's text fields and save the
        candidate information based on the pscid.

        :param: None

        :return: None

        """

        # Initialize the candidate dictionary with new values
        cand_data = {}

        # Capture data from fields
        cand_data['Identifier']  = self.text_pscid.get()
        cand_data['FirstName']   = self.text_firstname.get()
        cand_data['LastName']    = self.text_lastname.get()
        cand_data['DateOfBirth'] = self.text_dob.get()
        cand_data['Gender']      = self.text_gender_var.get()
        cand_data['PhoneNumber'] = self.text_phone.get()
        cand_data['CandidateStatus'] = self.text_status_var.get()

        # Set CandidateStatus to space string if not defined in cand_data
        if not cand_data['CandidateStatus']:
            cand_data['CandidateStatus'] = " "

        # Set PhoneNumber to space string if not defined in cand_data
        if not cand_data['PhoneNumber']:
            cand_data['PhoneNumber']     = " "

        # Check fields format and required fields
        candidate = Candidate(cand_data)
        message   = candidate.check_candidate_data('scheduler', self.candidate)
        if message:
            return message

        # Save candidate data
        DataManagement.save_candidate_data(cand_data)


    def capture_visit_data(self, row_nb):

        # Initialize the visit dictionary with new values
        visit_data = {}

        # Capture data from fields
        visit_data['VisitLabel']    = self.text_visit_label_var[row_nb].get()
        visit_data['VisitDate']     = self.text_visit_date_var[row_nb].get()
        visit_data['VisitStartWhen']= self.text_visit_startwhen_var[row_nb].get()
        visit_data['VisitEndWhen']  = self.text_visit_endwhen_var[row_nb].get()
        visit_data['VisitWhere']    = self.text_visit_where_var[row_nb].get()
        visit_data['VisitStatus']   = self.text_visit_status_var[row_nb].get()
        visit_data['VisitWithWhom'] = self.text_visit_withwhom_var[row_nb].get()

        # Set VisitWithWhom to space string if not defined in visit_data
        if not visit_data['VisitWithWhom']:
            visit_data['VisitWithWhom'] = " "

        # Set VisitWhere to space if not defined in visit_data
        if not visit_data['VisitWhere']:
            visit_data['VisitWhere'] = " "

        # Set VisitDate to space if not defined in visit_data
        if not visit_data['VisitDate']:
            visit_data['VisitDate'] = " "

        # Set VisitStartWhen to space if not defined in visit_data
        if not visit_data['VisitStartWhen']:
            visit_data['VisitStartWhen'] = " "

        # Set VisitEndWhen to space if not defined in visit_data
        if not visit_data['VisitEndWhen']:
            visit_data['VisitEndWhen'] = " "

        # Check fields format and required fields
        visit   = Visit(visit_data)
        message = visit.check_visit_data(
            self.candidate, visit_data['VisitLabel']
        )
        if message:
            return message

        # Save visit data
        DataManagement.save_visit_data(self.candidate, visit_data)


    def visit_save_action(self, row_number):
        """
        Actions to be performed when clicking on the save visit button.
          - Capture and save the visit data.
          - Disable edition of all fields of the row
          - Move the edit button back on top of the save button

        :param row_number: number of the row to be saved
         :type row_number: int

        """

        # Capture and save data entered
        message = self.capture_visit_data(row_number)
        if message:
            parent = Frame(self)
            newwin = DialogBox.ErrorMessage(parent, message)
            if newwin.buttonvalue == 1:
                return # to keep the fields open for edition after clicking OK

        # Disable edition of row fields
        self.set_row_to_view_mode(row_number)


    def visit_delete_action(self, row_number):
        """
        Actions to be performed when hitting the delete button.

        :param row_number: number of the row to be deleted
         :type row_number: int

        """

        #TODO: show warning before deleting

        #TODO: delete visit
        pass


    def visit_cancel_action(self, row_number):
        """
        Actions to be performed when hitting the cancel button:
          - show a warning message
          - if confirmed cancellation, disable edition of row widgets
          - else, go back to edition of the row widgets

        :param row_number: number of the row to cancel edition
         :type row_number: int

        """

        #self.cancel_button()
        parent = Frame(self)
        newwin = DialogBox.ConfirmYesNo(parent, MultiLanguage.dialog_cancel)
        if newwin.buttonvalue == 1:
            self.set_row_to_view_mode(row_number)
        else:
            return


    def set_row_to_view_mode(self, row_number):
        """
        Sets the row to view mode (a.k.a. disable widgets for edition).

        :param row_number: number of the row to disable edition
         :type row_number: int

        """

        # Disable edition of row fields
        self.text_visit_date[row_number].config(state=DISABLED)
        self.text_visit_startwhen[row_number].config(state=DISABLED)
        self.text_visit_endwhen[row_number].config(state=DISABLED)
        self.text_visit_where[row_number].config(state=DISABLED)
        self.text_visit_status[row_number].config(state=DISABLED)
        self.text_visit_withwhom[row_number].config(state=DISABLED)
        self.button_visit_save[row_number].config(state=DISABLED)
        self.button_visit_edit[row_number].config(state=NORMAL)

        # Display the edit button on top
        self.button_visit_edit[row_number].lift()
        self.button_visit_delete[row_number].lift()
        # Hide the save button below the edit button
        self.button_visit_save[row_number].lower()
        self.button_visit_cancel[row_number].lower()


    def set_row_to_edit_mode(self, row_number):
        """
        Sets the row to edit mode (a.k.a. enable widgets for edition).

        :param row_number: number of the row to enable edition
         :type row_number: int

        """

        # Enable edition of row fields
        self.text_visit_date[row_number].config(state=NORMAL)
        self.text_visit_startwhen[row_number].config(state='readonly')
        self.text_visit_endwhen[row_number].config(state='readonly')
        self.text_visit_where[row_number].config(state=NORMAL)
        self.text_visit_status[row_number].config(state='readonly')
        self.text_visit_withwhom[row_number].config(state=NORMAL)
        self.button_visit_save[row_number].config(state=NORMAL)
        self.button_visit_edit[row_number].config(state=DISABLED)

        # Hide the edit button below the save button
        self.button_visit_edit[row_number].lower()
        self.button_visit_delete[row_number].lower()
        # Display the save button on top of the edit button
        self.button_visit_save[row_number].lift()
        self.button_visit_cancel[row_number].lift()