# rundeck-ldap-plugin Rundeck Plugin

This is a WorkflowNodeStep plugin.

## Build

* Using gradle
```
gradle clean build
```

* Using make

```
make clean build
```

## Install

```
python -m pip install python-ldap
```

```
cp build/libs/rundeck-ldap-plugin.zip $RDECK_BASE/libext
```