__module_name__ = "sjis"
__module_version__ = "1.0"
__module_description__ = "Make your messages kawaii as shit, asshole."

import hexchat
import itertools

sjis_list = {}
sjis_path = '{}{}'.format(hexchat.get_info('configdir'), '\\addons\\sjis.dat')

with open(sjis_path, 'r', encoding='utf8') as f:
    for trigger, emoji in itertools.zip_longest(f, f, fillvalue=''):
        sjis_list[trigger[1:-2]] = emoji[:-1]

def sjis_say_command(word, word_eol, userdata):
    if len(word) < 2:
        return

    trigger = word[1]
    if not trigger in sjis_list:
        return

    emoji = sjis_list[trigger]
    hexchat.command('say {}'.format(emoji))

def sjis_say_hook(word, word_eol, userdata):
    words = []
    got_sjis = False

    for w in word:
        if w != ':' and w.startswith(':') and w.endswith(':'):
            trigger = w[1:-1]
            if trigger in sjis_list:
                words.append(sjis_list[trigger])
                got_sjis = True
            else:
                words.append(w)
        else:
            words.append(w)

    if got_sjis:
        hexchat.command('say {}'.format(' '.join(words)))
        return hexchat.EAT_ALL
    else:
        return hexchat.EAT_NONE

def sjis_list_command(word, word_eol, userdata):
    for trigger, emoji in sjis_list.items():
        hexchat.prnt(':{}: ---> {}'.format(trigger, emoji))

hexchat.hook_command('sjis', sjis_say_command)
hexchat.hook_command('sjislist', sjis_list_command)
hexchat.hook_command('', sjis_say_hook)