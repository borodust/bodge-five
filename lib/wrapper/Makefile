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

################################
#  MAIN LIBRARY CONFIGURATION  #
################################
NAME = five
INCLUDE_PATH = $(WORK_DIR)/../libfive/libfive/include

LIBNAME = lib$(NAME)
BIN := $(LIBNAME).$(EXTENSION)

################################
#    WRAPPER CONFIGURATION     #
################################
WRAPPER_SRC = cbv.c

WRAPPER_OBJ = $(WRAPPER_SRC:.c=.o)
WRAPPER_BIN = $(LIBNAME).wrapper.$(EXTENSION)
WRAPPER = $(WORK_DIR)/$(WRAPPER_BIN)
WRAPPER_CFLAGS = $(CFLAGS) -fPIC -I$(INCLUDE_PATH) -I../../
WRAPPER_LIBS =

ifeq ($(PLATFORM),linux)
	WRAPPER_CFLAGS += -Wl,-soname,$(WRAPPER_BIN) -Wl,-rpath,'$$ORIGIN/'
	WRAPPER_LIBS += -ldl
endif
ifeq ($(PLATFORM),darwin)
	WRAPPER_CFLAGS += -install_name '@loader_path/$(WRAPPER_BIN)'
	WRAPPER_LIBS += -ldl
endif

################################
#     BUILD CONFIGURATION      #
################################
build: $(WRAPPER)

$(WRAPPER):
	$(CC) -shared $(WRAPPER_SRC) $(WRAPPER_CFLAGS) -o $(WRAPPER) $(WRAPPER_LIBS)
	strip -S $(WRAPPER)

clean:
	rm -f $(WRAPPER)
