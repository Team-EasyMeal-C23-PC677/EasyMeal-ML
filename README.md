<h1 align="center"> EasyMeal-ML </h1> <br>
<p align="center">
  <a>
    <img alt="EasyMeal" title="EasyMeal" src="https://github.com/Team-EasyMeal-C23-PC677/.github/assets/97155903/6310e3f9-e4ee-4509-a193-b1036aac0b1f.png">
  </a>
</p>

<p align="center">
  Don't know what to cook? We got you!
</p>

# 🤖 Introduction

🍽 EasyMeal is an application which help users by giving recipe recommendations based on ingredients they have. This application also helps user find out ingredients they don't know simply by uploading image(s) of the ingredient(s).

# ℹ About Repository

This repository is dedicated for machine learning development. Dataset, models, etc. are stored in this repository.

# 🛠 Model

We are using mobilenet_1.00_224 with some additional layers. Here are the summary of the model.

 Layer (type)                Output Shape              Param #   
=================================================================
 mobilenet_1.00_224 (Functio  (None, 7, 7, 1024)       3228864   
 nal)                                                            
                                                                 
 global_average_pooling2d (G  (None, 1024)             0         
 lobalAveragePooling2D)                                          
                                                                 
 dense (Dense)               (None, 1280)              1312000   
                                                                 
 dense_1 (Dense)             (None, 3)                 3843      
                                                                 
=================================================================
Total params: 4,544,707
Trainable params: 1,315,843
Non-trainable params: 3,228,864
_________________________________________________________________

