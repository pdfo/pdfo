project(
    'pdfo',
    'c',
    version: '2.0.2',
    license: 'BSD-3',
    meson_version: '>= 0.64.0',
    default_options: [
        'c_std=c99',
        'fortran_std=legacy',
    ],
)

# https://mesonbuild.com/Python-module.html
py_mod = import('python')
py3 = py_mod.find_installation(pure: false)
py3_dep = py3.dependency()

# Compilers
add_languages('fortran', native: false)

subdir('python/pdfo')
