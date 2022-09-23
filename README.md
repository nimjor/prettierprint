# prettierprint
Python module for clean, human-readable printing of data structures.

## Quickstart
### Install
`pip install prettierprint`

### Usage
Basic:
```python
from prettierprint import print

some_data = {'key': 'value', 'list': [{'name': 'Hello', 'attr_A': 'foo', 'attr_B': 'bar'}, {'name': 'World', 'attr_A': 'bar', 'attr_B': 'foo'}]}

print(some_data)
```
Result:
```
key: value
list:
    - name: Hello
      attr_A: foo
      attr_B: bar
    - name: World
      attr_A: bar
      attr_B: foo
```
### Additional Parameters
When the main object being printed is a list of items, you can define a custom separator:
```python
from prettierprint import print as pretty

list_of_dicts = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}]

pretty(list_of_dicts, top_level_sep='\n-------------------------')
```
Result:
```

-------------------------
userId: 1
id: 1
title: delectus aut autem
completed: False

-------------------------
userId: 1
id: 2
title: quis ut nam facilis et officia qui
completed: False

-------------------------
userId: 1
id: 3
title: fugiat veniam minus
completed: False

-------------------------
userId: 1
id: 4
title: et porro tempora
completed: True
```
Or, pass in a different print function, like `rich.print` for some color:
```python
from rich import print as rprint
from prettierprint import pretty

item = {'type': 'cr2', 'size': '29 MB', 'bytes': 30408704, 'path': '~/Pictures/2022/04/20220401537.cr2', 'created': '2022-04-01', 'modified': '2022-09-14', 'metadata': {'location': {'latitude': -37.3159, 'longitude': 81.1496}}, 'tags': ['landscape', 'spring', 'green']}

pretty(item, print_func=rprint)
```
Result:
<img src="http://github.com/nimjor/prettierprint/blob/main/example_rich.png?raw=true" width="200" />

### Reference
**print**: Pretty prints a Python object
- `data`           - Any    - The object to be clean-printed
- `ind_char`       - str    - The string character for showing hierarchy depth. Default: ' '
- `ind_incr`       - int    - The number of ind_char to use for each new hierarchy level. Default: 6
- `item_sep`       - str    - The string character for separating individual items. Default: '\n'
- `top_level_sep`  - str    - The string to use for visually separating items in a list, set, or tuple.
- `depth`          - int    - The maximum level of hierarchy depth to display. Default: None (all levels)
- `print_func`     - func   - The print function to use. Default is Python's built-in 'print'

**format_output**: Returns a pretty-formatted string
- `data`           - Any    - The object to be clean-printed
- `ind_char`       - str    - The string character for showing hierarchy depth. Default: ' '
- `ind_incr`       - int    - The number of ind_char to use for each new hierarchy level. Default: 6
- `item_sep`       - str    - The string character for separating individual items. Default: '\n'
- `top_level_sep`  - str    - The string to use for visually separating items in a list, set, or tuple.
- `depth`          - int    - The maximum level of hierarchy depth to display. Default: None (all levels)
