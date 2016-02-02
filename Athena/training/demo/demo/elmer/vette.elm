#
# Elmer interface for vette.py
#
# This will define the interface which C programs will use for accessing data
# from 3rd generation Corvette data files
#

#
# tell Elmer what python module this is describing
#
module vette

#
# expose the "test" function to C programs
# ...rename it to "getTestString()" for use in C
#
string test( void ) -> getTestString

#
# describe the interface for the VetteData class
#
class VetteData {

    #
    # the constructor returns a VetteData object and accepts a string
    # ...rename __init__ to "create()" for clarity in C
    #
    VetteData __init__( string data_file ) -> create

    void load_data( void )

    int get_year( void )

    float get_dimension( string dim )

    list get_options( void )

    VetteOption get_option( string opt_code )
}


class VetteOption {

    #
    # the constructor will not be needed in C programs, so lets not expose it
    #
    
    void set_code( string opt_code )
    void set_desc( string description )
    void set_quantity( int quan )

    string get_code( void )
    string get_desc( void )
    int get_quantity( void )
}

    
