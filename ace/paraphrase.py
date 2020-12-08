import subprocess

from ace.data import get_ace
from ace.data import get_english_resource_grammar
from ace.data import get_jacy_grammar


def generate_paraphrase(text, grammar='english', verbose=False):
    if grammar == 'english' or grammar == 'erg':
        grammar = get_english_resource_grammar()
    elif grammar == 'japanese' or grammar == 'jacy':
        grammar = get_jacy_grammar()
    else:
        raise RuntimeError
    ace_binary = get_ace()
    cmd = 'echo "{}" | {} -g {} -1T 2>/dev/null | {} -g {} -e'\
        .format(text, ace_binary, grammar, ace_binary, grammar)
    if verbose:
        print(cmd)
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    proc.wait()
    stdout_data, _ = proc.communicate()
    paraphrase_list = stdout_data.decode('utf8').splitlines()
    paraphrase_list = [paraphrase for paraphrase in paraphrase_list
                       if len(paraphrase) > 0]
    if verbose:
        for s in proc.communicate():
            print(s.decode('utf8'))
    return paraphrase_list
