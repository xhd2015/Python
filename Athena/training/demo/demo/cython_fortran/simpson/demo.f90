module functions

  use types, only: dp
  implicit none

  contains

  real(dp) function myfunc(x) result(y)
      implicit none
      real(dp), intent(in) :: x
      y = cos(x)
  end function myfunc

end module functions


program demo

  use types, only: dp
  use simpson_module, only: simpson
  use functions, only: myfunc

  implicit none

  real(dp) integral, a, b, exact

  a = 0.0_dp
  b = 2.0_dp
  exact = sin(b) - sin(a)

  integral = simpson(myfunc, 0.0_dp, 2.0_dp, 100)
  print *, "simpson:", integral
  print *, "exact is", exact

end program
