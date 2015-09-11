# Retrieve unique ID from NFC card

from subprocess import check_output

def getUID():
  cmd = """nfc-poll | grep 'UID'"""
  out = check_output(cmd, shell=True)
  
  # Parse UID
  uid = out[21:47]
  uid = uid.strip()
  uid = uid.replace(" ", "")

  return uid

#print(getUID())
