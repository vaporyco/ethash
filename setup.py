#!/usr/bin/env python
import os
from distutils.core import setup, Extension
sources = [
    'src/python/core.c',
    'src/libvapash/io.c',
    'src/libvapash/internal.c',
    'src/libvapash/sha3.c']
if os.name == 'nt':
    sources += [
        'src/libvapash/util_win32.c',
        'src/libvapash/io_win32.c',
        'src/libvapash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libvapash/io_posix.c'
    ]
depends = [
    'src/libvapash/vapash.h',
    'src/libvapash/compiler.h',
    'src/libvapash/data_sizes.h',
    'src/libvapash/endian.h',
    'src/libvapash/vapash.h',
    'src/libvapash/io.h',
    'src/libvapash/fnv.h',
    'src/libvapash/internal.h',
    'src/libvapash/sha3.h',
    'src/libvapash/util.h',
]
pyvapash = Extension('pyvapash',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='pyvapash',
    author="Matthew Wampler-Doty",
    author_email="matthew.wampler.doty@gmail.com",
    license='GPL',
    version='0.1.23',
    url='https://github.com/vaporyco/vapash',
    download_url='https://github.com/vaporyco/vapash/tarball/v23',
    description=('Python wrappers for vapash, the ethereum proof of work'
                 'hashing function'),
    ext_modules=[pyvapash],
)
