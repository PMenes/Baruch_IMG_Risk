# Baruch's IMG - Risk Management and Portfolio Analysis
Below are detailed mathemathcial derivations, to be used in the implementation of scripts and code. Provided documentaiton will serve as both a walkthrough and explanation of concepts to be used in the program. 

## Software Overview & General Maintenance 
Description

## Risk Managment Models
Description

### Beta 
Let <a href="https://www.codecogs.com/eqnedit.php?latex=r" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r" title="r" /></a> be the (random) return of a portfolio and <a href="https://www.codecogs.com/eqnedit.php?latex=r_M" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_M" title="r_M" /></a> the return of the market portfolio at investment horizon. The portfolio's <a href="https://www.codecogs.com/eqnedit.php?latex=\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta" title="\beta" /></a> is defined by the ratio 

<a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;:=&space;\frac{cov(r,&space;r_M)}{\sigma_M^2}&space;=&space;\rho&space;\frac{\sigma}{\sigma_M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;:=&space;\frac{cov(r,&space;r_M)}{\sigma_M^2}&space;=&space;\rho&space;\frac{\sigma}{\sigma_M}" title="\beta := \frac{cov(r, r_M)}{\sigma_M^2} = \rho \frac{\sigma}{\sigma_M}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a> is the correlation coefficient between <a href="https://www.codecogs.com/eqnedit.php?latex=r" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r" title="r" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=r_M" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_M" title="r_M" /></a>. 

In particular, if <a href="https://www.codecogs.com/eqnedit.php?latex=r_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_n" title="r_n" /></a> is the linear return of the risky asset <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>, then <a href="https://www.codecogs.com/eqnedit.php?latex=\beta_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta_n" title="\beta_n" /></a> is the beta of risky asset <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>.

### Value-at-Risk (VaR)
Description

### Conditional Value-at-Risk (CVaR)
Description

## Optimization Models
Description

### Minimum Variance Portfolio (MVP)
The weights for minimum variance portfolio is determined by the solution to the constrained optimization problem 

<a href="https://www.codecogs.com/eqnedit.php?latex=\min_{w}&space;w^{T}&space;\Sigma&space;w" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\min_{w}&space;w^{T}&space;\Sigma&space;w" title="\min_{w} w^{T} \Sigma w" /></a>

By applying the method of Lagrange multiplier, we obtain the solution as:

<a href="https://www.codecogs.com/eqnedit.php?latex=w_{mvp}&space;=&space;\frac{\Sigma^{-1}&space;u}{u'&space;\Sigma^{-1}&space;u}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?w_{mvp}&space;=&space;\frac{\Sigma^{-1}&space;u}{u'&space;\Sigma^{-1}&space;u}." title="w_{mvp} = \frac{\Sigma^{-1} u}{u' \Sigma^{-1} u}." /></a>

The expected return <a href="https://www.codecogs.com/eqnedit.php?latex=\ell_{mvp}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\ell_{mvp}" title="\ell_{mvp}" /></a> and the variance <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_{mvp}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_{mvp}^2" title="\sigma_{mvp}^2" /></a> of the minimum variance portfolio are given by 

<a href="https://www.codecogs.com/eqnedit.php?latex=\ell_{mvp}&space;=&space;w_{mvp}'&space;\,&space;\ell&space;=&space;\frac{u'&space;\Sigma^{-1}\ell}{u^{T}&space;\Sigma^{-1}u}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\ell_{mvp}&space;=&space;w_{mvp}'&space;\,&space;\ell&space;=&space;\frac{u'&space;\Sigma^{-1}\ell}{u^{T}&space;\Sigma^{-1}u}" title="\ell_{mvp} = w_{mvp}' \, \ell = \frac{u' \Sigma^{-1}\ell}{u^{T} \Sigma^{-1}u}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_{mvp}^2&space;=&space;w_{mvp}'&space;\,&space;\Sigma&space;\,&space;w_{mvp}&space;=&space;\frac1{u^{T}&space;\Sigma^{-1}u}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_{mvp}^2&space;=&space;w_{mvp}'&space;\,&space;\Sigma&space;\,&space;w_{mvp}&space;=&space;\frac1{u^{T}&space;\Sigma^{-1}u}." title="\sigma_{mvp}^2 = w_{mvp}' \, \Sigma \, w_{mvp} = \frac1{u^{T} \Sigma^{-1}u}." /></a>

### Market Portfolio (MP)
Description
