import re

exp_reg = '^([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))((-)?([A-Z\d]{3}))?$'
ip = re.compile(exp_reg)
print(ip.search("MAMH970615ABA"))
