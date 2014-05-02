# Pipi Beta 1

This document describes the first beta release of Pipi.

* Name: http://rfc.abstractfactory.io/spec/49
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: draft
* Related: RFC10

Language can be found in RFC1

# Copyright



# Change Process

This document is not to be altered by anyone but the editor.

# Language

In addition to the language specified in RFC1, PLAYER refers to any person in contact with a content life-cycle, PIPI refers to the full Pipi software suite, BETA refers to this particular release of PIPI, beta 1.

# Goal

Deliver a platform for associating arbitrary, heterogenous metadata to folders in a file-system as a means of configuring an operating system for digital content creation in a collaborative environment.

# Components

DASHBOARD is a file-system browser facilitating a collaborative workflow and configuration. The PLAYER is presented with a miller-columns view of the data in which he interacts with and makes a choice of which folder, or workspace, to work within.

ABOUT is a metadata management utility, a graphical front-end to the open-source library Open Metadata. The PLAYER interacts with metadata on a file-system through ABOUT which is then used as configuration data for DASHBOARD

# Details

PIPI is built using Python (2.7) along with the third-party libraries PyQt (5), PyZMQ (4) and msgpack (0.4).

PIPI communicates with interconnected software using PyZMQ, a binding library for ZeroMQ; however the feature is disabled in this BETA.
