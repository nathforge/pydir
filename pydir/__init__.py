#!/usr/bin/env python


"""
Pydir is mkdir for Python modules.

Example:
    $ pydir -v myproject/module/etc
    Created directory myproject/module/etc
    Created file myproject/__init__.py
    Created file myproject/module/__init__.py
    Created file myproject/module/etc/__init__.py
"""


from optparse import OptionParser, make_option
import os
import os.path
import sys


def main():
    usage = '%prog path [path2] [path3] [pathN]\n\n' + __doc__.strip()
    parser = OptionParser(usage=usage, option_list=(
        make_option('-v', '--verbose', default=False, action='store_true'),
    ))
    
    options, args = parser.parse_args()
    
    if len(args) == 0:
        parser.error('No paths given.')
    
    output = sys.stdout if options.verbose else None
    
    for index, path in enumerate(args):
        path = path.replace('.', os.path.sep)
        
        if output and index > 0:
            output.write('\n')
        
        try:
            pydir(path, output=output)
        except BaseException, exc:
            print 'Couldn\'t create %s: %s' % (path, exc,)


def pydir(path, output=None):
    """
    Create a directory structure for a Python module, including __init__.py
    files. Converts existing directories into modules.
    """
    
    def info(line):
        if output:
            output.write(line)
            output.write('\n')
    
    try:
        os.makedirs(path)
    except (OSError, IOError), exc:
        if not os.path.isdir(path):
            info('Path already exists: %s' % path)
        else:
            raise
    else:
        info('Created directory %s' % path)
    
    segments = path.split(os.path.sep)
    for i in xrange(len(segments)):
        init_filename = os.path.sep.join(segments[:i+1] + ['__init__.py'])
        if not os.path.isfile(init_filename):
            try:
                open(init_filename, 'w').close()
            except (OSError, IOError), exc:
                raise
            else:
                info('Created file %s' % (init_filename,))
        else:
            info('File already exists: %s' % (init_filename,))


if __name__ == '__main__':
    main()

