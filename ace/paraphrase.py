import subprocess

from ace.data import get_ace
from ace.data import get_english_resource_grammar


def generate_paraphrase(text):
    ace_binary = get_ace()
    erg = get_english_resource_grammar()
    cmd = 'echo "{}" | {} -g {} -1T 2>/dev/null | {} -g {} -e'\
        .format(text, ace_binary, erg, ace_binary, erg, )
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
