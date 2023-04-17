import sysconfig


def get_platform():
    platform = sysconfig.get_platform()
    platform_split = platform.split('-')
    architecture = platform_split[-1]
    if architecture == 'win32':
        platform = "win-32"
    elif architecture in ['universal2', 'intel']:
        platform = f'macosx-{platform.uname().machine}'
    elif len(platform_split) > 2:
        platform = f'{platform_split[0]}-{architecture}'
    return platform
