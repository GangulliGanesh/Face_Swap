1.Create a new environment.
Go to Face_Swap and run sudo chmod +x install.sh


2.Run ./install.sh , Run python UploadTest.py --a link will pop up on the terminal which will lead you to a web API.

3.Base images and mugshots can be found in base folder and patch respectively.

4.Line 11 of remove_bg.py has the API key.
To get a new Key sign in here https://www.remove.bg/users/sign_up 
Then log in.Go to https://www.remove.bg/api click on "Get API Key" button. Copy 25 charecter key and place in line 11.

5.Double click on destroy.sh to delete all the files inside the static folder.(optional)

6.SAMPLE OUTPUT
<p align="center">
<em>Base Image</em>
</p>
<p align="center">
<img src="https://github.com/Aakroat/Face_Swap/blob/master/images/base/akshay_base.jpg"> 
</p>
<p align="center">
<em>Patch Image</em>
</p>
<p align="center">
<img src="https://github.com/Aakroat/Face_Swap/blob/master/images/patch/barak-obama.jpg" width=300>  
</p>  
<p align="center">
<em>Swaped Image</em>
</p>
<p align="center">
<img src="https://github.com/Aakroat/Face_Swap/blob/master/bo.png">
</p>


