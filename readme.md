# Eval selection

Evaluates selection as python code with sublime python. This is really rare used
plugin that requires knowledge of sublime api. This plugin can also be used to
study sublime api.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-eval-selection/master/demo/demo.gif "Demo")


### Installation

This plugin is part of sublime-enhanced plugin set. You can install
sublime-enhanced and this plugin will be installed automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov
/sublime-enhanced) package.


### Usage

Select python code and hit keyboard shortcut to evaluate selected code. This
plugin also saves evaluation history so you can reuse previous evaluations again
or create plugins on top of it.


### Commands

| Description             | Keyboard shortcuts | Command palette                        |
|-------------------------|--------------------|----------------------------------------|
| Evaluate selected code  | alt+`              | EvalSelection: Evaluate selection      |
| Show evaluation history | ctrl+alt+`         | EvalSelection: Show evaluation history |