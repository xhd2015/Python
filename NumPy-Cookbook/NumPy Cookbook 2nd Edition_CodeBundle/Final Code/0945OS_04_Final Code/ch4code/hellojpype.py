import jpype
import numpy as np

#1. Start the JVM
jpype.startJVM(jpype.getDefaultJVMPath())

#2. Print hello world
jpype.java.lang.System.out.println("hello world")

#3. Send a NumPy array
values = np.arange(7)
java_array = jpype.JArray(jpype.JDouble, 1)(values.tolist())

for item in java_array:
   jpype.java.lang.System.out.println(item)

#4. Shutdown the JVM
jpype.shutdownJVM()
