import base64

key = 'c2stNVlmc0Z4czVEeWE2R293bHlJbTlUM0JsYmtGSnlaamdFQ01WcHFHaG1EbVhpZmZI'

def KeyIa():
    KEY = base64.b64decode(key).decode('utf-8')
    return KEY
