<h1 align="center">
  <img src="../givit/static/img/leaveit2givit.jpg" />
</h1>

# background & vision

“Givit”is a non-profitable organization which operated by IDC student and aiming to help economically struggling students(“friends”) by helping them to furnish their apartments.

Givit web-application will automate the procces of gathering our friends demands, findind the furniture online and get thier approval for coordinate and transfer.

# app components

<h1 align="center">
  <img src="../givit/static/img/overview.png" />
</h1>
## Backend

implemted with Django the following components:

1. Demand controller-manage the friends requests and the demand DB.
2. Found controller-get updates from found-DB mange the verification and coordination procces.

3. Gatherer Controller:
   - automated system that will iterate the relevant sites(firat step Agora site second step facbook groups).
   - get requests from the Demand DB and updete the found DB.
   - operate details: we open vm in google cloud and using crontab run our script every hour, how create json file with our new searches.

DB- TBD.

## Frontend

implemented with bootstrap the following components:

1. friends:

   - private Feed - tracks the furniture which was found by the app, waits for the friend approval.
   - request box - a form which the friends will fill in order to request new items.

2. coordinte: track all the items that was approved by our friends.

## login system

- two users groups: friends, coordinates.
- technology- TBD.

## CI/CD- TBD

## issues & dillemas

- online feed is good ides with server-sdie rendering (or its better clieant side? how to avoid react in first stage?)
- DB?

# Getting started:

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them:

- Download and Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/) on your local computer
- Clone/ Download the zip file from the Groot repository to your local computer

### Initializing Project Groot Virtual Environment

A step by step series that tell you how to get Project Groot up and running

1. Clone + Fork the repository
2. Open command prompt and navigate to the local directory where all the files are
3. Spin the environment using:

```
   vagrant up
   vagrant ssh
```

4. navigate to the sync repo in vm

```
   cd /vagrant/GIVIT/
   python3 manage.py runserver 0:8000
```

5. open your browser and nevigate to http://localhost:8000/Hello/

6. When finished, tear down the environment using:

```
exit
vagrant destroy -f
```

# Dependencies:

we are planning to supply a requirement.txt and a bootstrap file that will install all the needed libraries.

this are the current use libraries:

Python 3.7

Django 3.1

beautifulsoup4 4.8.2

bs4 0.0.1

urllib3 1.25.7

# team members:

### -Rotem Ben Zvi

### -Nadav Shoshan

### -Matan Sinai

### -Tal kind

### -Lior Sidi
