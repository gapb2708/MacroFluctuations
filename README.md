#Macroeconomics Fluctuations

In this project we consider a simple economy that is characterized by the following 2 dynamics:

1. $$c_{t+1}=\beta c_t[\alpha A(k_{t+1})^{\alpha-1}+1-\delta)]$$
2. $$c_t+k_{t+1}=A(k_{t})^\alpha+(1-\delta)k_t$$

We calibrate the model: $\beta=0.99; \alpha=0.34; \delta=0.02; A=1$

The stationary states are calculates as:

$$k^*= (\frac{1/\beta-1+\delta}{\alpha A})^\frac{1}{\alpha-1}$$

$$c^* = A(k^* )^{-1}- \delta (k^*)^{-1}$$

Then we proceed to add a %5 permanent shock to the productivity. We calculate the new stationary state and check what happens with the capital returns.

The transition follows this dynamic:

$$\hat{k}_ {t+2} = A_0\hat{k}_ t+A_1\hat{k}_{t+1}$$

Where

$$A_0= -(\alpha A(k^*)^{\alpha-1}+1-\delta)$$

$$A_1= 1+\alpha A (k^* )^{\alpha-1}+1-\delta-\beta(A(k^* )^{\alpha}-\delta k^*)\alpha(\alpha-1)A k^{\alpha-1}$$

With the values of $A_1$ and $A_0$, we then write the dynamic as:

$$P^2-A_0-A_1P=0$$

This is clearly a second degree equation where one solution is greater than 1 and the other not. We only take the root that is less than 1 because is the stable root of the system.

With the help of the $P$ value we can analyze how the system transitions from its original state to the state with the 5% productivity shock.
