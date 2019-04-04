from setuptools import setup

setup(
    name="NanoV",
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg.pz',
                '**/*.xyz',
                '**/*.txt',
            ],
            'gui_apps': {
                'NanoV': 'main.py'
            },
            'platforms': [
            'manylinux1_x86_64',
            'macosx_10_6_x86_64',
            'win_amd64'],
            'plugins': [
                'pandagl',
                'p3openal_audio',
                'p3ffmpeg',
                'p3fmod_audio',
                'p3ptloader',
                'p3assimp',
                'p3tinydisplay',
                'pandagles',
                'pandagles2',
                'pandadx9'
            ],
            'include_modules' : ['wxpython']
        }
    }
)
