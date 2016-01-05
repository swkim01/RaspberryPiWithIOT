#-*- coding: 'utf-8' -*-
#!/usr/bin/env python
import pexpect

child = pexpect.spawn('bash')
#child = pexpect.spawn('bash', ['-c', 'ls'])
with open('pexpect.log', 'w') as f:
    child.logfile_read = f
    #index = child.expect("\$\x1b\[00m ")
    index = child.expect("\$[^ ]* ")
    cmd='ls'
    child.sendline(cmd)
    #print child.before.decode('utf-8')
    #index = child.expect("\$\x1b\[00m ")
    index = child.expect("\$[^ ]* ")
    print child.before[len(cmd)+2:].decode('utf-8')
    print child.after.decode('utf-8')
