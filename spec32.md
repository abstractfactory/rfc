# Advanced Software Discovery

This document extends upon RFC21, Software Discovery by the use of multiple keywords.

* Name: http://rfc.abstractfactory.io/spec/32
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Related: RFC21
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

In RFC21 we spoke of finding software on the local hard drive based on a single keyword.

```python
 _________         ___________         ___________________________________
|         |       |           |       |                                   |
| gimp2_1 |------>| resolve() |------>| c:\program files\gimp2.1\gimp.exe |
|_________|       |___________|       |___________________________________|

```

How about situations where the software consists of plug-ins? Each plug-in will in turn require discovery and reference via key; this specification will cover all possible methods of plug-in discovery.

# Architecture

```python
 _________       									  _______________________
|         |      									 |                       |
| gimp2_1 |---------. 					   .-------->| environment variables |
|_________|         .					   .		 |_______________________|
 _________        __v____         _________._         _______________
|         |      |       |       |           |       |               |
| blur3_2 |----->| query |------>| resolve() |------>| absolute path |
|_________|      |_______|       |___________|       |_______________|
 _________          A 					   .		  _______
|         |         .     				   .		 |       |
| tint0_6 |--------- 					    -------->| flags |
|_________| 							    		 |_______|

```

The above diagram illustrates a general process. There is a key for each software executable, as per RFC21, and a key for each plug-in and version. All keys are resolved into either an absolute path, environment variable or flag.

