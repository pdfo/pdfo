# NumPy include directories
incdir_numpy = run_command(py3, [
    '-c',
    'import os; import numpy; print(os.path.relpath(numpy.get_include()))',
], check: true).stdout().strip()
inc_np = include_directories(incdir_numpy)
# np_dep = declare_dependency(include_directories: inc_np)
incdir_f2py = run_command(py3, [
    '-c',
    'import os; import numpy.f2py; print(os.path.relpath(numpy.f2py.get_include()))',
], check: true).stdout().strip()
inc_f2py = include_directories(incdir_f2py)
fortranobject_c = incdir_f2py / 'fortranobject.c'

# Don't use the deprecated NumPy C API
numpy_nodepr_api = '-DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION'

# Dependencies for Fortran
# fortran_compiler = meson.get_compiler('fortran')
fortranobject_lib = static_library(
    '_fortranobject',
    fortranobject_c,
    c_args: numpy_nodepr_api,
    dependencies: py3_dep,
    include_directories: [inc_np, inc_f2py],
)
fortranobject_dep = declare_dependency(
    link_with: fortranobject_lib,
    include_directories: [inc_np, inc_f2py],
)

gethuge_module = custom_target(
    'gethugemodule',
    output : 'gethugemodule.c',
    input : '../py_gateways/gethuge-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
gethuge = py3.extension_module(
    'gethuge',
    [gethuge_module, '../py_gateways/gethuge.f90', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

uobyqa_module = custom_target(
    'fuobyqamodule',
    output : 'fuobyqamodule.c',
    input : '../py_gateways/uobyqa-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
uobyqa = py3.extension_module(
    'fuobyqa',
    [uobyqa_module, '../py_gateways/uobyqa.f90', '../../fsrc/uobyqa/uobyqa.f', '../../fsrc/uobyqa/uobyqb.f', '../../fsrc/uobyqa/trstep.f', '../../fsrc/uobyqa/lagmax.f', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

newuoa_module = custom_target(
    'fnewuoamodule',
    output : 'fnewuoamodule.c',
    input : '../py_gateways/newuoa-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
newuoa = py3.extension_module(
    'fnewuoa',
    [newuoa_module, '../py_gateways/newuoa.f90', '../../fsrc/newuoa/newuoa.f', '../../fsrc/newuoa/newuob.f', '../../fsrc/newuoa/update.f', '../../fsrc/newuoa/trsapp.f', '../../fsrc/newuoa/biglag.f', '../../fsrc/newuoa/bigden.f', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

bobyqa_module = custom_target(
    'fbobyqamodule',
    output : 'fbobyqamodule.c',
    input : '../py_gateways/bobyqa-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
bobyqa = py3.extension_module(
    'fbobyqa',
    [bobyqa_module, '../py_gateways/bobyqa.f90', '../../fsrc/bobyqa/bobyqa.f', '../../fsrc/bobyqa/bobyqb.f', '../../fsrc/bobyqa/update.f', '../../fsrc/bobyqa/trsbox.f', '../../fsrc/bobyqa/rescue.f', '../../fsrc/bobyqa/prelim.f', '../../fsrc/bobyqa/altmov.f', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

lincoa_module = custom_target(
    'flincoamodule',
    output : 'flincoamodule.c',
    input : '../py_gateways/lincoa-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
lincoa = py3.extension_module(
    'flincoa',
    [lincoa_module, '../py_gateways/lincoa.f90', '../../fsrc/lincoa/lincoa.f', '../../fsrc/lincoa/lincob.f', '../../fsrc/lincoa/update.f', '../../fsrc/lincoa/trstep.f', '../../fsrc/lincoa/prelim.f', '../../fsrc/lincoa/getact.f', '../../fsrc/lincoa/qmstep.f', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

cobyla_module = custom_target(
    'fcobylamodule',
    output : 'fcobylamodule.c',
    input : '../py_gateways/cobyla-interface.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
cobyla = py3.extension_module(
    'fcobyla',
    [cobyla_module, '../py_gateways/cobyla.f90', '../../fsrc/cobyla/cobyla.f', '../../fsrc/cobyla/cobylb.f', '../../fsrc/cobyla/trstlp.f', '../../fsrc/pdfoconst.F'],
    c_args: numpy_nodepr_api,
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'pdfo',
)

py3.install_sources([
    '__init__.py',
    '_bobyqa.py',
    '_cobyla.py',
    '_dependencies.py',
    '_lincoa.py',
    '_newuoa.py',
    '_pdfo.py',
    '_uobyqa.py',
], subdir: 'pdfo')

subdir('tests')
