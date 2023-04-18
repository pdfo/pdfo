project(
    'pdfo',
    'c',
    version: '1.2.2',
    license: 'BSD-3',
    meson_version: '>= 0.64.0',
)

# https://mesonbuild.com/Python-module.html
# The Python module is only available in Meson 0.46.0 or later.
# The pure argument of find_installation() is only available in Meson 0.64.0 or later.
# The dependency() method is only available in Meson 0.53.0 or later.
py_mod = import('python')
py3 = py_mod.find_installation(pure: false)
py3_dep = py3.dependency()

# Compilers
add_languages('fortran', native: false)

subdir('python/pdfo')
