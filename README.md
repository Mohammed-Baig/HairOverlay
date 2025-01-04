Remake of an old project, exploring a variety of methods to simulate what a certain hairstyle would look like on the user:
1. HairOverlay-1-Static: Overlays the hairstyle onto a set location in the video frame, lets the user line up the angle, which they may be more familiar with from other applications
2. HairOverlay-2.1 and 2.2-DynamicLandmarks: uses two different facial keypoint detection models to get location data to overlay the hair onto, allowing for real time tracking
3. HairOverlay-3.1 and 3.2-Triangulation: Uses the facial detection keypoints from the previous 2.2, alongside methods like delaunay triangulation to swap the users face onto the face of the hairstyles model; seamlessly, to make it easier to see what the full hairstyle would look on the head of the user
4. HairOverlay-4-ML: Uses Machine Learning to perform the previous task faster and more naturally
