import requests

url=''

account=''

password=''

mobile=''

content=''

headers={}

data={
    'account':account,
    'password':password,
    'mobile':mobile,
    'content':content,

}

response=requests.post(url,headers=headers,data=data)
