from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user    = <uid>
pwd     = <password>
factor2 = <2nd factor>
vc      = <vendor code>
app_key = <secret key>
imei    = <imei>
access_type="API2"

#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei,access_type=access_type)

print(ret)

