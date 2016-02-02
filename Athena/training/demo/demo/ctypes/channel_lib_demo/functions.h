
/*
 *  Declarations for the data structures and functions in functions.c.
 */
 
#define NAME_BUFSIZE 16
 
typedef struct
    {
    int channel;
    int channel_status;
    char code[4];
    char name[NAME_BUFSIZE];
    } channel_data;

channel_data *channel_init(char *name);
int channel_calibrate(channel_data *chdata, int param);
int channel_get_status(channel_data *chdata);
int channel_write(channel_data *chdata, int buflen, unsigned char *buffer);
int channel_close(channel_data *chdata);
