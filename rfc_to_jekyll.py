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

import sublime, sublime_plugin

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
    """Convert `content` into dictionary"""
    gen = blocks(content)

    title = gen.next().strip("# ")
    summary = gen.next()
    properties = gen.next()

    if properties.startswith('!'):
        # This is an optional image
        properties = gen.next()

    # legal = gen.next()

    dproperties = {}
    for prop in properties.splitlines():
        prop = prop.strip("* ")
        key, value = (prop.split(": ", 1) + [''])[:2]
        dproperties[key] = value

    content = DIV.join([g for g in gen])

    result = {'title': title,
              'summary': summary,
              'properties': dproperties,
              # 'legal': legal,
              'content': content}

    return result


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
        header += '%s: %s\n' % (key.lower(), value)
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
        --> This is RFC14
        <-- This is [RFC14](http://path/to/rfc/14)

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
        suffixes = [' ', '\n', ', ', ')']

        for suffix in suffixes:
            source = rfc + suffix
            target = replacement + suffix
            content = content.replace(source, target)

        print "Replacing %s with %s" % (rfc, replacement)

    return content


def perform_string_substitution(content):
    content = substitute_rfc(content)
    return content


class ToJekyllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        Parse currently open file, and write it out to:
        
            /jekyll/##.md

        Where ## represents the number of the RFC

        """

        self.view.run_command('save')

        source_file = self.view.file_name()

        with open(source_file) as f:
            content = f.read()

        content = content.decode('ascii', 'replace')
        # Only allow ASCII
        try:
            content.decode('ascii')
        except UnicodeDecodeError as e:
            # block = unicode(content[(e.end - 10): (e.end + 10)])
            # print dir(e)
            # print 
            # text = content[e.end].decode('UTF-8', 'strict')
            raise ValueError("Found non-ascii characters "
                             "in document %s: %s"
                             % (source_file))

        # Append property derived from `source_file`
        parsed = parse(content)

        basename = os.path.basename(source_file)
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

        # Exclude parts of content marked <draft>
        content = exclude_draft(content)

        # Process string-substitutions
        content = perform_string_substitution(content)

        # Merge original content with jekyll header
        jekyll_header = to_jekyll_header(parsed)
        jekyll_document = jekyll_header + content

        # Construct output path
        root_directory = os.path.dirname(source_file)
        output_directory = os.path.join(root_directory, 'jekyll')
        output_file = '%s.md' % number
        output_path = os.path.join(output_directory, output_file)

        if not os.path.exists(output_directory):
            os.mkdir(output_directory)

        print "Writing Jekyll file %s" % output_path

        with open(output_path, 'w') as f:
            f.write(jekyll_document)

        return True
