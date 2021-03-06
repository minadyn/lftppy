from distutils.core import setup
setup(
    name = 'lftppy',
    packages = ['lftppy'],
    version = '0.1.3',
    description = 'A wrapper around lftp',
    author = 'Danny Im',
    author_email = 'minadyn@gmail.com',
    url = 'https://github.com/minadyn/lftppy',
    download_url = 'https://github.com/minadyn/lftppy/tarball/0.1.3',
    keywords = ['lftp', 'ftp'],
    zip_safe = True,
    install_requires = [
        'pexpect<=3.4',
        'sure',
        'mock',
        'six',
        'pyftpdlib',
    ],
    dependency_links = [
        'git+https://git@github.com/pexpect/pexpect.git@e2ff2f47fc7719ebf4375eec81f996362816bb10#egg=pexpect-3.4'
    ]
)