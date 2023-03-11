#!/usr/bin/env python3
"""PDFO - Powell's Derivative-Free Optimization solvers

PDFO (Powell's Derivative-Free Optimization solvers) is a cross-platform
package providing interfaces for using the late Professor M. J. D. Powell's
derivative-free optimization solvers, including UOBYQA, NEWUOA, BOBYQA, LINCOA,
and COBYLA.

See https://www.pdfo.net for more information.
"""
import importlib
import os
import shutil
import sys

from pkg_resources import parse_version

if sys.version_info < (3, 6):
    raise RuntimeError('Python version >= 3.6 required.')

import builtins
from pathlib import Path

# Remove MANIFEST before importing setuptools to prevent improper updates.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

import setuptools  # noqa
from distutils.command.clean import clean  # noqa
from distutils.command.sdist import sdist  # noqa

# This is a bit hackish: to prevent loading components that are not yet built,
# we set a global variable to endow the main __init__ with with the ability to
# detect whether it is loaded by the setup routine.
BASE_DIR = Path(__file__).resolve(strict=True).parent
sys.path.insert(0, str(BASE_DIR / 'python'))
builtins.__PDFO_SETUP__ = True

import pdfo  # noqa
import pdfo._min_dependencies as min_deps  # noqa

SETUPTOOLS_COMMANDS = {
    'bdist_dumb',
    'bdist_egg',
    'bdist_rpm',
    'bdist_msi',
    'bdist_wheel',
    'bdist_wininst',
    'develop',
    'easy_install',
    'egg_info',
    'install',
    'install_egg_info',
    'upload',
}
if SETUPTOOLS_COMMANDS.intersection(sys.argv[1:]):
    extra_setuptools_args = dict(
        zip_safe=False,
        include_package_data=True,
        extras_require={k: min_deps.tag_to_pkgs[k] for k in ['tests']},
    )
else:
    extra_setuptools_args = {}

DOCLINES = (__doc__ or '').split('\n')


class CleanCommand(clean):
    description = 'Remove build artifacts from the source tree'

    def run(self):
        super().run()

        # Remove setuptools artifact directories and files.
        shutil.rmtree(BASE_DIR / 'build', ignore_errors=True)
        shutil.rmtree(BASE_DIR / 'dist', ignore_errors=True)
        for dirname in BASE_DIR.glob('*.egg-info'):
            shutil.rmtree(dirname)

        # Remove test and coverage cache directories and files.
        shutil.rmtree(BASE_DIR / '.pytest_cache', ignore_errors=True)

        # Remove the 'MANIFEST' file.
        if Path(BASE_DIR, 'MANIFEST').is_file():
            os.unlink(BASE_DIR / 'MANIFEST')

        for dirpath, dirnames, filenames in os.walk(BASE_DIR / 'python'):
            dirpath = Path(dirpath).resolve(strict=True)
            for dirname in dirnames:
                if dirname == '__pycache__':
                    shutil.rmtree(dirpath / dirname)
            for filename in filenames:
                basename, extension = os.path.splitext(filename)
                if extension in ('.dll', '.pyc', '.pyd', '.so', '.mod', '.o'):
                    os.unlink(dirpath / filename)


cmdclass = {'clean': CleanCommand, 'sdist': sdist}


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )

    config.add_subpackage('pdfo', str(BASE_DIR / 'python' / 'pdfo'))

    return config


def check_pkg_status(pkg, min_version):
    message = '{} version >= {} required.'.format(pkg, min_version)
    try:
        module = importlib.import_module(pkg)
        pkg_version = module.__version__  # noqa
        if parse_version(pkg_version) < parse_version(min_version):
            message += ' The current version is {}.'.format(pkg_version)
            raise ValueError(message)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(message)


def setup_package():
    metadata = dict(
        name='pdfo',
        author='Tom M. Ragonneau and Zaikun Zhang',
        author_email='pdfocode@gmail.com',
        maintainer='Tom M. Ragonneau and Zaikun Zhang',
        maintainer_email='pdfocode@gmail.com',
        version=pdfo.__version__,
        packages=['pdfo'],
        package_dir={'': 'python'},
        description=DOCLINES[0],
        long_description='\n'.join(DOCLINES[2:]),
        long_description_content_type='text/plain',
        keywords='Powell Derivative-Free Optimization UOBYQA NEWUOA BOBYQA '
                 'LINCOA COBYLA',
        license='GNU Lesser General Public License v3 or later (LGPLv3+)',
        url='https://www.pdfo.net',
        download_url='https://pypi.org/project/pdfo/#files',
        project_urls={
            'Bug Tracker': 'https://github.com/pdfo/pdfo/issues',
            'Documentation': 'https://www.pdfo.net',
            'Source Code': 'https://github.com/pdfo/pdfo',
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'Programming Language :: Fortran',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        platforms=['Linux', 'macOS', 'Unix', 'Windows'],
        cmdclass=cmdclass,
        python_requires='>=3.6',
        install_requires=min_deps.tag_to_pkgs['install'],
        **extra_setuptools_args
    )

    distutils_commands = {
        'check',
        'clean',
        'egg_info',
        'dist_info',
        'install_egg_info',
        'rotate',
    }
    commands = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
    if all(command in distutils_commands for command in commands):
        from setuptools import setup
    else:
        check_pkg_status('numpy', min_deps.NUMPY_MIN_VERSION)

        from numpy.distutils.core import setup

        if sys.platform == "win32":
            # Fix build with gcc under windows.
            # See https://github.com/jameskermode/f90wrap/issues/96
            from numpy.f2py.cfuncs import includes0
            includes0["setjmp.h"] = '#include <setjmpex.h>'

        metadata['configuration'] = configuration
    setup(**metadata)


if __name__ == '__main__':
    setup_package()
    del builtins.__PDFO_SETUP__  # noqa
