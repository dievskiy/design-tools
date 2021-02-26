import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    POTRACE_PATH = os.environ.get('POTRACE_PATH') or '/Users/sublime/Downloads/Browser/pt/potrace'
