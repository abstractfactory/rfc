"""
Convert Abstract Factory RFC markdown-file into
jekyll-compatible markdown.

File is written to a /jekyll parent directory:
    from    -- /spec1.md
    to      -- /jekyll/1.md

"""

import os
import re
import time
import copy

DIV = '\n\n'
SPEC_TEMPLATE = 'http://rfc.abstractfactory.io/spec/{number}'
GITHUB_TEMPLATE = 'https://github.com/abstractfactory/rfc/blob/master/spec/spec{number}.md'


def blocks(content):
    """
    Return a generator of blocks within `content`
    *Blocks are text separated by an empty line.

    """

    for group in content.split(DIV):
        yield group


def parse(content):
    """Convert `content` into dictionary

    Output
        {
            'title': str,
            'summary': str,
            'properties': str,
            'content': str
        }

    """
    
    try:
        gen = blocks(content)

        title = gen.next().strip("# ")
        summary = gen.next()
        properties = gen.next()

        if properties.startswith('!'):
            # This is an optional image
            properties = gen.next()

    except StopIteration:
        # At least these three blocks must exist
        raise ValueError("Document is incorrectly formatted")

    dproperties = {}
    for prop in properties.splitlines():
        prop = prop.strip("* ")
        key, value = (prop.split(": ", 1) + [''])[:2]
        dproperties[key.lower()] = value

    content = DIV.join([g for g in gen])

    result = {'title': title,
              'summary': summary,
              'properties': dproperties,
              'content': content}

    return result


def deparse(parsed):
    """Restore content from `parsed`"""

    # Copy `parsed` so as to not accidentally
    # make modifications to original
    parsed = copy.deepcopy(parsed)

    properties = parsed['properties']

    # Convert properties into block, starting with standards
    fields = []
    syntax = '* %s: %s'
    order = ('name', 'editor', 'related', 'tags', 'state')
    for key in order:
        value = properties.get(key)
        if not value:
            continue
        field = syntax % (key.title(), value)
        fields.append(field)

    # And finishing with miscellaneous
    for key, value in properties.iteritems():
        if key in order:
            continue
        field = syntax % (key.title(), value)
        fields.append(field)

    properties = '\n'.join(fields)
    parsed['properties'] = properties

    blocks = []
    order = ('title', 'summary', 'properties', 'content')
    for key in order:
        blocks.append(parsed[key])
    
    reconstructed = DIV.join(blocks)
    return reconstructed


def get_related(content):
    """Find mentions of 'RFC##' within `content` and return list of matches"""
    related = re.findall(r'RFC\d+', content)
    for rfc in related:
        print "Document was implicitly related to %s" % rfc
    return related


def reconstruct_parsed(parsed):
    """Given `parsed` content, reconstruct content with edited properties"""
    
    # Copy `parsed` so as to not accidentally
    # make modifications to original
    parsed = copy.deepcopy(parsed)

    # print parsed

    properties = parsed['properties']

    # Default state to 'raw'
    if not 'state' in properties:
        properties['state'] = 'raw'

    content = parsed['content']

    # Resolve relations
    relations = properties.get('related') or ''
    explicit_relations = []
    if relations:
        for relation in relations.split(", "):
            explicit_relations.append(relation)

    implicit_relations = get_related(content)
    all_relations = explicit_relations + implicit_relations
    all_relations.sort()

    relations = ', '.join(all_relations)

    properties['related'] = relations

    return parsed


def to_jekyll_header(parsed):
    """Using parsed content, construct Jekyll header"""
    jekyll_properties = {'layout': 'spec'}

    # Disregard content
    parsed.pop('content')

    # Append properties from content
    content_properties = parsed.pop('properties')
    
    jekyll_properties.update(parsed)
    jekyll_properties.update(content_properties)

    header = '---\n'
    for key, value in jekyll_properties.iteritems():
        if not value:
            continue
        header += '%s: %s\n' % (key, value)
    header += '---\n\n'

    return header


def exclude_draft(content):
    pat = re.compile(r'<draft>.*</draft>', re.DOTALL)

    for group in pat.findall(content):
        print "Excluding draft \n%s" % group
        content = ''.join(content.split(group, 1)[0:2])

    return content


def substitute_rfc(content):
    """
    Find lone RFC statements and replace them with full links

    Example
        in  This is RFC14
        out This is [RFC14](http://path/to/rfc/14)

    Expression
        Statement MUST be preceeded by an empty space
        Statement MUST be succeded by number
        Statement MUST be succeded by either empty space OR newline

    """

    pat = re.compile(r'RFC\d+')

    rfcs = []
    for rfc in pat.findall(content):
        rfcs.append(rfc)

    for rfc in rfcs:
        number = rfc[3:]
        link = SPEC_TEMPLATE.format(number=number)
        replacement = "[%s](%s)" % (rfc, link)

        # RFC may exist with multiple suffixes
        suffixes = [' ', '\n', ', ', ')', '.', ':']

        for suffix in suffixes:
            source = rfc + suffix
            target = replacement + suffix
            content = content.replace(source, target)

        print "Replacing %s with %s" % (rfc, replacement)

    return content


def perform_string_substitution(content):
    content = substitute_rfc(content)
    return content


def generate_jekyll_document(path):
    """
    Parse currently open file, and write it out to:
    
        /jekyll/##.md

    Where ## represents the number of the RFC

    """

    with open(path) as f:
        content = f.read()

    # Only allow ASCII
    # TODO: allow unicode..
    content = content.decode('ascii', 'replace')
    try:
        content.decode('ascii')
    except UnicodeDecodeError as e:
        # block = unicode(content[(e.end - 10): (e.end + 10)])
        # print dir(e)
        # print 
        # text = content[e.end].decode('UTF-8', 'strict')
        raise ValueError("Found non-ascii characters "
                         "in document %s: %s"
                         % (path))

    # Append property derived from `path`
    parsed = parse(content)

    basename = os.path.basename(path)
    name, ext = os.path.splitext(basename)
    number = name.strip("spec")
    parsed['number'] = number

    # Append date
    modified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    modified += '+0100'
    parsed['modified'] = modified

    # Append GitHub link
    link = GITHUB_TEMPLATE.format(number=number)
    parsed['link'] = link

    # Reconstruct content based on implicit data
    #   Related
    #   State Default State
    parsed = reconstruct_parsed(parsed)

    # Reconstruct content based on newly reconstructed parsed
    content = deparse(parsed)

    # Exclude parts of content marked <draft>
    content = exclude_draft(content)

    # Process string-substitutions
    content = perform_string_substitution(content)

    # Merge original content with jekyll header
    jekyll_header = to_jekyll_header(parsed)
    jekyll_document = jekyll_header + content

    # Construct output path
    root_directory = os.path.dirname(path)
    output_directory = os.path.join(root_directory, 'jekyll')
    output_file = '%s.md' % number
    output_path = os.path.join(output_directory, output_file)

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    print "Writing Jekyll file %s" % output_path

    with open(output_path, 'w') as f:
        f.write(jekyll_document)

    return True


if __name__ == '__main__':
    demo_content = '''
# This is the title

Followed by a summary.

* Name: And some properties
* Editor: By Marcus <email@af.io>

This is RFC12, and this RFC14
'''

    parsed = parse(demo_content)
    parsed = reconstruct_parsed(parsed)
    print deparse(parsed)