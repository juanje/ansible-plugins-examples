# Ansible plugins examples

This is a repository of simple examples of how to write plugins for
[Ansible](https://docs.ansible.com/ansible/latest/index.html).
These plugins don't try to be useful or to be used, but rather show
the bare minimum for have a functional [Ansible plugin](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html).

The examples are meant to be **simple**, **small** and **clear**, so
a beginer can understand them and learn from them.

**NOTE**: Keep in mind that this repository is my personal way to learn how to develop Ansible plugins and it's under development. More examples and better explanations/code/details will be added a long the way.

## Considerations

The plugin's code is written in Python. This is a must.

There are different kind of plugins:

* Action plugins
* Cache plugins
* Callback plugins
* Connection plugins
* Filter plugins
* Inventory plugins
* Lookup plugins
* Test plugins
* Vars plugins

Each type of plugin will have its own directory with an example
and some details or explanation.

In some cases (when it would be possible) it'd be two playbooks inside
that directory. One without using the plugin and one using it. This way
it'll be easier to see how the plugin works and what _problem_ it try
to solve.

## License

|                |                                           |
| -------------- | ----------------------------------------- |
| **Author:**    | Juanje Ojeda (<juanje.ojeda@gmail.com>)   |
| **Copyright:** | Copyright (c) 2020 Juanje Ojeda           |
| **License:**   | Apache License, Version 2.0               |

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
