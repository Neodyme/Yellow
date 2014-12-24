# - Try to find LibXml2
# Once done this will define
#  LIBXML2_FOUND - System has LibXml2
#  LIBXML2_INCLUDE_DIRS - The LibXml2 include directories
#  LIBXML2_LIBRARIES - The libraries needed to use LibXml2
#  LIBXML2_DEFINITIONS - Compiler switches required for using LibXml2

find_package(PkgConfig)
pkg_check_modules(PC_LIBTINS QUIET libtins)
set(LIBTINS_DEFINITIONS ${PC_LIBXML_CFLAGS_OTHER})

find_path(LIBTINS_INCLUDE_DIR tins/tins.h
  HINTS ${PC_LIBTINS_INCLUDEDIR} ${PC_LIBTINS_INCLUDE_DIRS}
  PATH_SUFFIXES tins )

find_library(LIBTINS_LIBRARY NAMES tins libtins
  HINTS ${PC_LIBTINS_LIBDIR} ${PC_LIBTINS_LIBRARY_DIRS} )

set(LIBTINS_LIBRARIES ${LIBTINS_LIBRARY} )
set(LIBTINS_INCLUDE_DIRS ${LIBTINS_INCLUDE_DIR} )

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(LibXml2  DEFAULT_MSG
  LIBTINS_LIBRARY LIBTINS_INCLUDE_DIR)

mark_as_advanced(LIBTINS_INCLUDE_DIR LIBTINS_LIBRARY )
