################################
#        LOCAL ENVIRONMENT     #
################################
WORK_DIR = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

ifeq ($(OS),Windows_NT)
	EXTENSION := dll
	PLATFORM := windows
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Darwin)
		EXTENSION := dylib
		PLATFORM := darwin
	else
		EXTENSION := so
		PLATFORM := linux
	endif
endif
CFLAGS += -march=x86-64

################################
#  MAIN LIBRARY CONFIGURATION  #
################################
NAME = five
LIBRARY_PATH = $(WORK_DIR)/libfive/build/libfive/src
INCLUDE_PATH = $(WORK_DIR)/libfive/libfive/include
BUILD_DIR = $(WORK_DIR)/libfive/build/

LIBNAME = lib$(NAME)
BIN := $(LIBNAME).$(EXTENSION)

LIBRARY := $(LIBRARY_PATH)/$(BIN)
BODGED_LIBRARY := $(WORK_DIR)/$(BIN)
WRAPPER := $(WORK_DIR)/lib$(NAME).wrapper.$(EXTENSION)

################################
#     BUILD CONFIGURATION      #
################################
build: wrapper bodged-library

library: $(LIBRARY)

$(LIBRARY):
	mkdir -p libfive/build && cd libfive/build/						\
	&& cmake -G "Unix Makefiles" $(BODGE_CMAKE_FLAGS)					\
		 -DCMAKE_C_FLAGS="$(CFLAGS)" -DCMAKE_CXX_FLAGS="$(CFLAGS) $(CXXFLAGS)"		\
		 -DBUILD_STUDIO_APP=OFF -DBUILD_TESTS=OFF -DBUILD_GUILE_BINDINGS=OFF ..		\
	&& cmake --build .

wrapper: $(WRAPPER)

$(WRAPPER):
	cd wrapper && make clean build

bodged-library: $(BODGED_LIBRARY)

$(BODGED_LIBRARY): library
	cp -L $(LIBRARY) $(BODGED_LIBRARY)
	strip -S $(BODGED_LIBRARY)
	case "$(PLATFORM)" in									\
	linux)											\
	  echo "Updating rpath of $(BODGED_LIBRARY)";						\
	  patchelf --set-rpath '$$ORIGIN/' $(BODGED_LIBRARY);					\
	  echo "$(BIN) SONAME: $$(patchelf --print-soname $(BODGED_LIBRARY))";			\
	;;											\
	darwin)											\
	  echo "Installing rpath name for $(BODGED_LIBRARY)";					\
	  install_name_tool -id "@loader_path/$(BIN)" "$(BODGED_LIBRARY)";			\
	;;											\
	esac

clean:
	rm -rf $(BODGED_LIBRARY) $(WRAPPER) $(BUILD_DIR)
