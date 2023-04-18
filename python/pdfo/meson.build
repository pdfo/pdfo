# NumPy include directories
incdir_numpy = run_command(py3, [
    '-c',
    'import os; import numpy; print(os.path.relpath(numpy.get_include()))',
], check: true).stdout().strip()
inc_np = include_directories(incdir_numpy)
incdir_f2py = incdir_numpy / '..' / '..' / 'f2py' / 'src'
inc_f2py = include_directories(incdir_f2py)
fortranobject_c = incdir_f2py / 'fortranobject.c'

# Don't use the deprecated NumPy C API
numpy_nodepr_api = '-DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION'

# Dependencies for Fortran
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

# The gethuge module is used by the Fortran solvers but also the Python interface
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

# Names of the Fortran source files for each solver
f77_sources = {
    'uobyqa': ['uobyqa.f', 'uobyqb.f', 'trstep.f', 'lagmax.f'],
    'newuoa': ['newuoa.f', 'newuob.f', 'update.f', 'trsapp.f', 'biglag.f', 'bigden.f'],
    'bobyqa': ['bobyqa.f', 'bobyqb.f', 'prelim.f', 'update.f', 'rescue.f', 'trsbox.f', 'altmov.f'],
    'lincoa': ['lincoa.f', 'lincob.f', 'prelim.f', 'update.f', 'trstep.f', 'getact.f', 'qmstep.f'],
    'cobyla': ['cobyla.f', 'cobylb.f', 'trstlp.f'],
}

foreach classical : [false, true]
    # Paths to the source and signature files
    if classical
        source_path = '../../fsrc/classical/'
        sig_path = '../py_gateways/classical/'
    else
        source_path = '../../fsrc/'
        sig_path = '../py_gateways/'
    endif

    foreach solver, source_filenames : f77_sources
        # Generate the F2PY module for the solver
        if classical
            f_name = 'f' + solver + '_classical'
        else
            f_name = 'f' + solver
        endif
        solver_module = custom_target(
            f_name + 'module',
            output : [f_name + 'module.c', f_name + '-f2pywrappers2.f90'],
            input : sig_path + solver + '-interface.pyf',
            command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
        )

        # Set the sources for the solver
        sources = [solver_module, sig_path + solver + '.f90', '../../fsrc/pdfoconst.F']
        foreach filename : source_filenames
            sources += source_path + solver + '/' + filename
        endforeach

        # Build the Fortran module
        py3.extension_module(
            f_name,
            sources,
            c_args: numpy_nodepr_api,
            dependencies: fortranobject_dep,
            install : true,
            link_language: 'fortran',
            subdir: 'pdfo',
        )
    endforeach
endforeach

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
