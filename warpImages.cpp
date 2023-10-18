/**
* warpImages.cpp
*/

#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/calib3d.hpp"
#include <vector>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;
using namespace cv;


static void onMouse(int event, int x, int y, int, void*);
Mat warping(Mat image, Size warped_image_size, vector< Point2f> srcPoints, vector< Point2f> dstPoints);
std::vector<std::string> split(std::string strToSplit, char delimeter);

String labels[4] = { "TL","TR","BR","BL" };
string files[5] = { "bc_cover.jpg", "bo_cover.jpg","fourth_cover.jpg","greta_cover.jpg", "rd_cover.jpg" };
int num_files = (int) sizeof(files)/sizeof(files[0]);
string warpDir= "/home/fred/Pictures/WARP_Images";
string warpFilename;
string bgFilename = "/home/fred/Pictures/TIMECover/lena.jpg";
Mat bg_image = imread(bgFilename);


int main(int argc, char** argv)
{
    CommandLineParser parser(argc, argv, "{@input| ../data/right.jpg |}");
    string filedir = parser.get<string>("@input");

    for (int idx = 0; idx < num_files; idx++)
    {
        vector< Point2f> roi_corners;
        vector< Point2f> dst_corners(4);

        std::vector<std::string> rootvec = split(files[idx], '.');
        string rootname = rootvec[0];
        warpFilename = "/warp_" + rootname;
        Mat original_image = imread( filedir + "/" + files[idx] );
        cout << "rootname=" << rootname << endl;
        cout << "filedir/files[idx]=" << filedir + "/" + files[idx] << endl;

        roi_corners.push_back(Point2f( (float)(1), (float)(1) ));      //TL
        roi_corners.push_back(Point2f( (float)(original_image.cols - 1), (float)(1) ));    //TR
        roi_corners.push_back(Point2f( (float)(original_image.cols - 1), (float)(original_image.rows - 1) ));    //BR
        roi_corners.push_back(Point2f( (float)(1), (float)(original_image.rows - 1) ));   //BL

        int warp_idx = 0;
        Mat warped_image;
        for (unsigned int k = 0; k < 4; k++)
        {
            int keep_token0, keep_token1, keep_token2, keep_token3;

            if (k == 0 && (k % 1 == 0) )
            {
                keep_token0 = 1; keep_token1 = 0; keep_token2 = 0; keep_token3 = 0;
            }
            if (k == 1 && (k % 2 == 1) )
            {
                keep_token0 = 0; keep_token1 = 1; keep_token2 = 0; keep_token3 = 0;
            }
            if (k == 2 && (k % 3 == 2) )
            {
                keep_token0 = 0; keep_token1 = 0; keep_token2 = 1; keep_token3 = 0;
            }
            if (k == 3 && (k % 4 == 3) )
            {
                keep_token0 = 0; keep_token1 = 0; keep_token2 = 0; keep_token3 = 1;
            }

            stringstream ks;
            ks << k;
            string k_str = ks.str();

            for (unsigned int i = 0; i < 10; i++, warp_idx+=3)
            {
                int warp0 = keep_token0 * warp_idx;
                int warp1 = keep_token1 * warp_idx;
                int warp2 = keep_token2 * warp_idx;
                int warp3 = keep_token3 * warp_idx;

    		    dst_corners[0].x = warp0 + 1;   //0;
    		    dst_corners[0].y = warp0 + 1;   //0;
                dst_corners[1].x = roi_corners[1].x - warp1;
                dst_corners[1].y = warp1 + 1;  //0;
                dst_corners[2].x = roi_corners[2].x - warp2;
                dst_corners[2].y = roi_corners[2].y - warp2;
    		    dst_corners[3].x = warp3 + 1;   //0;
                dst_corners[3].y = roi_corners[3].y - warp3;

    		    Size warped_image_size = Size(cvRound(dst_corners[2].x), cvRound(dst_corners[2].y));

    		    Mat H = findHomography(roi_corners, dst_corners); //get homography

    		    warpPerspective(original_image, warped_image, H, warped_image_size); // do perspective transformation

    		    stringstream ss;
    		    ss << i;
    		    string str = ss.str();

                Mat new_bg_image;
                bg_image.copyTo(new_bg_image);

                double x_rand = ((double) rand() / (RAND_MAX));
                double y_rand = ((double) rand() / (RAND_MAX));

                int x_shift = (int) warped_image.cols * x_rand;
                int y_shift = (int) warped_image.rows * y_rand;

                if (x_shift + warped_image.cols > new_bg_image.cols )
                    x_shift -= (x_shift + warped_image.cols - new_bg_image.cols);

                if (y_shift + warped_image.rows > new_bg_image.rows )
                    y_shift -= (y_shift + warped_image.rows - new_bg_image.rows);

                warped_image.copyTo(new_bg_image(cv::Rect(x_shift, y_shift, warped_image.cols, warped_image.rows)));

    		    //imwrite(warpDir + warpFilename + k_str + "_" + str + ".jpg", warped_image);
                imwrite(warpDir + warpFilename + k_str + "_" + str + ".jpg", new_bg_image);

                new_bg_image.release();
            }
        }
        roi_corners.clear();
    }

    return 0;
}


std::vector<std::string> split(std::string strToSplit, char delimeter)
{
    std::stringstream ss(strToSplit);
    std::string item;
    std::vector<std::string> splittedStrings;
    while (std::getline(ss, item, delimeter))
    {
       splittedStrings.push_back(item);
    }
    return splittedStrings;
}
