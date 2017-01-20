from pyparsing import *

class Parser:
    # Ansible
    ansible = "TASK [" + SkipTo(']',include=True) + SkipTo(LineEnd()) + oneOf('changed ok failed error unreachable') + ': ' + SkipTo(LineEnd())
    ansible.setParseAction(lambda x:{"task":x[1][0],"status":x[3],"subject": x[5],"ansible":1})
    
    # Vagrant
    vagrant_start = Literal("[") + SkipTo("]",include=True) + "Importing base box '" + SkipTo("'",include=True) + SkipTo(LineEnd())
    vagrant_start.setParseAction(lambda x:{"vm":x[1][0],"image":x[3][0],"vagrant":1,"global":"Booting VM"})

    vagrant_start = Literal("[") + SkipTo("]",include=True) + "Machine booted and ready!" + SkipTo(LineEnd())
    vagrant_start.setParseAction(lambda x:{"vm":x[1][0], "vagrant":1, "global":"VM Booted up"})

    gradle_start = "Downloading https://services.gradle.org" + SkipTo(LineEnd())
    gradle_start.setParseAction(lambda x:{"gradle":1, "global":"Gradle started"})

    foo = Literal("Foo")
    foo.setParseAction(lambda x:{'payload':'foo'})

    
