import bz2
import os
import os.path as osp
import platform

import gdown


download_base_dir = osp.expanduser('~/.ace')
download_bin_dir = osp.join(download_base_dir, 'bin')
download_grammar_dir = osp.join(download_base_dir, 'grammar')

ace_versions = (
    '0.9.31',
)
default_ace_version = '0.9.31'
english_resource_grammar_versions = (
    '1214',
    '2018',
)
default_english_resource_grammar_version = '2018'

jacy_urls = {
    '2017': {
        'osx':
        'https://drive.google.com/uc?id=1YdHii_0NNpi_e-Xi_Oa3vL4MQ3yS-b2f',
        'x86-64':
        'https://drive.google.com/uc?id=1-vG00-IsTX1RxJaCcQSKVLK-7wAzEqEe',
    },
}
default_jacy_version = '2017'


def get_ace(ace_version=default_ace_version):
    if ace_version not in ace_versions:
        raise RuntimeError('Could not find a version {} (from versions: {})'
                           .format(ace_version, ", ".join(ace_versions)))
    pf = platform.system()
    base_url = 'http://sweaglesw.org/linguistics/ace/download/ace-{}-{}.tar.gz'
    if pf == 'Windows':
        raise NotImplementedError('Not supported in Windows.')
    elif pf == 'Darwin':
        url = base_url.format(ace_version, 'osx')
        bin_filename = 'ace-{}-{}'.format(ace_version, 'osx')
    else:
        url = base_url.format(ace_version, 'x86-64')
        bin_filename = 'ace-{}-{}'.format(ace_version, 'x86-64')
    bin_filename = osp.join(download_bin_dir, bin_filename)

    name = osp.splitext(osp.basename(url))[0]
    if not osp.exists(bin_filename):
        gdown.cached_download(
            url=url,
            path=osp.join(download_bin_dir, name),
            postprocess=gdown.extractall,
            quiet=True,
        )
        os.rename(
            osp.join(download_bin_dir, 'ace-{}'.format(ace_version), 'ace'),
            bin_filename)
    return bin_filename


def get_english_resource_grammar(
        ace_version=default_ace_version,
        erg_version=default_english_resource_grammar_version):
    """Get Precompiled grammar images.

    """
    if ace_version not in ace_versions:
        raise RuntimeError(
            'Could not find an ACE version {} (from versions: {})'
            .format(ace_version, ", ".join(ace_versions)))
    if erg_version not in english_resource_grammar_versions:
        raise RuntimeError(
            'Could not find an ERG version {} (from versions: {})'
            .format(erg_version, ", ".join(english_resource_grammar_versions)))

    pf = platform.system()
    base_url = 'http://sweaglesw.org/linguistics/ace/download/' \
        'erg-{}-{}-{}.dat.bz2'
    if pf == 'Windows':
        raise NotImplementedError('Not supported in Windows.')
    elif pf == 'Darwin':
        url = base_url.format(erg_version, 'osx', ace_version)
        name = 'erg-{}-{}-{}.dat'.format(erg_version, 'osx', ace_version)
    else:
        url = base_url.format(erg_version, 'x86-64', ace_version)
        name = 'erg-{}-{}-{}.dat'.format(erg_version, 'x86-64', ace_version)

    dat_filename = osp.join(download_grammar_dir, name)
    bz2_file = osp.join(download_grammar_dir, name + '.bz2')
    if not osp.exists(dat_filename):
        gdown.cached_download(
            url=url,
            path=bz2_file,
            quiet=True,
        )
        with open(bz2_file, 'rb') as f:
            data = f.read()
            with open(dat_filename, 'wb') as fw:
                fw.write(bz2.decompress(data))
    return dat_filename


def get_jacy_grammar(ace_version=default_ace_version,
                     jacy_version=default_jacy_version):
    """Get Precompiled grammar images.

    https://github.com/delph-in/jacy
    """
    if ace_version not in ace_versions:
        raise RuntimeError(
            'Could not find an ACE version {} (from versions: {})'
            .format(ace_version, ", ".join(ace_versions)))
    if jacy_version not in jacy_urls.keys():
        raise RuntimeError(
            'Could not find a jacy version {} (from versions: {})'
            .format(jacy_version, ", ".join(jacy_urls.keys())))

    pf = platform.system()
    if pf == 'Windows':
        raise NotImplementedError('Not supported in Windows.')
    elif pf == 'Darwin':
        url = jacy_urls[jacy_version]['osx']
        name = 'jacy-{}-{}-{}.dat'.format(jacy_version, 'osx', ace_version)
    else:
        url = jacy_urls[jacy_version]['x86-64']
        name = 'jacy-{}-{}-{}.dat'.format(jacy_version, 'x86-64', ace_version)
    dat_filename = osp.join(download_grammar_dir, name)
    bz2_file = osp.join(download_grammar_dir, name + '.bz2')
    if not osp.exists(dat_filename):
        gdown.cached_download(
            url=url,
            path=bz2_file,
            quiet=True,
        )
        with open(bz2_file, 'rb') as f:
            data = f.read()
            with open(dat_filename, 'wb') as fw:
                fw.write(bz2.decompress(data))
    return dat_filename
