import os
from os.path import expanduser, exists, dirname
from shutil import copyfile
from configobj import ConfigObj

def get_config():
    from trash import __file__ as package_root
    package_root = dirname(package_root)
    default_config = os.path.join(package_root, 'trashrc')
    config_dir = expanduser('~/.config/trash/')
    user_config = '{}config'.format(config_dir)
    write_default_config(default_config, user_config)
    return load_config(default_config, user_config)


def write_default_config(source, destination, overwrite=False):
    destination = expanduser(destination)
    if not overwrite and exists(destination):
        return
    config_dir = expanduser(dirname(destination))
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    copyfile(source, destination)


def load_config(default_config, user_config):
    config = ConfigObj()
    config.merge(ConfigObj(default_config, interpolation=False))
    config.merge(ConfigObj(expanduser(user_config), interpolation=False, encoding='utf-8'))
    config.filename = expanduser(user_config)
    return config