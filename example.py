import PeopleBrowsr
x = PeopleBrowsr("[APP ID]", "[APP KEY]")
test = x.mentions(last = "yesterday", count = "30", source = "twitter", term = "pepsi")
print test

import Kred
x = Kred("[APP ID]", "[APP KEY]")
test = x.Kred(source = "twitter", term = "pepsi")
print test