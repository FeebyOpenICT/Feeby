import axios from 'axios'

axios.get('localhost/api/v1/posts/').then (
  response => console.log(response)
)

axios.post ('api/v1/post/', {
  headers : {
    'Content-Type' : 'application/json',
    'Accept' : 'application/json',
    'Authorization' : 'Bearer {jwt}',
    "title": "string",
    "description": "string",
  }
}).then ( response => console.log(response) )


