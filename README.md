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

#### `/excavator_stats`

Here you can extract some timestamped information about different monitors in the excavator. It takes two parameters, `start_time` and `end_time`.  If you use the access token from above, a call to this endpoints looks like:

```bash
$ curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTQ4MjIxMTYsImlhdCI6MTU1NDgyMTgxNiwibmJmIjoxNTU0ODIxODE2LCJpZGVudGl0eSI6MX0.IRfIYZF61DeRqhzJ_nWjQ6laYXQs96Fgt680o1AyKMM" "https://corrux-challenge.azurewebsites.net/excavator_stats?start_time=2019-03-01+00:00&end_time=2019-03-01+01:00"
[
...
    {                                                                                                                                   
        "cumulative_fuel_used": 3542.9,                                                                                                 
        "cumulative_hours_operated": 708.58,                                                                                            
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:35:00"                                                                                              
    },                                                                                                                                  
    {                                                                                                                                   
        "cumulative_fuel_used": 3543.5,                                                                                                 
        "cumulative_hours_operated": 708.7,                                                                                             
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:42:00"                                                                                              
    },                                                                                                                                  
    {                                                                                                                                   
        "cumulative_fuel_used": 3543.65,                                                                                                
        "cumulative_hours_operated": 708.73,                                                                                            
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:44:00"                                                                                              
    },                                                                                                                                  
    {                                                                                                                                   
        "cumulative_fuel_used": 3544.1,                                                                                                 
        "cumulative_hours_operated": 708.82,                                                                                            
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:49:00"                                                                                              
    },                                                                                                                                  
    {                                                                                                                                   
        "cumulative_fuel_used": 3544.6,                                                                                                 
        "cumulative_hours_operated": 708.92,
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:55:00"                                                                                              
    },                                
    {                                                                                                                                   
        "cumulative_fuel_used": 3544.65,                                                                                                
        "cumulative_hours_operated": 708.93,                                                                                            
        "most_recent_maintenance": "2019-03-01 00:00:00",                                                                               
        "timestamp": "2019-03-01 00:56:00"                                                                                              
    }  
...
]
```

#### `/can_status`

The excavator sends messages via an internal [CAN bus](https://en.wikipedia.org/wiki/CAN_bus) (the link is for your curiousity only -- you don't need to know anything about the CAN standard for this challenge).  The messages use some kind of encoding, but we can query them easily enough.  This endpoint returns the last 50:

```bash
$ curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTQ4MjIxMTYsImlhdCI6MTU1NDgyMTgxNiwibmJmIjoxNTU0ODIxODE2LCJpZGVudGl0eSI6MX0.IRfIYZF61DeRqhzJ_nWjQ6laYXQs96Fgt680o1AyKMM" "https://corrux-challenge.azurewebsites.net/can_stream"
[
...
    {   
        "id": "03",
        "message": [
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0xb",
            "0x53"
        ],
        "timestamp": "2019-04-09 14:11:52.016611"
    },
    {   
        "id": "04",
        "message": [
            "0x0",
            "0x0",
            "0xf",
            "0x36",
            "0x51",
            "0x5b",
            "0xc",
            "0x2"
        ],
        "timestamp": "2019-04-09 14:11:52.016611"
    },
    {   
        "id": "01",
        "message": [
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0x0",
            "0x3b",
            "0x10"
        ],
        "timestamp": "2019-04-09 14:07:52.016611"
    },
    {   
        "id": "02",
        "message": [
            "0x0",
            "0x0",
            "0xf",
            "0x36",
            "0x51",
            "0x58",
            "0x48",
            "0x2"
        ],
        "timestamp": "2019-04-09 14:07:52.016611"
    }
]
```
Every message has an ID, an 8-part message in hex encoding, and a timestamp.

## Your task

Your task is to pull these three data sources to a central datastore, and provide a small REST API that does some aggregations specified by the customer.  The endpoints for you to implement, in order of importance, are:

* `GET excavator_operating_hours_since_last_maintenance` this endpoint just tells the customer how many operating hours ago (from now) the most recent maintenance was.  This endpoint just returns a single `number`, the decimal number of operating hours since the last maintenance event.
* `GET excavator_average_fuel_rate_past_24h` this endpoint also returns a single `number`, the average fuel rate.  This is defined as the total fuel used in the past 24 hours divided by total operating hours in the past 24h.
* `GET excavator_last_10_CAN_messages` this endpoint has the same response structure as the `can_stream` endpoint above.  It simply returns the ten most recent messages instead of fifty.
* `GET excavator_operational` this endpoint will return whether the machine is operational or not, based on the last query (scrape) of the BigCo asset manager. It will be a string that says either `'operational'` or `'down'`

The only design constraint is that you MUST store data you pull from the API/scrape from the website in a database or other datastore.  That is, you may not simply have your endpoints query the original endpoints to construct responses.

Other than that, the rest is up to you: architecture, programming languages, frameworks whatever.  To make things easier, we provide a skeleton architecture in `docker-compose.yml` with some function stubs and comments.

## Included files

## Evaluation