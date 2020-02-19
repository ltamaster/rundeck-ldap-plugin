import ldap
import argparse
import logging
import os
import sys

log_level = 'INFO'
if os.environ.get('RD_JOB_LOGLEVEL') == 'DEBUG':
    log_level = 'DEBUG'
else:
    log_level = 'ERROR'

console = logging.StreamHandler()
console.stream=sys.stdout

log = logging.getLogger()
log.addHandler(console)
log.setLevel(log_level)

parser = argparse.ArgumentParser(description='Run ldap command.')
parser.add_argument('--ldapServer', help='the ldap server')
parser.add_argument('--bindUser', help='the bindUser')
parser.add_argument('--bindPassword', help='the bindPassword')
parser.add_argument('--baseDn', help='the baseDn')
parser.add_argument('--criteria', help='the criteria')
args = parser.parse_args()

ldapServer = args.ldapServer
# 'ldap://192.168.16.12:38'
user_dn = args.bindUser
# r"Administrator@foo.com"
password = args.bindPassword
baseDn = args.baseDn
# "CN=Users,DC=foo,DC=com"
criteria = args.criteria
# "(&(objectClass=user)(sAMAccountName=username))"

con = ldap.initialize(ldap)

attributes = ['displayName', 'company']

try:
    con.simple_bind_s(user_dn, password)
    res = con.search_s(baseDn, ldap.SCOPE_SUBTREE, '(objectClass=User)')
    for dn, entry in res:
        print(dn)
except Exception as error:
    print(error)
