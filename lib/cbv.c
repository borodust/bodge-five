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

__CLAW_API void __claw_libfive_tree_eval_d(libfive_vec3* arg2, libfive_tree arg0, libfive_vec3* arg1) {
  libfive_vec3 result = libfive_tree_eval_d(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API float __claw_libfive_tree_eval_f(libfive_tree arg0, libfive_vec3* arg1) {
  float result = libfive_tree_eval_f(arg0, (*arg1));
  return result;
}

__CLAW_API void __claw_libfive_tree_eval_r(libfive_interval* arg2, libfive_tree arg0, libfive_region3* arg1) {
  libfive_interval result = libfive_tree_eval_r(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API libfive_mesh* __claw_libfive_tree_render_mesh(libfive_tree arg0, libfive_region3* arg1, float arg2) {
  libfive_mesh* result = libfive_tree_render_mesh(arg0, (*arg1), arg2);
  return result;
}

__CLAW_API libfive_mesh_coords* __claw_libfive_tree_render_mesh_coords(libfive_tree arg0, libfive_region3* arg1, float arg2) {
  libfive_mesh_coords* result = libfive_tree_render_mesh_coords(arg0, (*arg1), arg2);
  return result;
}

__CLAW_API libfive_pixels* __claw_libfive_tree_render_pixels(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3) {
  libfive_pixels* result = libfive_tree_render_pixels(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API libfive_contours* __claw_libfive_tree_render_slice(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3) {
  libfive_contours* result = libfive_tree_render_slice(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API unsigned char __claw_libfive_tree_save_mesh(libfive_tree arg0, libfive_region3* arg1, float arg2, char* arg3) {
  unsigned char result = libfive_tree_save_mesh(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API void __claw_libfive_tree_save_slice(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3, char* arg4) {
  libfive_tree_save_slice(arg0, (*arg1), arg2, arg3, arg4);
}
#if defined(__cplusplus)
}
#endif
