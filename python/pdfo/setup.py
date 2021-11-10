from pathlib import Path

numpy_nodepr_api = {
    'define_macros': [('NPY_NO_DEPRECATED_API', 'NPY_1_9_API_VERSION')],
}


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    config = Configuration('pdfo', parent_package, top_path)

    base_dir = Path(__file__).resolve(strict=True).parent.parent.parent
    pdfo_dir = Path(base_dir, 'python')
    gtw_dir = Path(pdfo_dir, 'py_gateways')
    gtw_c_dir = Path(gtw_dir, 'classical')
    fsrc_dir = Path(base_dir, 'fsrc')
    fsrc_c_dir = Path(fsrc_dir, 'classical')

    sources = [gtw_dir / 'pdfoconst-interface.pyf', fsrc_dir / 'pdfoconst.F']
    config.add_extension('pdfoconst',
                         sources=list(map(str, sources)),
                         include_dirs=[get_numpy_include_dirs()],
                         **numpy_nodepr_api)

    sources = [gtw_dir / 'gethuge-interface.pyf', gtw_dir / 'gethuge.f90']
    config.add_extension('gethuge',
                         sources=list(map(str, sources)),
                         include_dirs=[get_numpy_include_dirs()],
                         **numpy_nodepr_api)

    for alg in ['uobyqa', 'newuoa', 'bobyqa', 'lincoa', 'cobyla']:
        fsrc = Path(fsrc_dir, alg)
        sources = [gtw_dir / f'{alg}-interface.pyf', gtw_dir / f'{alg}.f90']
        sources.extend(fsrc.glob('*.f'))
        config.add_extension(f'f{alg}',
                             sources=list(map(str, sources)),
                             include_dirs=[get_numpy_include_dirs()],
                             **numpy_nodepr_api)

        fsrc = Path(fsrc_c_dir, alg)
        sources = [gtw_c_dir / f'{alg}-interface.pyf', gtw_c_dir / f'{alg}.f90']
        sources.extend(fsrc.glob('*.f'))
        config.add_extension(f'f{alg}_classical',
                             sources=list(map(str, sources)),
                             include_dirs=[get_numpy_include_dirs()],
                             **numpy_nodepr_api)

    config.add_data_dir('tests')

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
