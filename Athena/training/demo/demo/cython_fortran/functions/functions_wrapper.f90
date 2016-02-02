module functions_wrapper

use iso_c_binding, only: c_int, c_double
use functions, only: sinc1d
implicit none

contains

subroutine c_sinc1d(n, x, y) bind(C)
    integer(c_int), value :: n
    real(c_double), intent(in) :: x(n)
    real(c_double), intent(out) :: y(n)

    call sinc1d(n, x, y)

end subroutine

end module
