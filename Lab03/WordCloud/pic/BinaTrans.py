import cv2

path = "C:\C++_for_vscode\DataVisualize\echarts-wordcloud-master\example\mnls1.png"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Flower", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()