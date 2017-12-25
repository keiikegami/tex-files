# Nerton Raphson
def NR1(theta, m11,m00,m1,itr, tol):
    for i in range(0,itr):
        # hess calculates hessian
        # grad calculates gardient
        del_theta = np.linalg.inv(hess(theta[0,0],theta[1,0],m11,m00,m1)).dot(grad(theta[0,0],theta[1,0],m11,m00,m1))
        theta = theta - del_theta
        if np.linalg.norm(del_theta) < tol:
            break
    return theta

# Main loop
def func(theta,m11,m00,m1,maxit,tol, itr, high):
    count = 0
    for j in range(0,maxit):
        # correct_ratio_00 is the function f_0
        # correct_ratio_00 is the function f_2
        ratio00 = correct_ratio_00(theta[0,0], theta[1,0])
        ratio11 = correct_ratio_11(theta[0,0], theta[1,0])
        # ratio00 denotes the ratio of markets which have no firm
        # ratio11 denotes the ratio of markets which have two firms
        newm00 = m00 * ratio00
        newm11 = m11 * ratio11
        newm1 = market_size - newm11 - newm00
        newtheta = NR1(theta,newm11,newm00,newm1,itr,tol)
        count += 1
        # conversion check
        if np.linalg.norm(newtheta - theta) < tol:
            checker = newtheta + e.rvs((2,1))/100
            checker = NR1(checker,newm11,newm00,newm1,itr,tol)
            if np.linalg.norm(newtheta - checker) < tol:
                newtheta = checker
                print("conversion")
                break
            else:
                theta = checker
        elif np.linalg.norm(newtheta - theta) > high:
            if count > 10:
                theta = (newtheta + theta)/2 + e.rvs((2,1))
                count = 0
        theta = newtheta
    return newtheta