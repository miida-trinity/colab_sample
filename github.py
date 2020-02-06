# -*- coding: utf-8 -*-
"""github.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qPFG_OQeKSkDPPtodjzJm5yH4TVaf-0b

# GitHubとの連携
Google ColaboratoryとGitHubの連携について学びましょう。

## ●Githubとは？
GitHubは、今や開発者にとってなくてはならないサービスです。  
「Git」は、プログラミングによるサービス開発の現場などでよく使われている「バージョン管理システム」です。  
そして、GitHubは、Gitの仕組みを利用して、世界中の人々が自分のプロダクトを共有、公開することができるようにしたウェブサービス名です。  
GitHubで作成されたリポジトリ（貯蔵庫のようなもの）は、無料の場合誰にでも公開されますが、有料の場合は指定したユーザーのみがアクセスできるプライベートなレポジトリを作ることができます。  
GitHubは、TensorFlowやKerasなどのオープンソースプロジェクトの公開にも利用されています。

## ●ノートブックをGitHubで公開する
ノートブックをGitHubにアップすることにより、ノートブックを一般に公開したり、チーム内で共有することができます。  
GitHubで新しくレポジトリを作った上で、このノートブックをGitHubにアップしてみましょう。  
以下はダミーのコードです。
"""

import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import Adam

(x_train, t_train), (x_test, t_test) = cifar10.load_data()

batch_size = 32
epochs = 1
n_class = 10

t_train = keras.utils.to_categorical(t_train, n_class)
t_test = keras.utils.to_categorical(t_test, n_class)

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(n_class))
model.add(Activation('softmax'))

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

x_train = x_train / 255
x_test = x_test / 255

model.fit(x_train, t_train, epochs=epochs, batch_size=batch_size, validation_data=(x_test, t_test))