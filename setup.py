from distutils.core import setup


setup(
    name = 'discordslashcommands',
    packages = ['discordslashcommands'],
    version = '1.0.4',
    license='MIT',
    long_description = 'A simple libary to configurate slash commands on discord\n\nSee documentation at https://github.com/mactul/discordslashcommands\n\nThanks to Seniru for reporting and correcting some bugs and imperfections',
    author = 'Macéo Tuloup',
    author_email = 'mactulgames@gmail.com',
    url = 'https://github.com/mactul/discordslashcommands',
    download_url = 'https://github.com/mactul/discordslashcommands.git',
    keywords = ['discord', 'slash', 'custom', 'command', 'commands'],
    install_requires=[
        'discord.py',
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
