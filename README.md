# Toy Robot
> A toy robot, toy application where the toy robot doesn't fall off the toy table


This project was built using [nbdev](https://github.com/fastai/nbdev) :)

## Install

`pip install toyrobot`

## Documentation

For documentation, refer [here](https://amaarora.github.io/toyrobot/).

## Run 

To run the project in command line (after installation): 

`toyrobot_run --cmd_file_path <path_to_example.txt>`

As an example: 
`toyrobot_run --cmd_file_path ./examples/example1.txt`

```
4,5,WEST
```

To print out outputs after every command add `-- verbose` flag to the command.

## Tests

To run unit as well as integration tests:

`nbdev_test_nbs`
