import tableauserverclient as TSC
import pandas as pd
keys = pd.read_csv('access\\tableau_server.csv')

# Enter server details
# read username and password from file
server_url = keys['server_url'][0]
sitename =  keys['sitename'][0]
username = keys['username'][0]
password = keys['password'][0]

# Set up for server authenication
tableau_auth = TSC.TableauAuth(username, password, sitename)
server = TSC.Server(server_url)


# Authenicate to Tableau Server, if error check server_url, sitename, username and password
with server.auth.sign_in(tableau_auth):
    print('login successful')
    
    # find all site content_urls for site switching
    all_sites, pagination_item = server.sites.get()

    for site in all_sites:
        print(site.name)
        server.auth.switch_site(site)

