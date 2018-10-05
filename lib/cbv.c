#include "bodge_libfive.h"
#ifndef __CLAW_API
#  if defined(_WIN32)
#    define __CLAW_API __declspec(dllexport)
#  elif defined(__GNUC__)
#    define __CLAW_API __attribute__((visibility("default")))
#  else
#    define __CLAW_API
#  endif
#endif
#if defined(__cplusplus)
extern "C" {
#endif

__CLAW_API void __claw_libfive_tree_eval_d(struct libfive_vec3* arg2, libfive_tree arg0, struct libfive_vec3* arg1) {
  struct libfive_vec3 result = libfive_tree_eval_d(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API float __claw_libfive_tree_eval_f(libfive_tree arg0, struct libfive_vec3* arg1) {
  float result = libfive_tree_eval_f(arg0, (*arg1));
  return result;
}

__CLAW_API void __claw_libfive_tree_eval_r(struct libfive_interval* arg2, libfive_tree arg0, struct libfive_region3* arg1) {
  struct libfive_interval result = libfive_tree_eval_r(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API void __claw_libfive_tree_save_slice(libfive_tree arg0, struct libfive_region2* arg1, float arg2, float arg3, char* arg4) {
  libfive_tree_save_slice(arg0, (*arg1), arg2, arg3, arg4);
}
#if defined(__cplusplus)
}
#endif
