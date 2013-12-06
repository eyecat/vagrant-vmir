from o365smr.mirclient import *
c = MirAdminClient('33.33.66.100','admin','mandiant',verify=False)
if not 'automation' in map(lambda x:x[1],c.get_users()):
    c.add_user('automation', 'mandiant', group_membership=(2,1))
    print 'Automation account created'
else:
    print 'Automation account exists'