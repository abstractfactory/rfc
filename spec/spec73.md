# cQuery

Adopting jQuery for traversal of content hierarchies.

* Name: http://rfc.abstractfactory.io/spec/73
* Editor: Marcus Ottosson <marcus@abstractfactory.io>
* State: raw

Copyright and Language can be found in RFC1

# Change Process

This document is governed by the [Consensus-Oriented Specification System](http://www.digistan.org/spec:1/COSS) (COSS).

# Goal

Mimic the HTML Document Object Model (DOM), by storing class, id and various selectors with folders, and access it via cQuery which is based on jQuery.

```html
<!--HTML-->
<div class='container' id='MyContainer'></div>
```

```javascript
// jQuery
$('.container').on('click', function(){})
```

Users can then get all folders of a specific class, or group of classes. By ID, or group of IDs.

Each folder may have multiple classes, but only one ID per hierarchy.

```bash
/home/dojo/asset.class
/home/marcus/asset.class
/home/marcus/character.class
/home/marcus/lowres.class
/home/marcus/funky_bro.id
```

Then, when getting all content of class "asset", will return:

```bash
/home/marcus
/home/dojo
```

# Some history

In traditional object-oriented programming languages, objects - such as buttons - are defined with speficic behaviour, potentially subclassed and finally put into an object hierarchy. The object maintains its behaviour from class and superclass descriptions.

In HTML, objects - such as buttons - carry no descriptions other than what has been pre-defined by browsers, and is simply stored into an object hierarchy as-is. Then, behvaiour is applied through the use of JavaScript and mass-selectors.

```javascript
// Select all buttons, and apply handler to event
$('button').on('click', my_behaviour)
```

In a similar fashion, content, the files and folders on our file-systems do not carry descriptions other than what has been pre-defined by the file-system itself. A folder is a folder and there are no alternatives.

Content and HTML share this attribute, so it may make sense to also apply tactics born to handle vast and deeply nested HTML to vast and deeply nested content hierarchies.

```javascript
// Select all folders, and apply handler to event
$('folder').on('enter', my_behaviour)

// Select all folders of class "asset" and "lowres" and apply handler to event
$('folder.asset.lowres').on('publish', validate)
```

# COM Modifications

Like with the DOM, COM must support being modified. Why would one want to modify a folder-hierarchy via a script? Like with Javascript and the DOM, modifications wouldn't actually modify the physical content on disk, but rather the in-memory mirror of it. Again like with the DOM, this may be useful when for instance you have a collection of content in one place that you would like to display together with content from elsewhere.