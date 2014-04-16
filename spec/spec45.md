# The Request Pattern

This document extends the general Observer Pattern with the ability to respond.

* Name: http://rfc.abstractfactory.io/spec/45
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

This pattern is a combination of ["Observer Pattern"][] found in e.g. Qt and ["Request-reply Pattern"][] found in e.g. web-server communication and is useful in inter-process communication between decoupled, yet associated components of a software architecture design; particularly GUI programming.

```python
                      __________       
                     |          |      
 ____________        |  signal  |        _________
|            |------>|__________|------>|         |
|  graphics  |        __________        |  logic  |
|____________|<------|          |<------|_________|
                     |  signal  |       
                     |__________|

```

Picture a graphical user interface (`graphics`) where a button represents performing a command; e.g. running a program.

Traditionally (e.g. in [MVP][]), `graphics` isn't actually performing any actions, but merely communicating that this is what the user has requested to have happen.

`logic` may be subscribed to the events of `graphics`. When the button within `graphics` is pressed, an event may be emitted that is received by `logic`. Once `logic` is finished performing the requested operation, `logic` may signal back to `graphics` that the action has been performed, so as to let `graphics` illustrate this to the user; e.g. with a notification widget.

In this example, the signal is a one-way stream of information. Data may only be passed from `graphics` to `logic`; `subject` to `observer`. However as we've just seen, there are two (2) signals for any action taking place.

In this scenario, `graphics` and `logic` are both observers and they are both subjects; e.g. they both request and they both respond.

```python
# Subject on emitting, observer on receiving.
                    __________       
  subject          |          |        observer
 __________        |          |        _________
|          |------>|__________|------>|         |
|          |        __________        |         |
|__________|<------|          |<------|_________|
                   |          |       
  observer         |__________|        subject

```

The Request Pattern is a method of distilling this procedure into a single call; the `request`.

```python
  subject                                observer
 __________         ___________         _________
|          |------>|           |------>|         |
|  button  |       |  request  |       |  logic  |
|__________|<------|___________|<------|_________|
 
```

Here, an `observer` is connected to `subject` via a `request`. The button in this scenario is said to emit a `request` as opposed to a `signal`. When `button` emits a `request`, the subscribed `observer` performs the given action and returns a value.

```python
# Trivial example in Python
#  --------------------------------
#
#  Marcus doesn't know his own age 
#
#  --------------------------------- 
>>> observer = type('Marcus', (object,), {})()
>>> observer.get_age = Request()
>>> observer.get_age()
None

```

```python
# Trivial example in Python
#  --------------------------------
#
#  Mom to the rescue
#
#  --------------------------------- 
>>> observer = type('Marcus', (object,), {})()
>>> observer.get_age = Request()

>>> subject = type('Mom', (object,), {})()
>>> subject.give_age = lambda: 27

>>> observer.get_age.connect(subject.give_age)
>>> observer.get_age()
27

```

# Architecture

### Multiple observers

As a side-effect to the given loose-coupling of this pattern, `request` objects may cope with multiple observers.

In the majority of cases, a request will have 0-1 observers. 0 meaning no one is there to answer the request - in which case it may simply return a null - 1 meaning there is exactly one component potentially capable of fullfilling the request. I say "potentially" because even though in the majority of cases, the return value will be what is expected, but the pattern allows for non-expected return values as well.

```python
                                        _________
                    ___________        |         |
 __________        |           |------>| primary |  # In the cloud
|          |------>|           |<------|_________|
| graphics |       |  request  |        ___________
|__________|<------|           |------>|           |
                   |___________|<------| secondary |  # Local
                                       |___________|
 
```

Picture another graphical user interface. This one has a button within `graphics` which requests the factorial of a very high number, requiring phenomenal computational horse-power.

When the button is pressed, `graphics` sends a request to a worker in the cloud; `primary`, a remote workstation with plentiful of computational horse-power. When `primary` has completed performing this task, it returns a value to `graphics`.

Now, what if the `graphics` suddenly got cut-off from the internet? `primary` would no longer be there to fulfill its duties and yet the user is awaiting an answer. In this scenario, another observer may be subscribed to the request, `secondary`, to fill in for when `primary` fails. This observer is running the operation locally and thus is a little slower; but, it gets the job done.

This pattern of handling and discarding requests may be called the [Strategy Pattern][]

```python
# Multiple observers example
observer = type('Math', (object,), {})()
observer.get_factorial = pifou.signal.Request()

subject1 = type('CloudService', (object,), {})()
subject2 = type('LocalService', (object,), {})()


def compute_remote():
    # Fails..
    return None


def compute_local():
    time.sleep(1)
    return 27


subject1.give_factorial = compute_remotely  # First one to try
subject2.give_factorial = compute_locally

observer.get_factorial.connect(subject1.give_factorial)
observer.get_factorial.connect(subject2.give_factorial)
observer.get_factorial()

```

[Strategy Pattern]: http://en.wikipedia.org/wiki/Strategy_pattern
["Observer Pattern"]: http://en.wikipedia.org/wiki/Observer_pattern
["Request-reply Pattern"]: http://en.wikipedia.org/wiki/Request-response
[MVP]: http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter