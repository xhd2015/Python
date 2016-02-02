module simpson_module

use types, only: dp

implicit none
private
public simpson

contains

! function simpson(f, a, b, n)
!
! Simpson's composite rule.
! n must be even.  This function does not check for invalid values of n.

real(dp) function simpson(f, a, b, n) result(integral)
    interface
        function f(x)
        use types, only: dp
        implicit none
        real(dp) f
        real(dp), intent(in) :: x
        end function
    end interface
    real(dp), intent(in) :: a, b
    integer, intent(in) :: n

    real(dp) h, x
    integer i

    h = (b - a) / n

    integral = f(a) + f(b)
    do i = 1, n, 2
        x = a + h * i
        integral = integral + 4.0_dp * f(x)
    end do
    do i = 2, n - 1, 2
        x = a + h * i
        integral = integral + 2.0_dp * f(x)
    end do
    integral = (h / 3.0_dp) * integral

end function simpson

end module simpson_module
