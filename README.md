# Backend-Coding-Challenge

First, thanks for your interest in corrux! We put together this coding challenge to give you a chance to show us your skills on a simplified but realistic task: harvesting, aggregating, and serving various equipment data streams.  This is our first iteration of the challenge, so if you find bugs or something is unclear, please raise an issue in the repo or email me directly: ryan@corrux.io

## Description

BigCo, a construction company, would like to enhance their analytics capabilities on their single excavator.  This excavator is connected to their platform and provides data through three channels: a website, and an API with two endpoints.

### The BigCo Dashboard

[BigCo's Dashboard](https://corrux-challenge.azurewebsites.net/login) is very simple.  You log in, and you can see the status of the excavator: either `OPERATIONAL` or `DOWN`. The customer has supplied us with the credentials, which we'll pass along to you.

### The BigCo API

Three endpoints are provided: `/auth`, `/excavator_stats`, and `/can_stream`.

#### `/auth`

Here you can generate a token to use the other two endpoints.  You can use the same username and password as for the dashboard.  If your username were `example@example.com` and your password were `12345`, then a curl to the endpoint would look like this:

```bash
$ curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username":"example@example.com","password":"12345"}' https://corrux-challenge.azurewebsites.net/auth
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTQ4MjIxMTYsImlhdCI6MTU1NDgyMTgxNiwibmJmIjoxNTU0ODIxODE2LCJpZGVudGl0eSI6MX0.IRfIYZF61DeRqhzJ_nWjQ6laYXQs96Fgt680o1AyKMM"}
```

You'll need the access token to access the other endpoints.  Careful: the token expires frequently!
