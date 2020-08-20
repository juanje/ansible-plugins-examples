# Filter plugin

Filter plugins manipulate data. They are a feature of [Jinja2](https://palletsprojects.com/p/jinja/)
and are also available in **Jinja2 templates** used by the [template module](https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html).

## Why

There are [plenty of builtin filters in Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html),
but you might want need to do a data convertion that is not supported. Or,
maybe, you are using a very long list of filters that makes your playbook less
readable, so you like to use a single filter with more meaningful name.

## Examples of builtin filters

Here are some examples of filters that you can already use in your playbooks:
```javascript
{{ some_variable | to_json }}
{{ some_variable | to_yaml }}
```

In action:
```yaml
tasks:
  - shell: cat /some/path/to/file.json
    register: result

  - set_fact:
      myvar: "{{ result.stdout | from_json }}"
```

You can chain more than one filter as is shown in this working example:
```yaml
tasks:
  - shell: cat /some/path/to/multidoc-file.yaml
    register: result
  - debug:
      msg: '{{ item }}'
    loop: '{{ result.stdout | from_yaml_all | list }}'
```

The filters can also accept parameters. For example:
```javascript
{{ some_variable | to_nice_yaml(indent=8) }}
```

## This example

You have 2 playbooks so you can compare between using and not using the plugin.
In this case, the plugin will search in a dictionary for the list of **users**
that follow certain criteria, and return a list with those users.

Bowth playbook start with a common dictionary of **users**:
```yaml
vars:
  users:
    - name: margaret
      docker: true
    - name: july
      docker: true
    - name: john
      sudo: without_password
    - name: peter
      sudo: without_password
    - name: anthony
      sudo: with_password
    - name: mary
      app_user: true
```

In order to get the list of users with the key `docker` set as `true` we can user a chain of normal filters:
```yaml
docker_users: "{{ users |
                 selectattr('docker', 'defined') |
                 selectattr('docker', 'equalto', True) |
                 map(attribute='name') |
                 list }}"
```

This does the job, but isn't the most readable code, nor the easiest to maintain.
With our plugin it can be written in a shorter, simpler and more meaninful way:
```yaml
docker_users: "{{ users | list_users('docker') }}"
```

## Considerations

The plugin's code is at the [filter_plugins/list_users.py](filter_plugins/list_users.py) file.

The name of the file doesn't need to be the same of the plugin, it can be anything. But the directory **must** be named `filter_plugins` in order to be found by Ansible.

This example and the test to check the vadility of the results are borrowed from [this article](https://darecode.com/en/blog/how-to-control-our-ansible-repository-with-filters/).