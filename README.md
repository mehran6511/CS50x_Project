# Human Skin Detection Web App
#### Video Demo:  <https://youtu.be/jRIt8jxDxzY>
#### Description:
The Human Skin Detection Web App is a project that aims to detect human skin from uploaded images. The project was authored by Mehran Moein, who also provided a reference for the concept of skin detection using RGB, HSV, and YCbCr color models.

The web app was created using Python and the Flask framework. It leverages the OpenCV library for image manipulation and analysis. The app allows users to upload an image from their local device and then runs a skin detection algorithm to identify and highlight areas of the image that contain human skin.

When a user first accesses the web app, they are directed to the homepage, which features a button to upload an image. Once an image is uploaded, the app uses the Flask framework to handle the file transfer, ensuring that only valid image files are accepted. If an invalid file is uploaded, the user is notified and prompted to try again.

Once a valid image is uploaded, the app reads the image file using OpenCV and converts it to different color models – RGB, HSV, and YCbCr. Each of these models handles color information differently, so analyzing an image in multiple color spaces provides more accurate detection of human skin.

Next, the app splits the image into individual color channels (i.e., red, green, and blue for RGB). It then applies pre-defined thresholds to these channels to determine which pixels likely contain skin. For example, if the red channel value is greater than 95, the green channel value is greater than 40, and the blue channel value is greater than 20, then the pixel is considered skin-like.

After identifying skin regions in the image, the app creates a new image that highlights those areas. The app merges the red, green, and blue color channels that correspond to the detected skin regions and saves the resulting image as a JPEG file. The app also saves the file to the Flask app's static folder, making it accessible to the user.

Finally, the app loads a "show" page that displays the original uploaded image alongside the skin detection result image. The user can then compare the two images side-by-side to see which areas were detected as skin.

The app is designed to be run locally on a user's machine or a web server that supports Python and Flask. The code is open source and available on GitHub, making it easy for other developers to contribute and modify the app. The app itself is straightforward and simple to use, making it an excellent tool for anyone who needs to quickly identify regions of human skin in an image.

In conclusion, the Human Skin Detection Web App is a useful tool for anyone who needs to identify skin regions in a digital image. The app leverages multiple color models and pre-defined thresholds to provide accurate and reliable detection results. The app is simple to use and easy to run, making it an excellent choice for developers and non-technical users alike.