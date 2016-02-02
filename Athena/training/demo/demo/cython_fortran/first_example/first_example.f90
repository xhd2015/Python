real(c_double) function myfunc(x) bind(C)
    use iso_c_binding, only: c_double
    implicit none
    real(c_double), intent(in) :: x

    real(c_double) y

    myfunc = x ** 2 + 1.0D0
end function myfunc
