import subprocess

from ace.data import get_ace
from ace.data import get_english_resource_grammar
from ace.data import get_jacy_grammar


def generate_paraphrase(text, grammar='english'):
    if grammar == 'english':
        grammar = get_english_resource_grammar()
    elif grammar == 'japanese' or grammar == 'jacy':
        grammar = get_jacy_grammar()
    else:
        raise RuntimeError
    ace_binary = get_ace()
    cmd = 'echo "{}" | {} -g {} -1T 2>/dev/null | {} -g {} -e'\
        .format(text, ace_binary, grammar, ace_binary, grammar)
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    proc.wait()
    paraphrase_list = proc.communicate()[0].decode('utf8').split('\n')
    paraphrase_list = [paraphrase for paraphrase in paraphrase_list
                       if len(paraphrase) > 0]
    return paraphrase_list
