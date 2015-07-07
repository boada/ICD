
# Install directory
INS_DIR = /home/steven/Projects/galaxy_icd_orig/libraries

# Compiler Info
CC     = gcc
OPTIMIZE = -O3

# Libraries
GSL_LIBS = -L/opt/gsl_1.15/lib
#FFTW_LIBS = -L/opt/fftw-3.2.2/lib
CFITSIO_LIBS = -L/opt/cfitsio_3.31/lib

# Includes
GSL_INC = -I/opt/gsl_1.15/include
#FFTW_INC = -I/opt/fftw-3.2.2/include
CFITSIO_INC = -I/opt/cfitsio_3.31/include

# Executable
EXEC = liboverseer

# Compiler Flags
OPTIONS = $(OPTIMIZE) $(OPT)
CFLAGS = $(OPTIONS) $(GSL_INC) $(FFTW_INC) $(CFITSIO_INC)
GSL_LIBS += -lgsl -lgslcblas
#FFTW_LIBS += -lfftw3
CFITSIO_LIBS += -lcfitsio
LIBS = -g $(GSL_LIBS) $(FFTW_LIBS) $(CFITSIO_LIBS) -lm

# Object Files
OBJS = 	image_size.lo \
	read_image.lo \
	read_table.lo \
	write_image.lo \
	fit.lo \
	calc_pr.lo \
	printerror.lo

$(EXEC): $(OBJS)
	libtool --mode=link $(CC) $(CFLAGS) -o $(EXEC).la $(OBJS) \
		-rpath $(INS_DIR) $(LIBS)

install:
	libtool --mode=install cp liboverseer.la $(INS_DIR)/liboverseer.la

image_size.lo: image_size.c
	libtool --mode=compile ${CC} ${CFLAGS} -c image_size.c 
read_image.lo: read_image.c
	libtool --mode=compile ${CC} ${CFLAGS} -c read_image.c
read_table.lo: read_table.c
	libtool --mode=compile ${CC} ${CFLAGS} -c read_table.c
write_image.lo: write_image.c
	libtool --mode=compile ${CC} ${CFLAGS} -c write_image.c
fit.lo: fit.c
	libtool --mode=compile ${CC} ${CFLAGS} -c fit.c
calc_pr.lo: calc_pr.c
	libtool --mode=compile ${CC} ${CFLAGS} -c calc_pr.c
printerror.lo: printerror.c
	libtool --mode=compile ${CC} ${CFLAGS} -c printerror.c

clean:
	rm -rf $(OBJS) $(EXEC).* *.lo *.o .libs/
