
#include <stdlib.h>
#include <string.h>

#include "functions.h"


/*
 *  The functions defined here provide an example of a typical
 *  pattern in C.  An "init" function allocates a block of memory.
 *  An assortment of functions operate on this block of memory.
 *  A "close" method frees the memory created by the "init" function.
 *
 *  The example C functions are:
 *    channel_data *channel_init(char *name)
 *    int channel_calibrate(channel_data *chdata, int param)
 *    int channel_get_status(channel_data *chdata)
 *    int channel_close(channel_data *chdata)
 */

channel_data *channel_init(char *name)
    {
    channel_data *chdata;

    chdata = (channel_data *) malloc(sizeof(channel_data));
    if (chdata != NULL)
        {
        /* Some data for demonstration. */
        chdata->channel = 1;
        chdata->channel_status = 0;
        strcpy(chdata->code, "DEF");
        strncpy(chdata->name, name, NAME_BUFSIZE-1);
        chdata->name[NAME_BUFSIZE-1] = '\0'; 
        }
    return chdata;
    }

int channel_calibrate(channel_data *chdata, int param)
    {
    /* Just a demo; this doesn't really do anything interesting. */
    chdata->channel_status = param;
    return 0;
    }

int channel_get_status(channel_data *chdata)
    {
    return chdata->channel_status;
    }

int channel_write(channel_data *chdata, int buflen, unsigned char *buffer)
    {
    /*
     * Don't really write anything; just add up the bytes and
     * and return the sum.
     */
    int result;
    int i;

    result = 0;
    for (i = 0; i < buflen; ++i)
        {
        result += buffer[i];
        }
    return result;
    }

int channel_close(channel_data *chdata)
    {
    /*
     *  Be a little paranoid and check that the user isn't calling
     *  with chdata == NULL.
     */
    if (chdata != NULL)
        free(chdata);
    return 0;
    }
