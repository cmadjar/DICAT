#import standard packages
#import internal packages
import datetime

import lib.utilities as utilities
import lib.multilanguage as MultiLanguage
import lib.datamanagement as DataManagement


class VisitSetup():
    """
    The VisitSetup() class is used to define a study (or project) in terms of sequence of visits and also serves as a
    base class for Visit(VisitSetup).  A study (or project) can have as many visits as required. There is no class for
    study as it is merely a simple dictionnary.

    Code example:  This study contains 3 visits.  Since V0 is the first visit, it doesn't have any values for
                   'previousvisit', 'visitwindow' and ' visitmargin'
                        study = {}
                        visit = visit.VisitSetup(1, 'V0')  #a uid (uuid1) is automatically generated
                        study[visit.uid] = visit           #VisitSetup.uid is a unique ID used as key
                        visit = visit.VisitSetup(2, 'V1', 'V0', 10, 2)
                        study[visit.uid] = visit
                        visit = visit.VisitSetup(3, 'V2', 'V1', 20, 10)
                        study[visit.uid] = visit

    This is the parent class of Visit(VisitSetup), furthermore Visit(VisitSetup) objects will be 'instanciated' from
    each instance of VisitSetup(object).
    Both VisitSetup(object) class and instances are used to create individual instances of Visit(VisitSetup)

    Attributes:
        uid:           A unique identifier using python's uuid1 method. Used as key to store and retrieve objects from
                       files and/or dictionaries.
        rank:          The rank of the visit in the sequence (int). Useful to sort the visits in order of occurrence.
        visitlabel:    The label of the visit (string) such as V1, V2 or anything else the user may come up with
        previousvisit: The visitlabel (string) of the visit occurring before this one. Used to plan this visit based on
                       the date of the previous visit. (default to None)
        visitwindow:   The number of days (int) between this visit and the previous visit.  (default to None)
        visitmargin:   The margin (in number of days (int)) that is an allowed deviation (a +/- few days ).  Basically,
                       this allow the 'calculation' of a date window when this visit should occur.  (default to None)
        mandatory:     Indicate if this visit is mandatory. Default to Yes
        actions:       A list of action points (or simply reminders) specific to that visit (i.e.'reserve room 101').
                       This is not implemented yet (default to None)
    """

    def __init__(self, rank, visitlabel, previousvisit = None, visitwindow = None, visitmargin = None, actions = None, uid=None):
        self.uid = utilities.generate_uid()
        self.rank = rank
        self.visitlabel = visitlabel
        self.previousvisit = previousvisit
        self.visitwindow = visitwindow
        self.visitmargin = visitmargin
        self.actions = actions  #not implemented yet!


class Visit():
    """

    """
    def __init__(self, visit_data):
        # Required fields in visit_data
        self.visitlabel  = visit_data['VisitLabel']
        self.visitstatus = visit_data['VisitStatus']

        # Optional fields
        if 'VisitWhen' in visit_data:
            self.visitwhen = visit_data['VisitWhen']
        else:
            self.visitwhen = " "
        if 'VisitWhere' in visit_data:
            self.visitwhere = visit_data['VisitWhere']
        else:
            self.visitwhere = " "
        if 'VisitWithWhom' in visit_data:
            self.visitwithwhom = visit_data['VisitWithWhom']
        else:
            self.visitwithwhom = " "


    def check_visit_data(self, candidate, visit=''):

        # Check that all required fields are set (a.k.a. visitlabel and status)
        # Error message is stored in MultiLanguage.dialog_missing_visit_info
        if not self.visitlabel or not self.visitstatus:
            return MultiLanguage.dialog_missing_visit_info

        #
        visits_array = DataManagement.grep_list_of_visit_labels(candidate)
        if visit == 'new' and self.visitlabel in visits_array:
            message = DataManagement.dialog_visitLabel_exists + candidate
            return message

        # Check date format and hour format
        #TODO: implement the date check and hour check

        # If we get there, it means all the data is good so no message needs to
        # be displayed. Return False so that no message is displayed.
        return False


    # TODO: move this visit_date_range function somewhere else?
    # def visit_date_range(self):
    #     #need to handle the case where a visit has no dates
    #     #this works but Exception handling seems to broad
    #     try:
    #         early_date = datetime.datetime.date(self.whenearliest)
    #         late_date = datetime.datetime.date(self.whenlatest)
    #         date_range = str(early_date), '<>', str(late_date)
    #     except Exception as e:
    #         #print e
    #         date_range = ""
    #     return date_range




