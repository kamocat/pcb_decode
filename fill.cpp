#include <iostream>
#include <stack>
#include <opencv2/opencv.hpp>
using namespace cv;

bool Inside(uchar * p, int x, int xmax){
    if( x<0 || x>xmax){
        return false;
    }
    return (p[x] == 255);
}

struct span{
    int start, end, y, direction;
};

// scan-and-fill implementation from Wikipedia
// https://en.wikipedia.org/wiki/Flood_fill#Span_Filling
void flood(Mat img, int mark, int x, int y){
    int xmax = img.cols - 1;
    int ymax = img.rows - 1;
    std::stack <struct span> s;
    s.push({x,x,y, 1});
    while( !s.empty() ){
        struct span sp = s.top();
        s.pop();
        int x1 = sp.start;
        int x2 = sp.end;
        int y  = sp.y;
        int d  = sp.direction;
        if( x2 < x1 )
            continue; //empty span
        if( y<0 || y>ymax)
            continue; //y is out of range
        uchar *p = img.ptr<uchar>(y);
        int x = x1;
        sp.end = x1-1;
        // Fill to the left
        while (Inside(p, x-1, ymax)){
            p[x]=mark;
            --x;
        }
        sp.start = x;
        // Search above left
        s.push({sp.start, sp.end, y-d, -d});
        while (x < x2){
            x = sp.end + 1;
            // Fill to the right
            while (Inside(p, x, ymax)){
                p[x]=mark;
                ++x;
            }
            // Search below
            sp.end = x-1;
            s.push({sp.start, sp.end, y+d, d});
            // Continue searching designated span
            while (!Inside(p, x, ymax))
                ++x;
            sp.start = x;
        }
        // Search above right
        s.push({x2, sp.end, y-d, -d});
    }
    return;
}

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: flood_fill<Image_Path>\n");
        return -1;
    }
    Mat img;
    img = imread( argv[1], 1 );
    if ( !img.data )
    {
        printf("No image data \n");
        return -1;
    }
    int ymax = img.rows - 1;
    int xmax = img.cols - 1;
    cvtColor(img, img, COLOR_BGR2GRAY);
    flood(img,128,296,250);
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", img);
    waitKey(0);
    return 0;
}
