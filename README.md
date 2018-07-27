# Python VNDB Public Database API wrapper

This module provides a method of requesting information from the [VNDB Public database API](https://vndb.org/d11) from within Python. Currently only get methods are implemented. "get user, get votelist, get vnlist, get wishlist" do not currently work.

The wrapper is accessed using a Vndb class object which is accessible once the package is imported. This class has several methods which are used to interface with the database. A complete list and description of these methods is as follows:

* login - Establishes a connection to the database, this is a TLS connection by default.
* logout - Closes connection to the database
* dbstats - returns the current statistics of the database
* vn
* releases 
* producer
* character
* staff
* user
* votelist
* vnlist
* wishlist

The other methods get information related to their name: vns, releases etc.

## Login method
Firstly, the database is accessed through a socket. This must be opened so that data can be passed between the server and client. This is done automatically one Vndb.login() is called. Additionally, to send requests to the server, you must be logged in. This can be done using the default values given in the module. Additionally you can pass the username and password of your VNDB account by passing a user and password argument to the method. Hashing is done server side, so if you do not use TLS when sending a password, you're asking for trouble! TLS is enabled by default though so don't worry.

## Logout method
This will simply shutdown the active socket and close it. To make new requests to the server you must call Vndb.login() first. This will create and connect a new socket and log you in.


## dbstats method
A quick method that returns a dict object containing basic summary stats of the database. These contain information such:
* total users
* total vns
* total tags
etc.

For full detail, check the [API docs](https://vndb.org/d11)


## Get methods
The database's main functionality comes from get requests. These requests require a *type*, at least one *flag*, can also contain a *filter*, and/or a set of *options*. Flags must be passed as strings or a list of strings. Filters must also be passed as a string or list of strings. Options must be a dict containing a number of entirely optional keys and appropriate corresponding values.

The total list of get-types is as follows:

* vn
* releases
* producer
* character
* staff
* user
* votelist
* vnlist
* wishlist

For each get type, there are different sets of possible flags to choose from. You must request at least one flag. You can request several flags by passing a list of flags to the associated method. The wrapper will enforce that you use correct flags to avoid returning a parse error in response to a malformed request. The list of possible flags can be found in the Vndb.possible_flags attribute. This dict contains lists of all the possible keys for each get-type as values with the associated get-type as the key. E.g if I wanted to find the entire set of possible keys for get vn, I could do so with Vndb_class_instance.possible_flags["vn"].

It is possible to filter on several different return parameters for each get-type. Additionally each of these filter parameters supports different types and numbers of operands. Filter enforcing has not been implemented yet as I haven't figured out a way of doing it that is not incredibly bulky or inelegant. As such, filters are experimental! Your requests may well fail if you do not form your filters properly. That said, the object methods will still interpret your filters into the database readable form if passed as a string or list of strings.

Options is an entirely optional parameter. This must be in the form of a dict which has any number of the following keys

* page
* results
* sort
* reverse

In terms of acceptable values, page requires an int which refers to the page of results you want returned. "results" also accepts an int which refers to the total number of results per page, e.g for {"page":2, "results": 3} you will recieve results 3-5 that matched your request. "sort" accepts a string which refers to the parameter to be sorted by. It is only possible to sort on one parameter. The set of parameters that it is possible to sort on varies with each get-type. For more info, please refer to the actual [API docs](https://vndb.org/d11). Again, I may implement an attribute that allows you to check or enforces correct sorting arguments if I get really bored. "reverse" accepts a bool which refers to whether or not you want the returned results to be reversed in order. These options are not checked in any way before being passed to the server.

## In terms of WIP
* Clearly no set methods have been implemented, but they are less useful so we'll see if I get round to it
* Full filter checking for each get type if I get bored enough
* Full option checking for each get type (basically sort checking)
