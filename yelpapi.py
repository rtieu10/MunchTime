#Business Search         https://api.yelp.com/v3/businesses/search
#Phone Search            https://api.yelp.com/v3/businesses/search/phone
#Transaction History     https://api.yelp.com/v3/transactions/{transaction_type}/search
#Business Details        https://api.yelp.com/v3/businesses/{id}
#Business Match          https://api.yelp.com/v3/businesses/matches
#Reviews                 https://api.yelp.com/v3/businesses/{id}/reviews
#Autocomplete            https://api.yelp.com/v3/autocomplete

import requests
from YelpAPI import API_KEY

API_KEY = iDdLIfVI4JYmglY_qsaRE0KsmDEwmiQ2XssHTiIlCqK7Xf9HRbgB-fFGKht4rSX7Lug42y0PA2bdYlmj_GsPP-b46JP3aF7nOTwCjaWxy0DSTpc0fP1u47imgwlTXnYx
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization':'bearer %s' % API_KEY}  #passing API key to yelp

#Define parameters
#creating a dict of params with keys & values
PARAMETERS={'term':'bubble tea',
            'limit':25,
            'radius':10,
            'location':'New York'
            }
#Making a request into a yelp API
#creating a response variable that stores what the Yelp API returned
response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
#response is returned in the form of a JSON string, so we convert it to Python dict so we can iterate through

#converting JSON string to a Python Dictionary
business_data = response.json()
print(business_data)  #should print all the data received from Yelp API
