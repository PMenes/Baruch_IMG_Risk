# Baruch_IMG_Risk
Risk Management and Portfolio Analysis for Baruch's Investment Management Group

The weights for minimum variance portfolio is determined by the solution to the constrained optimization problem 

<a href="https://www.codecogs.com/eqnedit.php?latex=\min_{w}&space;w^{T}&space;\Sigma&space;w" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\min_{w}&space;w^{T}&space;\Sigma&space;w" title="\min_{w} w^{T} \Sigma w" /></a>

By applying the method of Lagrange multiplier, we obtain the solution as:

<a href="https://www.codecogs.com/eqnedit.php?latex=w_{mvp}&space;=&space;\frac{\Sigma^{-1}&space;u}{u'&space;\Sigma^{-1}&space;u}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?w_{mvp}&space;=&space;\frac{\Sigma^{-1}&space;u}{u'&space;\Sigma^{-1}&space;u}." title="w_{mvp} = \frac{\Sigma^{-1} u}{u' \Sigma^{-1} u}." /></a>

The expected return $\ell_{mvp}$ and the variance $\sigma_{mvp}^2$ of the minimum variance portfolio are given by 

<a href="https://www.codecogs.com/eqnedit.php?latex=\ell_{mvp}&space;=&space;w_{mvp}'&space;\,&space;\ell&space;=&space;\frac{u'&space;\Sigma^{-1}\ell}{u^{T}&space;\Sigma^{-1}u}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\ell_{mvp}&space;=&space;w_{mvp}'&space;\,&space;\ell&space;=&space;\frac{u'&space;\Sigma^{-1}\ell}{u^{T}&space;\Sigma^{-1}u}" title="\ell_{mvp} = w_{mvp}' \, \ell = \frac{u' \Sigma^{-1}\ell}{u^{T} \Sigma^{-1}u}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_{mvp}^2&space;=&space;w_{mvp}'&space;\,&space;\Sigma&space;\,&space;w_{mvp}&space;=&space;\frac1{u^{T}&space;\Sigma^{-1}u}." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_{mvp}^2&space;=&space;w_{mvp}'&space;\,&space;\Sigma&space;\,&space;w_{mvp}&space;=&space;\frac1{u^{T}&space;\Sigma^{-1}u}." title="\sigma_{mvp}^2 = w_{mvp}' \, \Sigma \, w_{mvp} = \frac1{u^{T} \Sigma^{-1}u}." /></a>

