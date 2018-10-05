# LOCAL ENVIRONMENT
WORK_DIR = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

ifeq ($(OS),Windows_NT)
	EXTENSION := dll
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Darwin)
		EXTENSION := dylib
	else
		EXTENSION := so
	endif
endif
################

# MAIN LIBRARY CONFIGURATION
NAME = five
BIN = lib$(NAME)

LIBRARY_FILE := $(WORK_DIR)/libfive/build/libfive/src/libfive.$(EXTENSION)
BIN := $(BIN).$(EXTENSION).bodged
TARGET_FILE := $(WORK_DIR)/$(BIN)
################

# WRAPPER LIBRARY CONFIGURATION
WRAPPER_SRC = cbv.c
WRAPPER_OBJ = $(WRAPPER_SRC:.c=.o)
WRAPPER_BIN = $(BIN).wrapper
WRAPPER_TARGET_FILE = $(WORK_DIR)/$(WRAPPER_BIN)
WRAPPER_CFLAGS = $(CFLAGS) -O2 -fPIC  -I./libfive/libfive/include/ -I../ -L./
WRAPPER_LIBS = $(BIN)
################

build: $(WRAPPER_TARGET_FILE)

$(WRAPPER_TARGET_FILE): $(TARGET_FILE)
	$(CC) -shared $(WRAPPER_SRC) $(WRAPPER_CFLAGS) -o $(WRAPPER_TARGET_FILE) $(WRAPPER_LIBS)
	strip -S $(WRAPPER_TARGET_FILE)
	if [ "$(EXTENSION)" = "so" ]; then							\
	  patchelf --set-rpath '@ORIGIN/' "$(WRAPPER_TARGET_FILE)";				\
	  patchelf --set-soname '$(WRAPPER_BIN)' "$(WRAPPER_TARGET_FILE)";			\
	fi

$(TARGET_FILE):
	mkdir -p libfive/build && cd libfive/build/						\
	&& cmake -G "Unix Makefiles" $(BODGE_CMAKE_FLAGS)					\
		 -DCMAKE_C_FLAGS="$(CFLAGS)" -DCMAKE_CXX_FLAGS="$(CFLAGS) $(CXXFLAGS)"		\
		 -DBUILD_STUDIO_APP=OFF ..							\
	&& cmake --build .
	cp -L $(LIBRARY_FILE) $(TARGET_FILE)
	strip -S $(TARGET_FILE)
	if [ "$(EXTENSION)" = "so" ]; then							\
	  patchelf --set-rpath '@ORIGIN/' "$(TARGET_FILE)";					\
	  patchelf --set-soname '$(BIN)' "$(TARGET_FILE)";					\
	fi

clean:
	rm -rf $(TARGET_FILE) $(WRAPPER_TARGET_FILE) $(WORK_DIR)/libfive/build/
