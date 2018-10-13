(claw:c-include "bodge_libfive.h" bodge-five
  :in-package :%libfive
  :standard "c99"
  :includes (:libfive-includes)
  :include-definitions ("libfive_\\w*")
  :rename-symbols (claw:by-removing-prefixes "libfive_"))

(uiop:define-package :libfive
  (:use :cl)
  (:export #:init))
(cl:in-package :libfive)

(defun update-cbv-wrapper ()
  (claw:dump-c-wrapper :%libfive
                       (asdf:system-relative-pathname :bodge-five "lib/wrapper/cbv.c")
                       "libfive_init_bodge_wrapper"))

(defun init (library-path)
  (when (> (%libfive:init-bodge-wrapper (namestring library-path)) 0)
    (error "Failed to initialize librive wrapper")))
