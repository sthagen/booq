# [[[fill git_describe()]]]
__version__ = '2022.8.9+parent.389e71f4'
# [[[end]]] (checksum: 17d4e70a84916ab90bcfcc82821cdea7)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
