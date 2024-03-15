from __future__ import print_function
import numpy as np
import cv2
import open3d as o3d

ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
'''

def write_ply(fn, verts, colors):
    verts = verts.reshape(-1, 3)
    colors = colors.reshape(-1, 3)
    verts = np.hstack([verts, colors])
    with open(fn, 'wb') as f:
        f.write((ply_header % dict(vert_num=len(verts))).encode('utf-8'))
        np.savetxt(f, verts, fmt='%f %f %f %d %d %d ')

if __name__ == '__main__':
    print('loading images...')
    img1 = cv2.pyrDown(cv2.imread('view3.png'))
    img2 = cv2.pyrDown(cv2.imread('view4.png'))
    img3 = cv2.pyrDown(cv2.imread('view5.png'))
    img4 = cv2.pyrDown(cv2.imread('view6.png'))

    window_size = 5
    min_disp = 16
    num_disp = 160 - min_disp
    stereoLR = cv2.StereoSGBM_create(minDisparity=min_disp,
                                     numDisparities=num_disp,
                                     blockSize=5,
                                     P1=8 * 3 * window_size ** 2,
                                     P2=32 * 3 * window_size ** 2,
                                     disp12MaxDiff=1,
                                     uniquenessRatio=15,
                                     speckleWindowSize=100,
                                     speckleRange=32)

    stereoUD = cv2.StereoSGBM_create(minDisparity=min_disp,
                                     numDisparities=num_disp,
                                     blockSize=5,
                                     P1=8 * 3 * window_size ** 2,
                                     P2=32 * 3 * window_size ** 2,
                                     disp12MaxDiff=1,
                                     uniquenessRatio=15,
                                     speckleWindowSize=100,
                                     speckleRange=32)

    print('computing disparity for 1 and 2...')
    disp12 = stereoLR.compute(img1, img2).astype(np.float32) / 16.0

    print('computing disparity for 3 and 4...')
    disp34 = stereoUD.compute(img3, img4).astype(np.float32) / 16.0

    print('generating 3D point cloud...')
    h, w = img1.shape[:2]
    f = 0.8 * w
    Q = np.float32([[1, 0, 0, -0.5 * w],
                    [0, -1, 0, 0.5 * h],
                    [0, 0, 0, -f],
                    [0, 0, 1, 0]])

    points = cv2.reprojectImageTo3D(disp12, Q)
    colors = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    mask = disp12 > disp12.min()
    out_points = points[mask]
    out_colors = colors[mask]
    out_fn = 'out.ply'
    write_ply('out.ply', out_points, out_colors)
    print('%s saved' % 'out.ply')

    cv2.imshow('left', img1)
    cv2.imshow('disparity', (disp12 - min_disp) / num_disp)

    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("out.ply")
    print(pcd)
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd], width=650, height=650, left=20, top=20)

    cv2.waitKey()
    cv2.destroyAllWindows()
