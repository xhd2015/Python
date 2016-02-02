#include <Python.h>
#define elDEBUG 0
#include <elmer.h>
#include <vette.h>
static int __vetteObjCnt = 0;
static PyObject* __vetteEvalModule;
static PyObject* __vetteEvalDict;
static PyObject* __vetteEvalVal;
static int vette_IsLoaded = 0;

void vette_assertInitialized() {
   if( !Py_IsInitialized() ) {
      Py_Initialize();
   }
   if( !vette_IsLoaded ) {
      if( elDEBUG ) printf( "PYTHON CALL: import vette\n" );
      PyRun_SimpleString( (char*)"import vette" );
      vette_IsLoaded = 1;
   }
}
char* getTestString() {
   ElString __vetteRunString = elStrNew();
   char* retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = vette.test( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = PyString_AsString( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

int VetteData_create(char* arg0, int arg1) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   if( arg1 == elNEWID ) {
      __vetteObjCnt++;
      arg1 = __vetteObjCnt;
   } else {
      if( arg1 > __vetteObjCnt ) {
         __vetteObjCnt = arg1;
      }
   }
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, " = vette.VetteData( " );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
   return arg1;
}

void VetteData_load_data(int arg0) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".load_data( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
}

int VetteData_get_year(int arg0) {
   ElString __vetteRunString = elStrNew();
   int retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_year( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = (int)PyInt_AsLong( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

float VetteData_get_dimension(int arg0, char* arg1) {
   ElString __vetteRunString = elStrNew();
   int retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_dimension( " );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = (int)PyInt_AsLong( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

int VetteData_get_options(int arg0, int arg2) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   if( arg2 == elNEWID ) {
      __vetteObjCnt++;
      arg2 = __vetteObjCnt;
   } else {
      if( arg2 > __vetteObjCnt ) {
         __vetteObjCnt = arg2;
      }
   }
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg2 );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_options( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
   return arg2;
}

int VetteData_get_option(int arg0, char* arg1, int arg2) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   if( arg2 == elNEWID ) {
      __vetteObjCnt++;
      arg2 = __vetteObjCnt;
   } else {
      if( arg2 > __vetteObjCnt ) {
         __vetteObjCnt = arg2;
      }
   }
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg2 );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_option( " );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
   return arg2;
}

void VetteOption_set_code(int arg0, char* arg1) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".set_code( " );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
}

void VetteOption_set_desc(int arg0, char* arg1) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".set_desc( " );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, "\"\"\"" );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
}

void VetteOption_set_quantity(int arg0, int arg1) {
   ElString __vetteRunString = elStrNew();
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".set_quantity( " );
   elStrAppendInt( __vetteRunString, arg1 );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
}

char* VetteOption_get_code(int arg0) {
   ElString __vetteRunString = elStrNew();
   char* retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_code( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = PyString_AsString( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

char* VetteOption_get_desc(int arg0) {
   ElString __vetteRunString = elStrNew();
   char* retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_desc( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = PyString_AsString( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

int VetteOption_get_quantity(int arg0) {
   ElString __vetteRunString = elStrNew();
   int retVal;
   vette_assertInitialized();
   elStrAppendString( __vetteRunString, "__vetteObj" );
   elStrAppendString( __vetteRunString, " = __vetteObj" );
   elStrAppendInt( __vetteRunString, arg0 );
   elStrAppendString( __vetteRunString, ".get_quantity( " );
   elStrAppendString( __vetteRunString, " )" );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   __vetteEvalModule = PyImport_AddModule( (char*)"__main__" );
   __vetteEvalDict = PyModule_GetDict( __vetteEvalModule );
   __vetteEvalVal = PyDict_GetItemString( __vetteEvalDict, "__vetteObj" );
   if( __vetteEvalVal == NULL ) {
      char* elDebugVar = getenv( "EDEBUG" );
      if( (elDebugVar != NULL) && (strcmp( "1", elDebugVar ) == 0) || elDEBUG ) {
         PyErr_Print();
      }
      exit( 1 );
   }
   if( __vetteEvalVal == NULL ) {
      retVal = 0;
   } else {
      retVal = (int)PyInt_AsLong( __vetteEvalVal );
   }
   if( Py_FlushLine() ) {
      PyErr_Clear();
   }
   elStrDestroy( __vetteRunString );
   return retVal;
}

void delete_obj( int objId ) {
   ElString __vetteRunString = elStrNew();
   elStrAppendString( __vetteRunString, "del __vetteObj" );
   elStrAppendInt( __vetteRunString, objId );
   if( elDEBUG ) printf( "PYTHON CALL: %s\n", elStrGet( __vetteRunString ) );
   PyRun_SimpleString( elStrGet( __vetteRunString ) );
   elStrDestroy( __vetteRunString );
}
