# Backend-Coding-Challenge

First, thanks for your interest in corrux! We put together this coding challenge to give you a chance to show us your skills on a simplified but realistic task: harvesting, aggregating, and serving various equipment data streams.  This is our first iteration of the challenge, so if you find bugs or something is unclear, please raise an issue in the repo or email me directly: sion@corrux.io

## Description of Problem
![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Caterpillar_330B_Hydraulic_Excavator_side_2_-_Hillsboro%2C_Oregon.JPG/640px-Caterpillar_330B_Hydraulic_Excavator_side_2_-_Hillsboro%2C_Oregon.JPG)

BigCo, a construction company, would like to enhance their analytics capabilities on their single excavator.  This excavator is connected to their platform and provides data through two channels: a website, and an API with three endpoints.

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

#### `/can_stream`

The excavator sends messages via an internal [CAN bus](https://en.wikipedia.org/wiki/CAN_bus) (the link is for your curiousity only -- you don't need to know anything about the CAN standard for this challenge).  The messages use some kind of encoding, but we can query them easily enough.  This endpoint returns the last 50 messages:

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
        "timestamp": "2019-04-09 14:11:00"
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
        "timestamp": "2019-04-09 14:11:00"
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
        "timestamp": "2019-04-09 14:07:00"
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
        "timestamp": "2019-04-09 14:07:00"
    }
]
```
Every message has an ID, an 8-part message in hex encoding, and a timestamp.  One of these codes corresponds to the measurement `cumulative_fuel_used`.  It's a bonus question to figure out which ID that is (see the evaluation section)!

## Your task

Your task is to pull these three data sources to a central datastore, and provide a small REST API that does some aggregations specified by the customer.  The endpoints for you to implement, in order of importance, are:

* `GET excavator_operating_hours_since_last_maintenance` this endpoint just tells the customer how many operating hours ago (from now) the most recent maintenance was.  This endpoint just returns a single `number`, the decimal number of operating hours since the last maintenance event.
* `GET excavator_average_fuel_rate_past_24h` this endpoint also returns a single `number`, the average fuel rate.  This is defined as the total fuel used in the past 24 hours divided by total operating hours in the past 24h.
* `GET excavator_last_10_CAN_messages` this endpoint has the same response structure as the `can_stream` endpoint above.  It simply returns the ten most recent messages instead of fifty.
* `GET excavator_operational` this endpoint will return whether the machine is operational or not, based on the last query (scrape) of the BigCo asset manager. It will be a string that says either `'operational'` or `'down'`

The only design constraint is that you MUST store data you pull from the API/scrape from the website in a database or other datastore.  That is, you may not simply have your endpoints query the original endpoints to construct responses.

Other than that, the rest is up to you: architecture, programming languages, frameworks whatever.  To make things easier, we provide a skeleton architecture in `docker-compose.yml` with some function stubs and comments.

## Included files

We've included a skeletal outline the solution.  You can run it with `docker-compose up`, if you have docker-compose installed.  Note the functions are just stubs, you will have to implement all the logic.  This is just here for your reference, so feel free to use some, all, or none of the provided code in your solution.

## Evaluation

You will be evaluated on the critera below.  Subjective criteria (e.g. style and convention) will be a blind review.

### Completeness and correctness: up to 5 points:

1. All four endpoints are implemented and return correct results. *5 pts*
1. Three endpoints are implemented and return correct results. *4 pts*
1. At least two endpoints are implemented and return correct results. *3 pts*
1. At least two endpoints are implemented. There may be bugs or errors in the calculations, but works end to end. *2 pts*
1. At least one endpoint is implemented, possibly with errors but works end to end. *1 pt*
1. Anything else. *0 pts*

### Code style and conventions: up to 4 points:

1. Code is logically organized and clearly commented. Style both in code and documentation is consistent and clear.  There are at least some tests or assertions and exception handling (if necessary). *4 pts*
1. Code is logically organized and clearly commented. Style both in code and documentation is consistent and clear. *3 pts*
1. Code is logically organized, but documentation is inconsistent or confusing. *2 pts*
1. Code is disorganized and hard to follow.  Inconsistent and arbitrary style. *1 pt*
1. Anything else. *0 pts*

## Submitting a solution

You can fork this repo, but we don't recommend working on your fork directly. After all, anyone can see the forks and thus what you're working on.

You can either work in a private repo (on any hosting service) and invite me when you're ready, or you can submit an archive to me via email (sion@corrux.io).  However you do it, you should include clear instructions on how to run it.

## Thanks

Thanks and have fun!

## Image Credits

* Wikimedia Commons contributors, ["File:Caterpillar 330B Hydraulic Excavator side 2 - Hillsboro, Oregon.JPG,"](https://commons.wikimedia.org/w/index.php?title=File:Caterpillar_330B_Hydraulic_Excavator_side_2_-_Hillsboro,_Oregon.JPG&oldid=43302521) Wikimedia Commons, the free media repository available at  under the  Creative Commons Attribution-Share Alike 3.0 Unported, 2.5 Generic, 2.0 Generic and 1.0 Generic license
