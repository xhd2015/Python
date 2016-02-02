

      PROGRAM DEMO
C
C     Demonstrate the use of the SIMPSON function by
C     computing the definite integral of COS(X).
C
      EXTERNAL FUNC
      REAL*8 FUNC
      REAL*8 INTEGRAL, A, B, EXACT
      INTEGER N

      A = 0.0D0
      B = 2.0D0
      N = 100
      EXACT = DSIN(B) - DSIN(A)

      INTEGRAL = SIMPSON(FUNC, A, B, N)

      WRITE(*,*), "simpson:", INTEGRAL
      WRITE(*,*), "exact is", EXACT

      STOP
      END


      REAL*8 FUNCTION FUNC(X)
      REAL*8 X
      FUNC = DCOS(X)
      RETURN
      END
