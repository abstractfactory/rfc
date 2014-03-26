# REP - Representations Pattern

Representations facilitate the need for multiple data-types to co-exist within any given version.

* Name: https://github.com/abstract-factory/rfc/spec:6 (6/SPP)
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: spec:1

Copyright, Change Process and Language is derived via inheritance as per [spec:1][]

# Goal

As content is strongly-coupled to the application in which it was produced, it can sometimes be beneficial to maintain multiple data-types of the same version so as to allow it to be used in multiple applications other than the one it was originally created in.

Representations Pattern define a way in which to do so with little logical overhead.