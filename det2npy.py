from numpy import genfromtxt, save
import os.path

# path = './resources/detections/MOT16_test_nofeature/'
# path = './MOT16/test/MOT16-06/det/'
path = './bellevue/ne8/det/'
data = genfromtxt(os.path.join(path, 'det.txt'), delimiter=',')
save(os.path.join(path, 'det.npy'), data)