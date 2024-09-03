# LINKED LISTS

## GOAL OF PROJECT

- Self study project to improve my knowledge on data structures
- Treat it as much as a real life application as possible
- Stepping out of my comfort zone by using a programming language quite unfamiliar to me

### key learning concepts

- Brush up on the basic data structre LinkedList which is often ignored in FE development
- Syntax for unit testing and folder structure in Pyhton
- Basic Docker knowledge to create smooth scripts
- Improve on testing knowledge to assure robust testing

## FOLDER STRUCTURE

```
📁 list
    📄 SingleList.py
    📄 DoubeList.py
📁 test
    📄 test_SingleList.py
    📄 test_DoubeList.py
```

## MEMORY ALLOCATED TO LISTS

1. `NEXT` = link to next node = N
2. `DATA` = data = N
3. `HEAD` = head of list = 1
4. `TAIL` = tail of list = 1

### Total

\(2N + 2\)

## TESTING

### Concept

### How to set up

1. build with docker

```bash
docker build -t list-test .
```

2. Execute tests

```bash
docker run -t list-test
```
