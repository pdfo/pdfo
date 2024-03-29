! The gateway for COBYLA
!
! Authors:
!     Tom M. RAGONNEAU (tom.ragonneau@polyu.edu.hk)
!     and Zaikun ZHANG (zaikun.zhang@polyu.edu.hk)
!     Department of Applied Mathematics,
!     The Hong Kong Polytechnic University.
!
! Dedicated to the late Professor M. J. D. Powell FRS (1936--2015).

module fcobyla
use pdfoconst ! See pdfoconst.F, which defines HUGENUM
implicit none
integer :: nf
double precision, allocatable :: fhist(:),chist(:),conval_x0(:)
end module fcobyla

subroutine mcobyla (n,m,x,rhobeg,rhoend,iprint,maxfun,w,iact,f,info,funhist,conhist,ftarget,resmax,conval)
use fcobyla
implicit none
integer, intent(in) :: n,m,iprint,maxfun,iact(m+1)
integer, intent(out) :: info
integer :: i
double precision, intent(inout) :: x(n),conval(m)
double precision, intent(in) :: rhobeg,rhoend,w(n*(3*n+2*m+11)+4*m+6),ftarget
double precision, intent(out) :: f,funhist(maxfun),conhist(maxfun),resmax

nf=0
if (allocated(fhist)) deallocate (fhist)
allocate(fhist(maxfun))
if (allocated(chist)) deallocate (chist)
allocate(chist(maxfun))
if (allocated(conval_x0)) deallocate (conval_x0)
allocate(conval_x0(m))
fhist(:)=hugenum
chist(:)=hugenum
do i=1,m
    ! The values of the constraint functions at the initial guess are
    ! evaluated in the Python code, in order to get their number.
    ! Therefore, not to re-evaluate it, we store it in the module
    ! fcobyla to use it during the first evaluation.
    conval_x0(i)=conval(i)
end do

call cobyla (n,m,x,rhobeg,rhoend,iprint,maxfun,w,iact,f,info,ftarget,resmax,conval)

funhist=fhist
conhist=chist
deallocate(fhist)
deallocate(chist)
return
end subroutine mcobyla

subroutine calcfc (n,m,x,f,con)
use fcobyla
implicit none
integer, intent(in) :: n,m
integer :: i
double precision, intent(in) :: x(n)
double precision, intent(out) :: f,con(m)
double precision :: fun,resmax
external :: fun,confun
f=fun(n,x)

! use extreme barrier to cope with 'hidden constraints'
if (f .gt. HUGEFUN .or. f .ne. f) then
    f = HUGEFUN ! HUGEFUN is defined in pdfoconst
endif

resmax=0.0d0
if (m .gt. 0 .and. nf .ne. 0) then
    ! The call to the constraint subroutine should be made only if a
    ! constraint function is supplied in the Python code. If m = 0,
    ! no such function is defined.
    call confun(n,m,x,con)
else
    ! The evaluations of the constraint functions of the first
    ! iteration has already been done, and stored in conval_x0. Note
    ! that the case m=0 does not lead to an exception since the DO
    ! statement will not be executed.
    do i=1,m
        con(i)=conval_x0(i)
    end do
endif
do i=1,m
    if (con(i) .lt. -HUGECON .or. con(i) .ne. con(i)) then
        con(i) = -HUGECON ! HUGECON is defined in pdfoconst
    endif

    ! This part is NOT extreme barrier. We replace extremely negative values
    ! of the constraint array (which leads to no constraint violation) by
    ! -hugecon. Otherwise, NaN of Inf may occur in the interpolation models.
    if (con(i) .gt. HUGECON) then
        con(i) = HUGECON ! HUGECON is defined in pdfoconst
    endif

    resmax=dmax1(resmax,-con(i))
enddo

nf=nf+1
fhist(nf)=f
chist(nf)=resmax
return
end subroutine calcfc
