(uiop:define-package :%libfive
  (:use))

(claw:c-include "bodge_libfive.h" bodge-five
  :in-package :%libfive
  :standard "c99"
  :includes (:libfive-includes)
  :include-definitions ("libfive_\\w*")
  :rename-symbols (claw:by-removing-prefixes "libfive_"))
