[{"tag":"struct","ns":0,"name":"libfive_interval","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:26:16","bitSize":64,"bitAlignment":32,"fields":[{"tag":"field","name":"lower","bitOffset":0,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"upper","bitOffset":32,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}}]},{"tag":"typedef","ns":0,"name":"libfive_interval","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:26:64","type":{"tag":":struct","name":"libfive_interval","id":9}},{"tag":"struct","ns":0,"name":"libfive_region2","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:31:16","bitSize":128,"bitAlignment":32,"fields":[{"tag":"field","name":"X","bitOffset":0,"bitSize":64,"bitAlignment":32,"type":{"tag":"libfive_interval"}},{"tag":"field","name":"Y","bitOffset":64,"bitSize":64,"bitAlignment":32,"type":{"tag":"libfive_interval"}}]},{"tag":"typedef","ns":0,"name":"libfive_region2","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:31:61","type":{"tag":":struct","name":"libfive_region2","id":10}},{"tag":"struct","ns":0,"name":"libfive_region3","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:36:16","bitSize":192,"bitAlignment":32,"fields":[{"tag":"field","name":"X","bitOffset":0,"bitSize":64,"bitAlignment":32,"type":{"tag":"libfive_interval"}},{"tag":"field","name":"Y","bitOffset":64,"bitSize":64,"bitAlignment":32,"type":{"tag":"libfive_interval"}},{"tag":"field","name":"Z","bitOffset":128,"bitSize":64,"bitAlignment":32,"type":{"tag":"libfive_interval"}}]},{"tag":"typedef","ns":0,"name":"libfive_region3","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:36:64","type":{"tag":":struct","name":"libfive_region3","id":11}},{"tag":"struct","ns":0,"name":"libfive_vec2","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:41:16","bitSize":64,"bitAlignment":32,"fields":[{"tag":"field","name":"x","bitOffset":0,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"y","bitOffset":32,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}}]},{"tag":"typedef","ns":0,"name":"libfive_vec2","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:41:50","type":{"tag":":struct","name":"libfive_vec2","id":12}},{"tag":"struct","ns":0,"name":"libfive_vec3","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:46:16","bitSize":96,"bitAlignment":32,"fields":[{"tag":"field","name":"x","bitOffset":0,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"y","bitOffset":32,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"z","bitOffset":64,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}}]},{"tag":"typedef","ns":0,"name":"libfive_vec3","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:46:53","type":{"tag":":struct","name":"libfive_vec3","id":13}},{"tag":"struct","ns":0,"name":"libfive_vec4","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:51:16","bitSize":128,"bitAlignment":32,"fields":[{"tag":"field","name":"x","bitOffset":0,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"y","bitOffset":32,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"z","bitOffset":64,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"field","name":"w","bitOffset":96,"bitSize":32,"bitAlignment":32,"type":{"tag":":float","bitSize":32,"bitAlignment":32}}]},{"tag":"typedef","ns":0,"name":"libfive_vec4","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:51:56","type":{"tag":":struct","name":"libfive_vec4","id":14}},{"tag":"struct","ns":0,"name":"libfive_tri","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:57:16","bitSize":96,"bitAlignment":32,"fields":null},{"tag":"typedef","ns":0,"name":"libfive_tri","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:57:56","type":{"tag":":struct","name":"libfive_tri","id":15}},{"tag":"struct","ns":0,"name":"libfive_contour","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:63:16","bitSize":128,"bitAlignment":64,"fields":[{"tag":"field","name":"pts","bitOffset":0,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":"libfive_vec2"}}}]},{"tag":"typedef","ns":0,"name":"libfive_contour","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:66:3","type":{"tag":":struct","name":"libfive_contour","id":16}},{"tag":"struct","ns":0,"name":"libfive_contours","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:72:16","bitSize":128,"bitAlignment":64,"fields":[{"tag":"field","name":"cs","bitOffset":0,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":"libfive_contour"}}}]},{"tag":"typedef","ns":0,"name":"libfive_contours","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:75:3","type":{"tag":":struct","name":"libfive_contours","id":17}},{"tag":"struct","ns":0,"name":"libfive_mesh","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:81:16","bitSize":192,"bitAlignment":64,"fields":[{"tag":"field","name":"verts","bitOffset":0,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":"libfive_vec3"}}},{"tag":"field","name":"tris","bitOffset":64,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":"libfive_tri"}}}]},{"tag":"typedef","ns":0,"name":"libfive_mesh","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:86:3","type":{"tag":":struct","name":"libfive_mesh","id":18}},{"tag":"struct","ns":0,"name":"libfive_mesh_coords","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:95:16","bitSize":256,"bitAlignment":64,"fields":[{"tag":"field","name":"verts","bitOffset":0,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":"libfive_vec3"}}}]},{"tag":"typedef","ns":0,"name":"libfive_mesh_coords","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:100:3","type":{"tag":":struct","name":"libfive_mesh_coords","id":19}},{"tag":"struct","ns":0,"name":"libfive_pixels","id":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:106:16","bitSize":128,"bitAlignment":64,"fields":[{"tag":"field","name":"pixels","bitOffset":0,"bitSize":64,"bitAlignment":64,"type":{"tag":":pointer","type":{"tag":":_Bool","bitSize":8,"bitAlignment":8}}}]},{"tag":"typedef","ns":0,"name":"libfive_pixels","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:110:3","type":{"tag":":struct","name":"libfive_pixels","id":20}},{"tag":"function","name":"libfive_contours_delete","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:117:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"cs","type":{"tag":":pointer","type":{"tag":"libfive_contours"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"libfive_mesh_delete","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:122:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"m","type":{"tag":":pointer","type":{"tag":"libfive_mesh"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"libfive_pixels_delete","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:127:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"ps","type":{"tag":":pointer","type":{"tag":"libfive_pixels"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"libfive_opcode_enum","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:133:5","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"op","type":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"function","name":"libfive_opcode_args","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:139:5","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"op","type":{"tag":":int","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"libfive_tree","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:148:15","type":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"typedef","ns":0,"name":"libfive_id","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:149:15","type":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"typedef","ns":0,"name":"libfive_archive","location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:150:15","type":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"function","name":"libfive_tree_x","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:156:14","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_y","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:161:14","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_z","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:166:14","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_var","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:171:14","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_is_var","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:176:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}}],"returnType":{"tag":":_Bool","bitSize":8,"bitAlignment":8}},{"tag":"function","name":"libfive_tree_const","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:181:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"f","type":{"tag":":float","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_get_const","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:187:7","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"success","type":{"tag":":pointer","type":{"tag":":_Bool","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"function","name":"libfive_tree_constant_vars","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:193:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_nonary","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:199:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"op","type":{"tag":":int","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_unary","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:205:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"op","type":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"a","type":{"tag":"libfive_tree"}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_binary","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:211:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"op","type":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"a","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"b","type":{"tag":"libfive_tree"}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_id","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:217:13","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}}],"returnType":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"function","name":"libfive_tree_eval_f","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:223:7","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"p","type":{"tag":"libfive_vec3"}}],"returnType":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"function","name":"libfive_tree_eval_r","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:230:18","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"r","type":{"tag":"libfive_region3"}}],"returnType":{"tag":"libfive_interval"}},{"tag":"function","name":"libfive_tree_eval_d","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:236:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"p","type":{"tag":"libfive_vec3"}}],"returnType":{"tag":"libfive_vec3"}},{"tag":"function","name":"libfive_tree_eq","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:241:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"a","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"b","type":{"tag":"libfive_tree"}}],"returnType":{"tag":":_Bool","bitSize":8,"bitAlignment":8}},{"tag":"function","name":"libfive_tree_delete","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:247:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"ptr","type":{"tag":"libfive_tree"}}],"returnType":{"tag":":void"}},{"tag":"function","name":"libfive_tree_save","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:251:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"ptr","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"filename","type":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":":_Bool","bitSize":8,"bitAlignment":8}},{"tag":"function","name":"libfive_tree_load","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:254:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"filename","type":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_remap","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:258:14","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"p","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"x","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"y","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"z","type":{"tag":"libfive_tree"}}],"returnType":{"tag":"libfive_tree"}},{"tag":"function","name":"libfive_tree_print","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:267:7","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"t","type":{"tag":"libfive_tree"}}],"returnType":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}},{"tag":"function","name":"libfive_tree_render_slice","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:282:19","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region2"}},{"tag":"parameter","name":"z","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":":pointer","type":{"tag":"libfive_contours"}}},{"tag":"function","name":"libfive_tree_save_slice","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:291:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region2"}},{"tag":"parameter","name":"z","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"f","type":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"libfive_tree_render_mesh","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:305:15","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region3"}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":":pointer","type":{"tag":"libfive_mesh"}}},{"tag":"function","name":"libfive_tree_render_mesh_coords","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:312:22","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region3"}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":":pointer","type":{"tag":"libfive_mesh_coords"}}},{"tag":"function","name":"libfive_tree_save_mesh","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:322:6","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region3"}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"f","type":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}],"returnType":{"tag":":_Bool","bitSize":8,"bitAlignment":8}},{"tag":"function","name":"libfive_tree_render_pixels","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:330:17","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"tree","type":{"tag":"libfive_tree"}},{"tag":"parameter","name":"R","type":{"tag":"libfive_region2"}},{"tag":"parameter","name":"z","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"parameter","name":"res","type":{"tag":":float","bitSize":32,"bitAlignment":32}}],"returnType":{"tag":":pointer","type":{"tag":"libfive_pixels"}}},{"tag":"function","name":"libfive_git_version","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:338:13","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}},{"tag":"function","name":"libfive_git_revision","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:344:13","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}},{"tag":"function","name":"libfive_git_branch","ns":0,"location":"C:\/msys64\/home\/appveyor\/quicklisp\/local-projects\/bodge-five\/lib\/libfive\/libfive\/include\\libfive.h:349:13","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":":pointer","type":{"tag":":char","bitSize":8,"bitAlignment":8}}}]