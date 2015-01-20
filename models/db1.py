# coding: utf8
db.define_table('mclient',
                Field('last_name', 'string'),
                Field('first_name','string'),
                Field('minst', 'string'),
                Field('address', 'string'),
                Field('zip', 'string'),
                Field('member_id', 'integer'),
                Field('stat','string'),
 #               auth.signature
                primarykey = ['member_id'],
                migrate = False
                )

db.define_table('case_action_master',
                Field('action_name'),
                Field('action_value'),
 #               auth.signature,
                primarykey = ['action_name'],
                migrate = False
)



db.define_table('case_master',
                Field('case_number', 'string'),
                Field('member_id', 'reference mclient', ondelete='NO ACTION'),
                Field('description','text'),
                Field('date_assigned', 'date'),
                Field('date_closed','date'),
                Field('dead_file_box_number'),
                Field('case_disposition', 'text'),
                Field('assigned_to', 'reference auth_user', ondelete='NO ACTION'),
               
#                auth.signature,
                
                primarykey = ['case_number'],
                migrate = False
 )

db.define_table('case_action',
                Field('record_id', 'id'),
                Field('case_id'),# 'reference case_master'),
                Field('action_id'), #'reference case_action_master'),
                Field('date_performed', 'date'),
                Field('remarks', 'text'),
 #               auth.signature,
                primarykey = ['record_id'],
                migrate = False
 )

dbx.define_table('casemasterxport',
                Field('case_number', 'string'),
                Field('member_id', 'integer'),
                Field('lastname'),
                Field('firstname'),
                Field('institution'),
                Field('casedescription', 'text'),
                Field('dateassigned', 'date'),
                Field('dateclosed', 'date'),
                Field('deadfileboxnumber'),
                Field('memberstatus'),
                Field('casedisposition'),
                migrate= False,
                primarykey=['case_number']
                )

db.define_table('caseactionsxport',
                Field('recordid', 'id'),
                Field('casenumber', 'string'),
                Field('action'),
                Field('actiondate', 'date'),
                Field('remarks'),
                migrate = False,
                primarykey = ['recordid']
                )

db2_prod.define_table('member',
                 Field('id_no','integer'),
                 Field('name', 'string','length=21'),
                 Field('first_name', 'string', 'length=21'),
                 Field('minst', 'string', 'length=7'),
                 Field('address','string', 'length=35'),
                 Field('zip','string', 'length=10'),
                 Field('phone','string', 'length=13'),
                 Field('email','string', 'length= 50'),
                 Field('stat','string','length=3'),
                 primarykey = ['id_no'],
                 migrate = False)
