(cl:defpackage :libfive.example
  (:use :cl)
  (:export #:render))
(cl:in-package :libfive.example)

;; Adapted from "libfive_tree_render_slice" test case
(defun render (&optional (svg-path (asdf:system-relative-pathname
                                    :bodge-five/example "local/circle.svg")))
  (claw:with-float-traps-masked ()
    ;; All of these trees are manually managed and must be freed
    ;; In higher-level languages, freeing can be attached to the object's
    ;; destructor and run during garbage collection.
    (let* ((x (%libfive:tree-x))
           (y (%libfive:tree-y))

           (x2 (%libfive:tree-unary (%libfive:opcode-enum "square") x))
           (y2 (%libfive:tree-unary (%libfive:opcode-enum "square") y))
           (r (%libfive:tree-binary (%libfive:opcode-enum "add") x2 y2))

           (one (%libfive:tree-const 1f0))
           (d (%libfive:tree-binary (%libfive:opcode-enum "sub") r one)))

      ;; Select a 2D region to export, then write an SVG

      (claw:c-with ((region %libfive:region2))
        (setf (region :x :lower -2)
              (region :x :upper 2)
              (region :y :lower -2)
              (region :y :upper 2))
        (let ((cs (%libfive:tree-render-slice d region 0f0 10f0)))
          (ensure-directories-exist svg-path)
          (%libfive:tree-save-slice d region 0f0 10f0 (namestring svg-path))

          ;; Finally, clean up all of the intermediate trees
          (%libfive:tree-delete x)
          (%libfive:tree-delete y)
          (%libfive:tree-delete x2)
          (%libfive:tree-delete y2)
          (%libfive:tree-delete r)
          (%libfive:tree-delete one)
          (%libfive:tree-delete d)
          (%libfive:contours-delete cs))))))
