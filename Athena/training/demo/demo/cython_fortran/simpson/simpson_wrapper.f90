module simpson_wrapper

use iso_c_binding, only: c_double, c_int
use simpson_module, only: simpson

implicit none
private
public c_simpson

contains

! c_simpson is a simple wrapper of simpson that has C bindings.

real(c_double) function c_simpson(f, a, b, n) bind(c)
    implicit none
    interface
        real(c_double) function f(x) bind(c)
        use iso_c_binding, only: c_double
        implicit none
        real(c_double), intent(in) :: x
        end function
    end interface
    real(c_double), intent(in) :: a, b
    integer(c_int), intent(in) :: n

    c_simpson = simpson(f, a, b, n)
end function

end module
