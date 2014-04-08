# Metadata Blob

This document describes the way in which Open Metadata deals with files it cannot parse.

* Name: http://rfc.abstractfactory.io/spec/16
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* Inherits: RFC1
* State: draft

Copyright, Change Process and Language is derived via inheritance as per RFC1.

# Goal

Open Metadata supports a variety of data-types that are directly editable via the API. However some data-types are inevitably going to become part of a metadata hierarchy that Open Metadata will have no knowledge of and will be unable to edit.

* `jpeg`
* `png`
* `mov`
* `alembic`
* `obj`
* `...`