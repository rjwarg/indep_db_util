# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import sys

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def copy_actions():
    actions = db(db.caseactionsxport).select()
    error_list = []
    for a in actions:
        try:
            db.case_action.insert(
                                  case_id = db(db.case_master.case_number == a.casenumber).select().first(),
                                  action_id = db(db.case_action_master.action_name == a.action).select().first(),
                                  date_performed = a.actiondate,
                                  remarks = a.remarks
                                  )
        except:
             error_list.append({"action_in_error": a, "error_is": sys.exc_info()})
             
                
    return locals()                

def copy_cases():
    cases = dbx(dbx.casemasterxport).select()
    error_list = []
#    return locals()
    
    
    for case in cases:
        try:
            db.case_master.insert(    case_number = case.case_number,
                                      member_id = case.member_id,
                                      description = case.casedescription,
                                      date_assigned = case.dateassigned,
                                      date_closed = case.dateclosed,
                                      case_disposition = case.casedisposition,
                                      assigned_to = 3
                                      )
            
        except :
            error_list.append({"case_in_error": case, "error_is": sys.exc_info()})
                              
    return locals()

def test():
    # test for existence of a record
    result =  db.mclient(999) != None
    result_list = []
    result_list.append({"999 exists?": result})
    result = db(db.mclient.member_id == 111).count()>0
    result_list.append({"111 exists?": result})
    return locals()

def build_client():
    member_id_list = db().select(db.casemasterxport.member_id, distinct=True)
    member_list = []
    error_list = []   
    
    for m in member_id_list:
        n = m.member_id
        member_list.append(n)
        # does this client already exist?
        if db.mclient(n) == None:
            member = db2_prod.member(n)
            if member:
                try:
                    db.mclient.insert(member_id= member.id_no,
                                   last_name = member.name,
                                   first_name = member.first_name,
                                   minst = member.minst,
                                   address = member.address,
                                   zip = member.zip,
                                   stat = member.stat
                                   )
                except:
                    error_list.append({"member_in_error": member})
            else:
                error_list.append(m)
                error_list.append(n)
          #  member_list.append(member)
        else:
            error_list.append({"client_exists": n})
        
    
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
