import matplotlib.pyplot
import multiprocessing
import time

def mandelbrot(c, max_iterations=100):
    '''evaluate iterations'''
    counter = 0
    def determine(x,c,max_counter):
        nonlocal counter
        counter += 1
        z = x**2+c
        if abs(z)>2:
            return counter
        elif counter == max_counter:
            return 0
        else:
            return determine(z,c,max_counter)
    return determine(0,c,max_iterations)

def mandel_output(c, pos,output, max_iterations=100):
    output.put((pos,mandelbrot(c, max_iterations)))

def mandelbrot_serial(xmin, xmax, ymin, ymax, N=100):
    man_set = []
    for y in range(N):
        subitem = [mandelbrot(xmin+x*(xmax-xmin)/(N-1)+(y*(ymin-ymax)/(N-1)-ymin)*1j) for x in range(N)]
        man_set.append(subitem)
    return man_set

def mandelbrot_static(xmin, xmax, ymin, ymax, N=100):
    result = multiprocessing.Queue(N)

    man_set = []
    for y in range(N):
        processes = []
        for x in range(N):
            p = multiprocessing.Process(target=mandel_output, args = (xmin+x*(xmax-xmin)/(N-1)+(y*(ymin-ymax)/(N-1)-ymin)*1j,x,result))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        # for p in processes:
        answer = [result.get() for p in processes]
        answer.sort()
        answer = [item[1] for item in answer]
        man_set.append(answer)

    return man_set

def mandelbrot_dynamic(xmin, xmax, ymin, ymax, N=100):
    pool = multiprocessing.Pool(4)
    man_set = multiprocessing.Queue(N)
    for y in range(N):
        subitem = pool.map(mandelbrot, [xmin+x*(xmax-xmin)/(N-1)+(y*(ymin-ymax)/(N-1)-ymin)*1j for x in range(N)])
        man_set.put(subitem)
    pool.close()
    pool.join()
    answer = []
    while not man_set.empty():
        answer.append(man_set.get())
    return answer


if __name__ == "__main__":

    xmin = -2.25
    xmax = 0.75
    ymin = -1.5
    ymax = 1.5
    N = 6

    serial_start = time.time()
    print(mandelbrot_serial(xmin,xmax,ymin,ymax,N))
    serial_end = time.time()
    print(f'Serial Function takes {serial_end-serial_start} seconds')

    static_start = time.time()
    print(mandelbrot_static(xmin,xmax,ymin,ymax,N))
    static_end = time.time()
    print(f'Static Fuction takes {static_end-static_start} seconds')

    dynamic_start = time.time()
    print(mandelbrot_dynamic(xmin,xmax,ymin,ymax,N))
    dynamic_end = time.time()
    print(f'Dynamic Function takes {dynamic_end-dynamic_start} seconds')


    im = matplotlib.pyplot.imshow(mandelbrot_dynamic(xmin,xmax,ymin,ymax,N),'nipy_spectral')
    matplotlib.pyplot.savefig('mandelbrot.png')
    matplotlib.pyplot.show()
