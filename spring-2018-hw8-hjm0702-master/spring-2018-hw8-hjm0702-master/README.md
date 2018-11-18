# MPCS 51042, Python Programming

**Homework 8**

**Due**: May 29 at 12:00pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1

The [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) is one of the most complex and beautiful images arising from mathematics. It is defined to be the set of [complex numbers](https://en.wikipedia.org/wiki/Complex_number) for which the function f<sub>c</sub>(z) = z<sup>2</sup> + c does not diverge when iterated from z=0. For a clear explanation of what that means, see [this video](https://www.youtube.com/watch?v=NGMRB4O922I) on YouTube featuring Dr. Holly Krieger from MIT. In short:

- Each point in the image corresponds a different number, c, in the complex plane. The x-axis represents the real component of the complex number and the y-axis represents the imaginary component of the complex number.
- Each different color in the image represents how many iterations it took for the function f(z) to diverge. For points where the function f(z) does not diverge (for example, c=0), the corresponding pixel is usually colored black.

For this problem, you will need to have the [matplotlib](https://matplotlib.org/) third-party package installed on your machine. 

### Evaluating iterations

Write a function called `mandelbrot(c, max_iterations=100)` that determines whether the function f(z) diverges for a given point, c, in the complex plane. The function should iterate on successive values of f(z) = z<sup>2</sup> + c starting at z=0 (i.e. z<sub>1</sub> = 0<sup>2</sup> + c, z<sub>2</sub> = z<sub>1</sub><sup>2</sup> + c, z<sub>3</sub> = z<sub>2</sub><sup>2</sup> + c, ...). If at any point, the [absolute value](https://en.wikipedia.org/wiki/Complex_number#Absolute_value_and_argument) of z<sub>n</sub> becomes greater than 2, we know that the function has diverged. Once this happens, `mandelbrot` should return the number of iterations that it took to diverge. If `max_iterations` iterations are reached, it is assumed that the function does not diverge for the given input, c. In this case, `mandelbrot` should return zero.

### Generating an image in serial

Write a function called `mandelbrot_serial(xmin, xmax, ymin, ymax, N=100)` that generates an image of the Mandelbrot set for complex numbers whose real components range from `xmin` to `xmax` and imaginary components range from `ymin` to `ymax`.

- The `xmin`, `xmax`, `ymin`, and `ymax` arguments can be assumed to be of type `float`.
- The function should return a list for which each element is a list itself storing the number of iterations returned by `mandelbrot` for each value of `c` corresponding to a pixel in a row of the image. The nested lists should be able to be passed directly to [matplotlib.pyplot.imshow](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow). For the image to display correctly, the [0][0] index in the nested list should correspond to the upper left corner of the image (lowest x value, highest y value).
- The `N` argument specifies the resolution of the image (number of pixels in each dimension), so the resulting list should have, by default, 100 items (each of them being a list with 100 items).

To make things clearer with an example, if `xmin, xmax = -1, 1`,  `ymin, ymax = -1, 1`, and `N=3`, the list returned should be:
```Python
[[mandelbrot( 1 - 1j), mandelbrot( 1 + 0j), mandelbrot( 1 + 1j)],
 [mandelbrot( 0 - 1j), mandelbrot( 0 + 0j), mandelbrot( 0 + 1j)],
 [mandelbrot(-1 - 1j), mandelbrot(-1 + 0j), mandelbrot(-1 + 1j)]]
```

### Parallelizing with static distribution of work

Write a function called `mandelbrot_static(xmin, xmax, ymin, ymax, N=100)` that generates an image of the Mandelbrot set based on the same arguments as `mandelbrot_serial`. In this case, however, the work of calling `mandelbrot` multiple times should be parallelized by evenly distributing the calls over a number of processes (using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) module). For example, if two processes are being used, the top half of the image could be evaluated by one process and the bottom half by the other. Your function should use as many CPU cores as are available on your machine, but the logic should be general enough to work with any number of processes. As with `mandelbrot_serial`, the function should return a list of length N for which each item is itself a list of length N.

### Parallelizing with dynamic load balancing

Write a function called `mandelbrot_dynamic` that generates an image of the Mandelbrot set in parallel by using a [Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool) of processes to which "tasks" are submitted. Each task should be a single call to the `mandelbrot` function. This function should also have the same arguments and return value as `mandelbrot_serial`.

### main() function

The `main()` function should pick suitable values for `xmin`, `xmax`, `ymin`, and `ymax`. See [this website](http://www.atopon.org/mandel/) to explore the Mandelbrot set (the x,y range is displayed in the top-left corner of the image). Then, using these values, call each of the three image-generation functions and use the built-in [time](https://docs.python.org/3/library/time.html) module to measure how long it took to run each and print the elapsed time. Finally, use [imshow](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow) to plot one of the images (the image produced by each function should be the same!) and save it with [savefig](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig). You can experiment with the `cmap` argument of `imshow` to change the colormap that is used in the image; see [here](https://matplotlib.org/examples/color/colormaps_reference.html) for available colormaps.

Generating and saving the image should look something like:
```Python
import matplotlib.pyplot as plt

plt.imshow(image)
plt.savefig('mandelbrot.png')
```
