import requests
url='https://learn-us-east-1-prod-fleet01-xythos.content.blackboardcdn.com/blackboard.learn.xythos.prod/5849b9bae4172/1442907?X-Blackboard-Expiration=1665954000000&X-Blackboard-Signature=ua1TDJAQ0zbKd7Ph8N9D5nqnvp90ClGLDsPD%2Fk1CP6M%3D&X-Blackboard-Client-Id=301824&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27wordlist%25281%2529.txt&response-content-type=text%2Fplain&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLWVhc3QtMSJHMEUCIFB%2BhCh9l7tUZ0jWizx9WJ0A%2B%2BRMHr3HGmJE7EwuoEsjAiEA6emPysf6vRAJkVSnmYA9TIx6V9tVpi7VOI6KOgtKQjsq1gQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTY5MDM4NjEzNjEiDAvp4kaQEsk0CHJkbyqqBDWOqTlsrBb4mpShPoPHi6HtUXk6p%2FqzqrbNU64Zm4929zW4urV2TkqIFTRcdNzai2knDAzlmwJDkeWF35oDi4A7d74Xc3%2B3IN2FDTAG%2FSCYvBdfEHUzxyAeGWD99CxsasvBqAiuqL07clOBnJw49cb1ZIE8OLf0ZVUgBqVbENczI%2Fzpq8YrpiymDqmhLKQcS4VwL0j55zP7p3kdbWK2pIyyXHO6rNh8idiKpwvDQlHyMMuA%2Fb2TNMGf5FaepBlTopZL13t%2FWV1ZiEjsh2fyL3YUTPqqQ57BT67VuFfgWGTtk0z1G7t74rlnofqZz22sAAr6reLcaDNZpG8UNYQ9ZZimHp4Z%2B%2FmTTN4nGhEjvlKsiB8TkOZQIIW%2Fel4%2FOeSQ9cKjN8Dt4GFcFgs6kG8TBVuL12olP655Z5yaIh5uBGSSsrnbgUIe%2FHKis7HXN3YKZ3QJxCcHSjTTnyGn7ZqonuIFB0UDCFlk%2BGD6lP87U5ZBKe3RYCUtNah0YREFtb5tbqCmjSOm57lrdzag%2Bbn15pEFjwJIPI731ra5bdsZM46EWb6TIRGiWMxmnJKcbFdUPJQGw49KPtSABy2cgSDS1EZf%2F12MDMDi6wrioS0AieaJi3fpgOgaU4%2FRtTuazdFCY5IoLy7uXYG%2FV22cLjM5tzfnLs0dOFrOLvGaZLkZ1LNX%2BNzdGhMFBYMBBJ%2BkTkMoRJqT7GTPf8BEfCv5lfqUKYsNbCBZLmzs%2BE1BMKjQsJoGOqkBS04Y8vDJu8t%2FwzeHjxTt3S999wkXjRYcJ4AbGUcFLnGQrc6%2BGBS7iPCLD1248nhtBfJyQbK%2FLyLuX7qmSdj9nnu4Mr44Z1JUuWqeywCcWs1lTXmKB95pt3Lf6l1RNak1zi9%2B%2FIMBRvRSn8osvF7KJBC5ZzMKyU%2FuIYzABWZ5rCVCNFat1agJihBTNTqifsXwyuIb78uwGZsuPC7e0ZOEWwYISOYeydoXdw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221016T150000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAYDKQORRYWS465GEF%2F20221016%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c6bc2e3af256a21b2c1751e319a852d0d71dd4df5edb19f03f7d68e865cc114d'
x=requests.get(url)
f=open('wordlist.txt','w')
for word in x.text.split():
	f.write(word+'\n')
f.close()	
# print(os.sys.platform)