from pyparsing import *

class Parser:
    test_pattern = "{{{" + SkipTo("}}}",include=True)
    test_pattern.setParseAction(lambda x:{"test":x[1][0]})

    test_pattern2 = "1" + SkipTo(LineEnd(),include=True) + SkipTo(LineEnd(),include=True) + "2"
    test_pattern2.setParseAction(lambda x:{"test":x[1]})

    ansible = "TASK [" + SkipTo(']',include=True) + SkipTo(LineEnd(),include=True) + oneOf('changed ok failed error unreachable') + ': ' + SkipTo(LineEnd(),include=True)
    ansible.setParseAction(lambda x:{"task":x[1],"status":x[3],"subject": x[5],"ansible":1})

    ansible2 = "TASK [" + SkipTo(']',include=True) + SkipTo(LineEnd(),include=True) + SkipTo(LineEnd(),include=True) + oneOf('changed ok failed error unreachable') + ': ' + SkipTo(LineEnd(),include=True)
    ansible2.setParseAction(lambda x:{"task":x[1],"status":x[2],"subject": x[4],"ansible":1})

    # Vagrant
    vagrant_start = Literal("[") + SkipTo("]",include=True) + "Importing base box '" + SkipTo("'",include=True) + SkipTo(LineEnd(),include=True)
    vagrant_start.setParseAction(lambda x:{"vm":x[1][0],"image":x[3][0],"vagrant":1,"global":"Booting VM"})

    vagrant_start = Literal("[") + SkipTo("]",include=True) + "Machine booted and ready!" + SkipTo(LineEnd(), include=True)
    vagrant_start.setParseAction(lambda x:{"vm":x[1][0], "vagrant":1, "global":"VM Booted up"})

    gradle_start = "Downloading https://services.gradle.org" + SkipTo(LineEnd(), include=True)
    gradle_start.setParseAction(lambda x:{"gradle":1, "global":"Gradle started"})

    debian_preparing = "Preparing to unpack" + Word(printables) + SkipTo(LineEnd(), include=True)
    debian_preparing.setParseAction(lambda x:{"debian":1, "package":x[1]})

