import keyring

MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

# the service is just a namespace for your app
service_id = 'IM_YOUR_APP!'  

netID = 'John Smith'

# save password
keyring.set_password(service_id, netID, "password123")

# optionally, abuse `set_password` to save username onto keyring
# we're just using some known magic string in the username field
keyring.set_password(service_id, MAGIC_USERNAME_KEY, netID)


# again, abusing `get_password` to get the username.
# after all, the keyring is just a key-value store
netID = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
password = keyring.get_password(service_id, netID)  

print ("Done")
