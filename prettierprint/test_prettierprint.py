import argparse
from typing import NamedTuple
from prettierprint import print as cleanprint

class One(NamedTuple):
    a: str=None
    b: int=12
    c: str='C'

class Two:
    foo = None
    bar = None
    def __init__(self, foo, bar, **kwargs):
        self.foo = foo
        self.bar = bar
        for k, v in kwargs.items():
            self.__setattr__(k, v)

#########################
#       Test data       #
#########################
one = One()
test = {
    'user': 'jordan',
    'name': 'nimjor',
    'attrs': [
        'foo',
        'bar',
        {'accountExpires': '2022-09-15'},
        {'age': 34},
        {'something': (1, 2, 3, 4, 'five')}
    ],
    'another': one
}

test2 = [
    {'name': 'jordan', 'age': 34, 'attrs': ('abc', 'foo' 'bar')},
    {'name': 'tester', 'age': 50, 'attrs': ('test', 'def'), 'opts': {'some_list': ['item1', 'item2', {'alpha': 'A', 'beta': 'B', 'gamma': Two('q', 'w')}]}},
    Two('abc', 'def', NUMBER=1234, pi=3.14)
]

some_data = {
    'key': 'value', 
    'list': [
        {
            'name': 'Hello',
            'attr_A': 'foo', 
            'attr_B': 'bar'
        },
        {
            'name': 'World',
            'attr_A': 'bar',
            'attr_B': 'foo'
        }
    ]
}
##### End test data #####


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indent-char', '-i', type=str, action='store',
                        help='The character used for indenting hierarchy levels')
    args = parser.parse_args()
    if args.indent_char:
        cleanprint(test2, ind_char=args.indent_char, item_sep="^^^", top_level_sep="\n***********************************", depth=4, print_func=print)
    else:
        cleanprint(some_data)