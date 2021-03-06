(asdf:defsystem bodge-five
  :description "Wrapper over libfive"
  :version "1.0.0"
  :author "Pavel Korolev"
  :mailto "dev@borodust.org"
  :license "MIT"
  :depends-on (uiop claw)
  :serial t
  :components ((:file "claw")
               (:static-file "bodge_libfive.h")
               (:module libfive-includes :pathname "lib/libfive/libfive/include/")
               (:module spec)))



(asdf:defsystem bodge-five/example
  :description "Example of bodge-five usage"
  :version "1.0.0"
  :author "Pavel Korolev"
  :mailto "dev@borodust.org"
  :license "MIT"
  :depends-on (five-blob bodge-five)
  :serial t
  :components ((:file "example")))
