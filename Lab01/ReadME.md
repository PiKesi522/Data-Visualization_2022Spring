<center><h1>DataVisualize Lab 01</h1></center>

<center><h3>10192100571 俞辰杰</h3></center>

为了视觉效果，推荐使用Chrome缩放50%。



首先<u>输入聚类中心的数量K</u>**（基本功能1拓展）**，实验结果会根据K的数量产生变化

![image-20220327134118433](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327134118433.png)



点击图片实现<u>交互的上传图片</u>**（进阶功能1）**进行聚类

![image-20220327134848105](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327134848105.png)

在图像分析的时候加载loading界面![image-20220327134940219](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327134940219.png)



结果展示界面：

​	最上方呈现选中的图像，下方显示聚类的结果，包含<u>柱状图，饼图和散点图三种形式</u>**（基础功能3拓展）**

<img src="C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327141316012.png" alt="image-20220327141316012" style="zoom:80%;" />

1. 柱状图，X轴显示颜色；鼠标移动到饼图之上的时候，会显示<u>聚类的颜色和数量</u>**（基本功能2）**

   <img src="C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327141238793.png" alt="image-20220327141238793" style="zoom:50%;" />

2. 饼图，鼠标移动到饼图之上的时候，会显示<u>聚类颜色的颜色和数量</u>**（基本功能2）**：

<img src="C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327140258245.png" alt="image-20220327140258245" style="zoom: 50%;" />

3. 散点图，通过采样来显示图片的哪些像素属于哪一种分类。

   颜色与实际不符，为了使用更高对比度的颜色来展示结果

   <img src="C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327141051218.png" alt="image-20220327141051218" style="zoom:50%;" />



显示结果下方有切换样式按钮，<u>点击可在三种样式之间切换</u>**（进阶功能2）**

![image-20220327142145391](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327142145391.png)

网页右上角有刷新按钮，在实验完成后需要再次尝试可以点击**（进阶功能3）**

![image-20220327142946987](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327142946987.png)

聚类中心过多，或者某次聚类结果不好，产生聚类数量为0的聚类中心，此时会提醒并刷新界面**（进阶功能4）**

![image-20220327144055595](C:\Users\86008\AppData\Roaming\Typora\typora-user-images\image-20220327144055595.png)





如果实验无法正常进行，请参考文件夹内的**实验视频.mp4**
