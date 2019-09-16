import secure_passwords
import keyring

MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

# the service is just a namespace for your app
service_id = 'IM_YOUR_APP!'  

netID = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
password = keyring.get_password(service_id, netID)  
