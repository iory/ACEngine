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
