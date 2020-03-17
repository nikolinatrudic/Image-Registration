
import cv2
import time
import matplotlib.pyplot as plt
import numpy as np

par_fx = 3
par_fy = 1.5

img = cv2.imread('calb.png', cv2.IMREAD_COLOR)

inter_nearest_time = []
inter_linear_time = []
inter_area_time = []
inter_cubic_time = []
inter_lanczos_time = []
for i in range(100):
	t = time.time()
	res_nearest = cv2.resize( img, None, fx = par_fx, fy = par_fy, interpolation = cv2.INTER_NEAREST )
	inter_nearest_time.append(time.time() - t)
	t = time.time()
	res_linear = cv2.resize( img, None, fx = par_fx, fy = par_fy, interpolation = cv2.INTER_LINEAR )
	inter_linear_time.append(time.time() - t)
	t = time.time()
	res_area = cv2.resize( img, None, fx = par_fx, fy = par_fy, interpolation = cv2.INTER_AREA )
	inter_area_time.append(time.time() - t)
	t = time.time()
	res_cubic = cv2.resize( img, None, fx = par_fx, fy = par_fy, interpolation = cv2.INTER_CUBIC )
	inter_cubic_time.append(time.time() - t)
	t = time.time()
	res_lanczos4 = cv2.resize( img, None, fx = par_fx, fy = par_fy, interpolation = cv2.INTER_LANCZOS4 )
	inter_lanczos_time.append(time.time() - t)

times = [inter_nearest_time, inter_linear_time, inter_area_time, inter_cubic_time, inter_lanczos_time]
method_names = ['Inter nearest', 'Inter linear', 'Inter area', 'Inter cubic', 'Inter lanczos']

avg_of_times = []
for item in times:
	avg_of_times.append(np.average(item))

plt.bar(method_names, avg_of_times)
plt.show()

#I am showing just original photo and result from one of the methods

cv2.imshow('Original',img)
cv2.imshow( 'Resampled nearest', res_nearest )
#cv2.imshow( 'Resampled linear', res_linear )
#cv2.imshow( 'Resampled area', res_area )
#cv2.imshow( 'Resampled cubic spline', res_cubic )
#cv2.imshow( 'Resampled Lanczos', res_lanczos4 )

cv2.waitKey(0)
cv2.destroyAllWindows()
