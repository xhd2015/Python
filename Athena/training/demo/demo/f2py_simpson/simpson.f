
      FUNCTION SIMPSON(F, A, B, N)
C
C     Apply the composite Simpson's rule to the function F(X) using N
C     subintervals on the interval A <= X <= B.  N must be even (but
C     the code does not verify this).
C
      EXTERNAL F
      REAL*8 SIMPSON
      REAL*8 F
      REAL*8 A, B
      INTEGER N

      REAL*8 H, X
      INTEGER I

      H = (B - A) / N
      SIMPSON = F(A) + F(B)

      DO I = 1, N, 2
         X = A + H * I
         SIMPSON = SIMPSON + 4.0D0 * F(X)
      ENDDO
      DO I = 2, N - 1, 2
         X = A + H * I
         SIMPSON = SIMPSON + 2.0D0 * F(X)
      ENDDO
      SIMPSON = (H / 3.0D0) * SIMPSON
      RETURN
      END
