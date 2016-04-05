import lib.datamanagement as DataManagement
import candidate
import visit

# Create a new database
#TODO: create functions to create a new database
database = "test_database.db"
#DataManagement.create_new_database(database)

# Create list of Projects for the study
#TODO: create functions to build projects (will be part of the project pane)
project_info = [ (1, "Project1", 100),
                 (2, "Project2", 150),
                 (3, "Project3", 50),
               ]
#DataManagement.save_project_data(database, project_info)


# Create list of Visit windows
#TODO: create functions to build visit windows for projects (in project pane)
visit_windows_info = [ (1, "V0", 1, None, None),
                       (1, "V1", 2, 50,   100 ),
                       (1, "V2", 3, 50,   100 ),
                       (2, "V0", 1, 100,  200 ),
                       (2, "V1", 2, 100,  200)
                     ]
#DataManagement.save_visit_windows_data(database, visit_windows_info)

#Create list of Candidates and save it
#TODO: create function to create or modify candidate (candidate.Candidate function)
#TODO: have option to enter multiple phone numbers
cand1 = candidate.Candidate('Billy',  'Roberts',   '451-784-9856', otherphone='514-874-9658')
cand2 = candidate.Candidate('Sue',    'Allen',     '451-874-9632', 'Elizabeth', None, "Active", "MTL0002")
cand3 = candidate.Candidate('Alan',   'Parson',    '451-874-8965', None,        None, "Excluded")
cand4 = candidate.Candidate('Pierre', 'Tremblay',  '547-852-9745', 'Dartagnan')
cand5 = candidate.Candidate('Alain',  'Jeanson',   '245-874-6321')
cand6 = candidate.Candidate('Marc',   'St-Pierre', '412-897-9874')
candidate_info = [ ( 'MTL0001',       '123456',         cand1.status,
                     cand1.firstname, cand1.middlename, cand1.lastname,
                     cand1.phone
                   ),
                   ( cand2.pscid,     '234567',         cand2.status,
                     cand2.firstname, cand2.middlename, cand2.lastname,
                     cand2.phone
                   ),
                   ( "MTL0003",       '345678',         cand3.status,
                     cand3.firstname, cand3.middlename, cand3.lastname,
                     cand3.phone
                   ),
                   ( "MTL0004",       '456789',         cand4.status,
                     cand4.firstname, cand4.middlename, cand4.lastname,
                     cand4.phone
                   ),
                   ( "MTL0005",       '567891',         cand5.status,
                     cand5.firstname, cand5.middlename, cand5.lastname,
                     cand5.phone
                   )
                 ]
#DataManagement.save_candidate_data(database, candidate_info)

# Create one candidate at a time (mimics behavior of the application)
cand6_info = ("MTL0006",       '678912',         cand6.status,
              cand6.firstname, cand6.middlename, cand6.lastname,
              cand6.phone
             )
#DataManagement.save_candidate_data(database, cand6_info)

# Get all entries of the candidate table
#TODO: grep for all occurence of DataManagement.read_candidate_data() and replace by this way of selecting all candidates
#TODO: read the candidate_list, new function in candidate maybe? or datamanagement (is this needed?)
candidates_list = DataManagement.database_selectall_table(database, "candidate")


# Create list of visit for candidates

# Get list of PSCID
PSCID_list = []
for idx in range(len(candidates_list)):
    PSCID_list.append(candidates_list[idx]['PSCID'])

# get candidate dictionary from fetch_candidate_info and create the candidate object
cand1_dict = DataManagement.fetch_candidate_info(database, candidates_list[0]['PSCID'])
candidate1 = candidate.Candidate(cand1_dict['Firstname'],
                                 cand1_dict['Lastname'],
                                 cand1_dict['Phone'],
                                 cand1_dict['Middlename'],
                                 cand1_dict['CandID'],
                                 cand1_dict['Status'],
                                 cand1_dict['PSCID']
                                )

# select visits for candidate1
visitdone = DataManagement.database_selectwhere_table(database,
                                                      'session',
                                                      'WHERE CandID = ?',
                                                      (candidate1.candid,)
                                                     )
# Create a new visit scheduled for candidate
visitproject   = 'Project1'    #TODO selection from dropdown
visitprojectID = DataManagement.fetch_projectID(database, visitproject)
visitlabel     = 'V0'          #TODO selection from droplist
visitdate      = '2014-12-25'  #TODO add regex controls
visittime      = '13:15'       #TODO add regex controls
visitlocation  = 'CRIUGM lobby'
visitwithwhom  = 'Annie'
visitstatus    = 'Scheduled'
# Create visit data array to insert
visitdata = (candidate1.candid,
             visitlabel,
             visitprojectID,
             visitdate,
             visittime,
             visitlocation,
             visitwithwhom,
             visitstatus
            )
#DataManagement.save_visit_data(database, visitdata)
update_fields = 'VisitDate = ?, VisitTime = ?'
where_fields  = 'CandID = ? AND VisitLabel = ? AND ProjectID = ?'
query_values  = ('2014-12-24',      '13:30',     #update values
                 candidate1.candid, visitlabel, visitprojectID  # where values
                )
DataManagement.database_update_table(database,      'session',
                                     update_fields, where_fields,
                                     query_values
                                    )

#nextvisitlabel = DataManagement.determine_next_visit_label(database,
#                                                           visitprojectID,
#                                                           candidate1.candid
#                                                          )


# # visitdata = candidate1.set_visit_date(candidate1.candid, visitlabel,
# #                                       visitproject,      visitdate,
# #                                       visittime,         visitlocation,
# #                                       visitwithwhom,     visitstatus
# #                                      )
# #DataManagement.save_visit_data(database, visitdata)
#
# #candidate1.set_next_visit_window(candidate1, visitdata)
#
#
# # determine what would be the next visit to schedule
# if ( len(visitdone) ):
#     print "Find next visit based on ProjectID"
# else:
#     print "Schedule first visit based on the ProjectID"

# #add visit data to candidates
# db = dict(DataManagement.read_candidate_data())
# #get all key values
# keylist = []
# for key in db:
#     keylist.append(key)
#
# candidate1 = db.get(keylist[0])
# visitlabel = 'V0'  #TODO selection from droplist
# visitdate = '2014-12-25'  #TODO add regex controls
# visittime = '13:15' #TODO add regex controls
# visitwhere = 'CRIUGM lobby'
# visitwhom = 'Annie'
# thisvisit = candidate1.set_visit_date(visitlabel, visitdate, visittime, visitwhere, visitwhom)
# candidate1.set_next_visit_window(candidate1, thisvisit)
# DataManagement.save_candidate_data(db)
#
#
# candidate2 = db.get(keylist[1])
# visitlabel = 'V1'  #TODO selection from droplist
# visitdate = '2014-12-27'  #TODO add regex controls
# visittime = '14:30' #TODO add regex controls
# visitwhere = 'CRIUGM M-124'
# visitwhom = 'Jean'
# thisvisit = candidate2.set_visit_date(visitlabel, visitdate, visittime, visitwhere, visitwhom)
# candidate2.set_next_visit_window(candidate2, thisvisit)
# DataManagement.save_candidate_data(db)
#
# candidate3 = db.get(keylist[2])
# visitlabel = 'V1'  #TODO selection from droplist
# visitdate = '2015-01-13'  #TODO add regex controls
# visittime = '09:15' #TODO add regex controls
# visitwhere = 'McDo'
# visitwhom = 'Scott'
# thisvisit = candidate3.set_visit_date(visitlabel, visitdate, visittime, visitwhere, visitwhom)
# candidate3.set_next_visit_window(candidate3, thisvisit)
# DataManagement.save_candidate_data(db)
# Utilities.print_object(thisvisit)
#
# candidate4 = db.get(keylist[3])
# visitlabel = 'V0'  #TODO selection from droplist
# visitdate = '2015-02-24'  #TODO add regex controls
# visittime = '15:30' #TODO add regex controls
# visitwhere = 'IGA'
# visitwhom = 'Charlie'
# thisvisit = candidate4.set_visit_date(visitlabel, visitdate, visittime, visitwhere, visitwhom)
# candidate4.set_next_visit_window(candidate4, thisvisit)
#
# Utilities.print_object(thisvisit)
#
# DataManagement.save_candidate_data(db)
