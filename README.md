[![Build Status](https://travis-ci.org/borodust/bodge-five.svg)](https://travis-ci.org/borodust/bodge-five) [![Build status](https://ci.appveyor.com/api/projects/status/gfwaqhm4h4v8mqqu?svg=true)](https://ci.appveyor.com/project/borodust/bodge-five)


# libfive wrapper for Common Lisp

Wrapper over [`libfive`](https://github.com/libfive/libfive) library.

## Install

### bodge-five
```lisp
;; add cl-bodge distribution into quicklisp
(ql-dist:install-dist "http://bodge.borodust.org/dist/org.borodust.bodge.testing.txt")

;; load the wrapper
(ql:quickload :bodge-five)
```

## Usage

`%libfive` package contains direct bindings to `libfive` API.

## Example

```lisp
(ql:quickload :bodge-five/example)
(libfive.example:render)
```
