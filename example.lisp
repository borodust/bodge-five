(cl:defpackage :libfive.example
  (:use :cl)
  (:export #:render))
(cl:in-package :libfive.example)

;; Adapted from "libfive_tree_render_mesh" test case
(defun render (&optional (output-path (asdf:system-relative-pathname
                                       :bodge-five/example "local/result.stl")))
  (libfive:init (bodge-blobs-support:find-loaded-library-name :five-blob :main))
  (claw:with-float-traps-masked ()
    ;; All of these trees are manually managed and must be freed
    ;; In higher-level languages, freeing can be attached to the object's
    ;; destructor and run during garbage collection.
    (let* ((x (%libfive:tree-x))
           (y (%libfive:tree-y))
           (z (%libfive:tree-z))

           (x2 (%libfive:tree-unary (%libfive:opcode-enum "square") x))
           (y2 (%libfive:tree-unary (%libfive:opcode-enum "square") y))
           (z2 (%libfive:tree-unary (%libfive:opcode-enum "square") z))

           (r- (%libfive:tree-binary (%libfive:opcode-enum "add") x2 y2))
           (r (%libfive:tree-binary (%libfive:opcode-enum "add") r- z2))

           (one (%libfive:tree-const 1f0))
           (d (%libfive:tree-binary (%libfive:opcode-enum "sub") r one)))

      ;; Select a 3D region to render
      (claw:c-with ((region %libfive:region3))
        (setf (region :x :lower) -2f0
              (region :x :upper) 2f0
              (region :y :lower) -2f0
              (region :y :upper) 2f0
              (region :z :lower) -2f0
              (region :z :upper) 2f0)
        (let ((tree-str (%libfive:tree-print d)))
          (format t "~&Tree:~&~A"
                  (cffi:foreign-string-to-lisp tree-str))
          (finish-output)
          (claw:free tree-str))

        (ensure-directories-exist output-path)
        (%libfive:tree-save-mesh d region 100f0 (namestring output-path))
        (format t "~&Rendering finished: ~A" output-path)

        ;; Finally, clean up all of the intermediate trees
        (%libfive:tree-delete x)
        (%libfive:tree-delete y)
        (%libfive:tree-delete z)
        (%libfive:tree-delete x2)
        (%libfive:tree-delete y2)
        (%libfive:tree-delete z2)
        (%libfive:tree-delete r-)
        (%libfive:tree-delete r)
        (%libfive:tree-delete one)
        (%libfive:tree-delete d)))))
