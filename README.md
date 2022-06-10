# visionmath
showing how tape detect math works


[web version](https://replit.com/@Kiwi_kun/visionmath-1?v=1)


<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8" />
<link href='https://fonts.googleapis.com/css?family=Oswald' rel='stylesheet'>
<link rel="stylesheet" href="css/inter.css" />
<link
rel="stylesheet"
href="css/main.css"
/>


</head>
<body style="background-color: white;">
<div class="sidenav">
<a href="#title"> <i class="oswald"; style="font-size: 25px;">vision math!</i></a>
<a href="#variable_h">table of variables</a>
<a href="#no_tilt">no tilt</a>
<a href="#horizontal_tilt">horizontal tilt</a>
<a href="#vertical_tilt">vertical tilt</a>
<a href="#all_tilt">tilt in all dimensions</a>
</div>

<div class="header">
<h1 id="title"; align="center"><i>vision math for rapid react, 2022</i></h1>
</div>

<div class="main">
<h2 id="variable_h">table of variables </h2>
<table id="variable_table">
<tr>
<td>
variable name
</td>
<td>
meaning of variable
</td>
<td align="center">
value
</td>
</tr>
<tr>
<td>
$$y_{img}$$
</td>
<td>
distance from the bottom of the screen in px
</td>
<td>
$$0 < y_{img} < 240$$
</td>
</tr>
<tr>
<td>
$$x_{img}$$
</td>
<td>
distance from the center horizontally in px, right = positive and left = negative
</td>
<td>
$$-160 < x_{img} < 160$$
</td>
</tr>
<tr>
<td>
$$f$$
</td>
<td>
focal length (horizontal)
</td>
<td>
$$284.772$$
</td>
</tr>
<tr>
<td>
$$h$$
</td>
<td>
height from camera to tape in feet
</td>
<td>
$$4.8125$$
</td>
</tr>

<tr>
<td>
$$z$$
</td>
<td>
straight line distance to the target in feet
</td>
<td>
$$z$$
</td>
</tr>

<tr>
<td>
$$\theta$$
</td>
<td>
horizontal angle between robot and target
</td>
<td>
$$\theta$$
</td>
</tr>

<tr>
<td>
$$\rho$$
</td>
<td>
angle between robot and target, vertically
</td>
<td>
$$arctan(\frac{h}{z}$$
</td>
</tr>

<tr>
<td>
$$z_\theta$$
</td>
<td>
distance to target if it's angled
</td>
<td>
$$z_\theta$$
</td>
</tr>

<tr>
<td>
$$\varphi$$
</td>
<td>
vertical tilt up of limelight camera in RADIANS
</td>
<td>
$$\varphi$$
</td>
</tr>

<tr>
<td>
$$y_v$$
</td>
<td>
virtual y_img, where it would be if the FOV is centered
</td>
<td>
$$y_v$$
</td>
</tr>

</table>
 
<img src=/images/tkinter.png height="300"> <img src=/images/variables.png height="300">
<img src=/images/interface.png height="300"> <img src=/images/pinhole.png height="300">


<h2 id="no_tilt"> no tilt in any direction</h2>
<p>
Assumptions: robot is aligned, limelight FOV is 60 degrees and it's exactly 30 degrees on each side (FOV is centered)
</p>
<p>
because of how a pinhole camera works, and since no tilt in any axis, $$x_{img} = 0$$ $$\frac{y_{img}}{f} = \frac{h}{z}$$$$z = \frac{hf}{y_{img}}$$
</p>
<p>
alternatively, $$\rho = arctan(\frac{y_{img}}{f}) = arctan(\frac{h}{z})$$
</p>
<div align="center">
<img src=/images/notilt.png height="300">
</div>

<h2 id="horizontal_tilt">tilt in the horizontal direction</h2> 
<p>
Assumptions: FOV is still centered.
</p>
<p>
Since there is horizontal tilt, x_img != 0. So we have a right triangle with legs x_img, in non-camera verison, and z, and hypotenuse z_theta, where z_theta is actual distance to target and z is the distance to the target if it were aligned. We already know that

$$z = \frac{hf}{y_{img}}$$
 $$z^2 + (\frac{x_{img}h}{y_{img}})^2 = {z_\theta}^2$$
solving for $${z_\theta}$$, we get
$$z_\theta = \sqrt{(\frac{hf}{y_{img}})^2 + (\frac{x_{img}h}{y_{img}})^2}$$
</p>
<div align="center">
<img src=/images/horizontaltilt.png height="300">
</div>

<h2 id="vertical_tilt">tilt in the vertical direction</h2>
<p>
Now the FOV is no longer centered. There is a tilt of phi radians up. For now, we will disregard horizontal tilt and assume we are aligned to the target.
</p>
<p>
$$\theta = arctan(\frac{y_{img}}{f})$$
We can get the vertical angle of the perceived target. Then since we are adding phi, the target appears further away than expected if phi is positive, so we take $$tan(arctan(\frac{y_{img}}{f}) + \varphi)$$
as the target is actually further up. Then finally, we take h divided by this to get the distance:

$$z_\varphi = \frac{h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)}$$
</p>
<p>
We also get that $$y_v = tan(arctan(\frac{y_{img}}{f} + \varphi))\cdot f$$
</p>
<div align="center">
<img src=/images/verticaltilt.png height="300">
</div>

<h2 id="all_tilt"> all 3 axis together</h2>
<p>
So we have that
$$z_\theta = \sqrt{(\frac{hf}{y_{img}})^2 + (\frac{x_{img}h}{y_{img}})^2}$$
$$z_\varphi = \frac{h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)}$$
</p>

<p>
When we derived z_theta, we had an intermediate equation $$z^2 + (\frac{x_{img}h}{y_{img}})^2 = {z_\theta}^2$$
</p>

<p>
$$y_v = tan(arctan(\frac{y_{img}}{f}) + \varphi)\cdot f$$
</p>

<p>
Plugging this in, we get
$$(\frac{h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)})^2 + (\frac{x_{img}h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)\cdot f})^2 = {z_\theta}^2$$
</p>





<p>
Or, solving for z_theta:
$$z_\theta = \sqrt{(\frac{h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)})^2 + (\frac{x_{img}h}{tan(arctan(\frac{y_{img}}{f}) + \varphi)\cdot f})^2}$$
</p>



</body>
</html>
