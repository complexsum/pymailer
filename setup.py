"""A setuptools based setup module.
"""

# Always prefer setuptools over distutils
import setuptools
import pathlib
import shutil

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# https://packaging.python.org/en/latest/single_source_version.html
about = {}
exec((here / 'pymailer/__about__.py').read_text(encoding='utf-8'), globals(), about)


dist_path = here / 'dist'
if dist_path.exists():
    shutil.rmtree(dist_path)


setuptools.setup(
    name='py3mailer',
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',
    url='https://github.com/complexsum/pymailer',
    author='Shubham Sharma',
    author_email='shubhamjsharma10@gmail.com',
    license='Apache 2.0',

    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',

        'Operating System :: OS Independent',
        'Typing :: Typed',
    ],


    keywords='email, python email, python smtp, python send emails, smtp',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={'': '.'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=setuptools.find_packages(include=['pymailer', 'pymailer.*'], exclude=['doc']),  # Required

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip pip install -i https://test.pypi.org/simple/ py3mailer==1.0.4install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.6, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],  # Optional

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/complexsum/pymailer/issues',
        'Source': 'https://github.com/complexsum/pymailer',
    },
)