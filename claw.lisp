(claw:c-include "bodge_libfive.h" bodge-five
  :in-package :%libfive
  :standard "c99"
  :includes (:libfive-includes)
  :include-definitions ("libfive_\\w*")
  :rename-symbols (claw:by-removing-prefixes "libfive_"))

(uiop:define-package :libfive
    (:use :cl))
(cl:in-package :libfive)

(defun update-cbv-wrapper ()
  (claw:dump-c-wrapper :%libfive
                       (asdf:system-relative-pathname :bodge-five "lib/cbv.c")))
