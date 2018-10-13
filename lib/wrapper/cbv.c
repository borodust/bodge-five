#include "bodge_libfive.h"

#if !defined(__CLAW_API)
#  if defined(_WIN32)
#    define __CLAW_API __declspec(dllexport)
#  elif defined(__GNUC__)
#    define __CLAW_API __attribute__((visibility("default")))
#  else
#    define __CLAW_API
#  endif
#endif

#if defined(__cplusplus)
extern C {
#endif

#include <stddef.h>

#ifdef _WIN32
#  include <windows.h>
static HMODULE ___claw_module;

static int ___claw_init_wrapper(const char* module_name) {
  int wide_string_length = MultiByteToWideChar(CP_UTF8, 0, module_name, -1, NULL, 0);
  wchar_t* wide_module_name = calloc(wide_string_length, sizeof(wchar_t));
  MultiByteToWideChar(CP_UTF8, 0, module_name, -1, wide_module_name, wide_string_length);
  ___claw_module = LoadLibraryW(wide_module_name);
  free(wide_module_name);
  return ___claw_module != NULL;
}

static void ___claw_close_wrapper(void) {
  if(___claw_module != NULL) {
    FreeLibrary(___claw_module);
    ___claw_module = NULL;
  }
}
#else
#  include <dlfcn.h>
static void* ___claw_module;

static int ___claw_init_wrapper(const char* module_name) {
  ___claw_module = dlopen(module_name, RTLD_NOW | RTLD_GLOBAL);
  return ___claw_module != NULL;
}

static void ___claw_close_wrapper(void) {
  if(___claw_module != NULL) {
    dlclose(___claw_module);
    ___claw_module = NULL;
  }
}
#endif

static void* claw_get_proc_addr(const char *name) {
  if(___claw_module == NULL) {
    return NULL;
  }

#ifdef _WIN32
  return (void*) GetProcAddress(___claw_module, name);
#else
  return dlsym(___claw_module, name);
#endif
}

static libfive_vec3 (*__v_claw_libfive_tree_eval_d)(libfive_tree, libfive_vec3);
static float (*__v_claw_libfive_tree_eval_f)(libfive_tree, libfive_vec3);
static libfive_interval (*__v_claw_libfive_tree_eval_r)(libfive_tree, libfive_region3);
static libfive_mesh* (*__v_claw_libfive_tree_render_mesh)(libfive_tree, libfive_region3, float);
static libfive_mesh_coords* (*__v_claw_libfive_tree_render_mesh_coords)(libfive_tree, libfive_region3, float);
static libfive_pixels* (*__v_claw_libfive_tree_render_pixels)(libfive_tree, libfive_region2, float, float);
static libfive_contours* (*__v_claw_libfive_tree_render_slice)(libfive_tree, libfive_region2, float, float);
static libfive_contours3* (*__v_claw_libfive_tree_render_slice3)(libfive_tree, libfive_region2, float, float);
static unsigned char (*__v_claw_libfive_tree_save_mesh)(libfive_tree, libfive_region3, float, char*);
static void (*__v_claw_libfive_tree_save_slice)(libfive_tree, libfive_region2, float, float, char*);

__CLAW_API int libfive_init_bodge_wrapper(const char *name) {
  if(___claw_init_wrapper(name)) {

    __v_claw_libfive_tree_eval_d = claw_get_proc_addr("libfive_tree_eval_d");
    __v_claw_libfive_tree_eval_f = claw_get_proc_addr("libfive_tree_eval_f");
    __v_claw_libfive_tree_eval_r = claw_get_proc_addr("libfive_tree_eval_r");
    __v_claw_libfive_tree_render_mesh = claw_get_proc_addr("libfive_tree_render_mesh");
    __v_claw_libfive_tree_render_mesh_coords = claw_get_proc_addr("libfive_tree_render_mesh_coords");
    __v_claw_libfive_tree_render_pixels = claw_get_proc_addr("libfive_tree_render_pixels");
    __v_claw_libfive_tree_render_slice = claw_get_proc_addr("libfive_tree_render_slice");
    __v_claw_libfive_tree_render_slice3 = claw_get_proc_addr("libfive_tree_render_slice3");
    __v_claw_libfive_tree_save_mesh = claw_get_proc_addr("libfive_tree_save_mesh");
    __v_claw_libfive_tree_save_slice = claw_get_proc_addr("libfive_tree_save_slice");

    ___claw_close_wrapper();
    return 0;
  }
  return 1;
}


__CLAW_API void __claw_libfive_tree_eval_d(libfive_vec3* arg2, libfive_tree arg0, libfive_vec3* arg1) {
  libfive_vec3 result = __v_claw_libfive_tree_eval_d(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API float __claw_libfive_tree_eval_f(libfive_tree arg0, libfive_vec3* arg1) {
  float result = __v_claw_libfive_tree_eval_f(arg0, (*arg1));
  return result;
}

__CLAW_API void __claw_libfive_tree_eval_r(libfive_interval* arg2, libfive_tree arg0, libfive_region3* arg1) {
  libfive_interval result = __v_claw_libfive_tree_eval_r(arg0, (*arg1));
  (*arg2) = result;
}

__CLAW_API libfive_mesh* __claw_libfive_tree_render_mesh(libfive_tree arg0, libfive_region3* arg1, float arg2) {
  libfive_mesh* result = __v_claw_libfive_tree_render_mesh(arg0, (*arg1), arg2);
  return result;
}

__CLAW_API libfive_mesh_coords* __claw_libfive_tree_render_mesh_coords(libfive_tree arg0, libfive_region3* arg1, float arg2) {
  libfive_mesh_coords* result = __v_claw_libfive_tree_render_mesh_coords(arg0, (*arg1), arg2);
  return result;
}

__CLAW_API libfive_pixels* __claw_libfive_tree_render_pixels(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3) {
  libfive_pixels* result = __v_claw_libfive_tree_render_pixels(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API libfive_contours* __claw_libfive_tree_render_slice(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3) {
  libfive_contours* result = __v_claw_libfive_tree_render_slice(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API libfive_contours3* __claw_libfive_tree_render_slice3(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3) {
  libfive_contours3* result = __v_claw_libfive_tree_render_slice3(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API unsigned char __claw_libfive_tree_save_mesh(libfive_tree arg0, libfive_region3* arg1, float arg2, char* arg3) {
  unsigned char result = __v_claw_libfive_tree_save_mesh(arg0, (*arg1), arg2, arg3);
  return result;
}

__CLAW_API void __claw_libfive_tree_save_slice(libfive_tree arg0, libfive_region2* arg1, float arg2, float arg3, char* arg4) {
  __v_claw_libfive_tree_save_slice(arg0, (*arg1), arg2, arg3, arg4);
}


#if defined(__cplusplus)
}
#endif
