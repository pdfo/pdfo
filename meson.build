project(
    'pdfo',
    'c',
    version: '1.2.1',
    license: 'BSD-3',
    meson_version: '>= 0.64.0',
    default_options: [
        'c_std=c99',
        'fortran_std=legacy',
    ],
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
# cc = meson.get_compiler('c')
# m_dep = cc.find_library('m', required : false)
# if m_dep.found()
#     add_project_link_arguments('-lm', language : 'c')
# endif

subdir('python/pdfo')
