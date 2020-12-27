# Freshwork-Assignment
This repository contains my solution for the given assignment.

datastore.py has the main functions i.e create, read and write with all the given constraints.

check.py file is a test file which imports the datastore in order to try creating, reading and deleting data.

<h1> Functional Requirements</h1>
<ol>
<li>It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.  </li>
<li>   A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.  </li>
<li>  If Create is invoked for an existing key, an appropriate error must be returned.  </li>
<li>  A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.  </li>
<li> A Delete operation can be performed by providing the key.  </li>
<li> Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.  </li>
<li>  Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.</li>
</ol>

<h1>Non-functional Requirements.</h1>
<ol>
<li>The size of the file storing data must never exceed 1GB.</li>
<li>More than one client process cannot be allowed to use the same file as a data store at any given time.</li>
<li>A client process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread-safe.</li>
<li>The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.</li>
</ol>
