/*
 * this is the C test program which exercises the vette.py module
 * through the use of an elmer-generated C interface
 */
#include <vette.h>

int main( int argc, char** argv ) {

  int vStat1, vOpt1;
  int vStat2, vOpt2;

  /*
   * load data files and create data objects for each
   * ...tell the elmer interface code to generate new, unique IDs instead
   * of maintaining them ourselves
   */
  vStat1 = VetteData_create( "68.dat", elNEWID );
  VetteData_load_data( vStat1 );
  
  vStat2 = VetteData_create( "72.dat", elNEWID );
  VetteData_load_data( vStat2 );

  /*
   * lookup specific options for each data object and create option objects
   */
  vOpt1 = VetteData_get_option( vStat1, "C60", elNEWID );
  vOpt2 = VetteData_get_option( vStat2, "C60", elNEWID );

  /*
   * access and print the data
   */
  printf( "\n" );
  printf( "For model year: %d, the Corvette weighed %.2f pounds\n", 
	  VetteData_get_year( vStat1 ),
	  VetteData_get_dimension( vStat1, "weight" ) );

  printf( "For model year: %d, %d orders were made for (%s), \"%s\"\n", 
	  VetteData_get_year( vStat1 ),
	  VetteOption_get_quantity( vOpt1 ),
	  VetteOption_get_code( vOpt1 ),
	  VetteOption_get_desc( vOpt1 ) );

  printf( "\n" );
  printf( "For model year: %d, the Corvette weighed %.2f pounds\n", 
	  VetteData_get_year( vStat2 ),
	  VetteData_get_dimension( vStat2, "weight" ) );
  
  printf( "For model year: %d, %d orders were made for (%s), \"%s\"\n", 
	  VetteData_get_year( vStat2 ),
	  VetteOption_get_quantity( vOpt2 ),
	  VetteOption_get_code( vOpt2 ),
	  VetteOption_get_desc( vOpt2 ) );

  printf( "\n" );

  /*
   * if -test was given, dump test string
   */
  if( (argc > 1) && (strcmp( argv[1], "-test" ) == 0) ) {
    printf( "%s\n", getTestString() );
  }
  
  /*
   * tell Python to cleanup
   */
  delete_obj( vStat1 );
  delete_obj( vOpt1 );
  delete_obj( vStat2 );
  delete_obj( vOpt2 );

 return 0;
}

