module functions

    implicit none
    integer, parameter :: dp = kind(1.0D0)
    real(dp), parameter :: PI = 3.141592653589793238_dp

contains

    subroutine sinc1d(n, x, y)
        integer, intent(in) :: n
        real(dp), dimension(n), intent(in) :: x
        real(dp), dimension(n), intent(out) :: y

        where(x == 0.0_dp)
            y = 1.0_dp
        elsewhere
            y = sin(PI * x) / (PI * x)
        endwhere

    end subroutine

end module
