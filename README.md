# Pi_estimation

## Modules required: pygame, random

This is basically a program to estimate the value of pi using the Monte-Carlo method.

Here's how it works.

Consider a unit circle centered at the origin. Generate two random numbers between -1 and 1, say x and y. This point can be represented on a 2D plane as (x, y). Then find the Euclidean distance between the origin and (x, y). If the distance is less than 1 (ie the radius of the circle), then the point lies wthin the circle. The number of points lying within the circle and the total number of points needs to be kept track of. Do this an arbitrary number of times. Divide the number of points lying within the circle by the total number of points, and multiply the result by 4. That's an estimated value of pi.

This program, in essence, does the same thing, albeit in a slightly complicated way, since the centres of neither the square nor the circle is at the origin. So, the random numbers generated are between the left and right ends of the square.

## Screenshot:

![image](https://user-images.githubusercontent.com/84128922/136684594-69a45b76-98cf-4aab-88fc-134d33536590.png)

