# Chatot Corgiman

## Table of content
1. [English - Tiếng Anh](#english)
2. [Vietnamese - Tiếng Việt](#vietnam)

### 1. English (Tiếng Anh) <a name="english"></a>
#### a. Introduction
Introducing Corgiman, the simple yet efficient chatbot designed to answer your questions with ease. Built using the Flask framework and utilizing MongoDB for data storage, Corgiman is the perfect tool for those looking for a fun and engaging conversation. Despite its simplicity, this project is a great opportunity to practice and showcase what has been learned in the field of chatbot development. So sit back, ask away, and enjoy the conversation with Corgiman!

#### b. Key Features
> - Utilize dynamic training data for improved performance
> - Experience real-time communication through messaging
> - Conveniently send messages in both text and speech form
> - Receive messages in text and audio
> - Enjoy two distinct user roles, including administrator and regular user, for enhanced security and functionality.

#### c. Quick start

###### - Clone this repository
```
git clone https://github.com/Linhvjc/Corgiman.git
```

###### - Go to the project
```
cd Corgiman
```

###### - Installing Python Packages From a Requirements File
```
pip install -r requirements.txt
```

###### - Create new database and some collection in MongoDB compass
> First, you must have MongoDB compass in your computer, and then we will create new database with name is "chatbot" and collection "data_train" <br>
![image](https://user-images.githubusercontent.com/93339285/216780303-e1987400-fe2f-4f9b-8446-d295ac82e6e6.png)

> Next, we will create 3 more collections is "message", "message_no_response", "user"
> Double check after we finish, the database will display like this image below <br>
![image](https://user-images.githubusercontent.com/93339285/216780317-51ef2f8a-e66e-41ff-ae84-b985e4eb8984.png)


###### - Run this app in localhost
```
python web.py
```
> The command line window will appear as follows <br>
![image](https://user-images.githubusercontent.com/93339285/216780331-1feec63e-2276-4001-9cb7-6697c4914a7f.png)

###### - Visit http://localhost:5000/ and register with username is 'admin'
![image](https://user-images.githubusercontent.com/93339285/216780344-4101655d-4e41-458b-bd99-daab2fe5ce9d.png)

###### - Login as the account admin
![image](https://user-images.githubusercontent.com/93339285/216780249-a8fd6b81-6705-409f-9f18-d9b1f7f25a62.png)

###### - Go to tab "Train data" and training the model
> Before 
![image](https://user-images.githubusercontent.com/93339285/216780523-9e357f40-bee5-4532-b640-4c6eabde2aa2.png)
> After 
![image](https://user-images.githubusercontent.com/93339285/216780697-b092cf2b-0442-4674-87f8-ffbd3a03ab66.png)

###### - After that, you can logout and register another account
> Only one account is admin, the rest will all be users

###### - Enjoy
> Use can type or speak
![image](https://user-images.githubusercontent.com/93339285/216781007-8f9e4171-7b4e-4f20-b88d-6e8628b5a626.png)

#### d. Explanation
> - web.py - This file contains the source code for the Flask application. It is used to build a website that allows users to interact with the chatbot and has features such as login, registration, message history, and user message management. It uses Flask, Flask-SocketIO, and other modules to function.
> - requirements.txt - This is a file that contains the necessary libraries to install and run a software project.
> - Chatbot.py - This file contains the code to create a Chatbot. It reads data stored in the files words.pkl and classes.pkl, and loads the trained model from the chatbot_model.h5 file. It uses the functions clean_up_sentence, bag_of_word, and predict_class to process the input sentence and predict its label. Then, it uses the get_response function to search and return a response from the database.
> - training.py - This file is used to train a chatbot model to answer questions. The training results are stored, and the model is saved for future use.
> - db.py - This file contains functions for accessing the MongoDB database.
> - handle.py - This file serves as a module to manage, store, search, and process data in the program's database. 




### 2. Vietnamese (Tiếng Việt) <a name="vietnam"></a>
#### a. Giới thiệu
Giới thiệu đến Corgiman, chatbot đơn giản nhưng hiệu quả dùng để trả lời các câu hỏi của bạn một cách dễ dàng. Được xây dựng bằng Flask và sử dụng MongoDB để lưu trữ dữ liệu, Corgiman là công cụ hoàn hảo cho những người muốn trò chuyện vui vẻ và xả stress. Mặc dù đơn giản, dự án này là cơ hội tuyệt vời để tôi luyện tập và trình bày những gì đã học trong lĩnh vực trí tuệ nhân tạo. Hãy ngồi yên và tận hưởng cuộc trò chuyện với Corgiman!

#### b. Các tính năng chính
> - Sử dụng dữ liệu đào tạo linh hoạt để cải thiện hiệu suất
> - Trải nghiệm trao đổi thời gian thực qua tin nhắn
> - Gửi tin nhắn dễ dàng bằng văn bản và giọng nói
> - Nhận tin nhắn bằng văn bản hoặc âm thanh
> - Thưởng thức hai vai trò người dùng khác nhau, bao gồm quản trị viên và người dùng thông thường, để tăng cường bảo mật và tính năng.

#### c. Bắt đầu nhanh
###### - Tải về 
```
git clone https://github.com/Linhvjc/Corgiman.git
```

###### - Đến dự án đã được tải về
```
cd Corgiman
```

###### - Cài đặt tất cả gói python từ file requirements
```
pip install -r requirements.txt
```

###### - Tạo cơ sở dữ liệu với một vài bộ sưu tập trong MongoDB compass
> Trước hết, bạn phải có MongoDB Compass trên máy tính của mình, sau đó chúng ta sẽ tạo một cơ sở dữ liệu mới với tên là "chatbot" và bộ sưu tập "data_train". <br>
![image](https://user-images.githubusercontent.com/93339285/216780303-e1987400-fe2f-4f9b-8446-d295ac82e6e6.png)

> Sau đó, chúng ta sẽ tạo thêm 3 bộ sưu tập là "message", "message_no_response", "user". 
> Kiểm tra lại sau khi hoàn thành, cơ sở dữ liệu sẽ hiển thị như hình dưới đây.  <br>
![image](https://user-images.githubusercontent.com/93339285/216780317-51ef2f8a-e66e-41ff-ae84-b985e4eb8984.png)


###### - Chạy ứng dụng trên localhost.
```
python web.py
```
> Cửa sổ dòng lệnh sẽ xuất hiện như sau
![image](https://user-images.githubusercontent.com/93339285/216780331-1feec63e-2276-4001-9cb7-6697c4914a7f.png)

###### - Truy cập http://localhost:5000/ và đăng ký với tên đăng nhập là 'admin'.
![image](https://user-images.githubusercontent.com/93339285/216780344-4101655d-4e41-458b-bd99-daab2fe5ce9d.png)

###### - Đăng nhập với tài khoản admin
![image](https://user-images.githubusercontent.com/93339285/216780249-a8fd6b81-6705-409f-9f18-d9b1f7f25a62.png)

###### - Hãy đến tab "Train data" và đào tạo mô hình
> Before 
![image](https://user-images.githubusercontent.com/93339285/216780523-9e357f40-bee5-4532-b640-4c6eabde2aa2.png)
> After 
![image](https://user-images.githubusercontent.com/93339285/216780697-b092cf2b-0442-4674-87f8-ffbd3a03ab66.png)

###### - Sau đó, bạn có thể đăng xuất và đăng ký tài khoản khác.
> Chỉ có một tài khoản là quản trị viên, còn lại tất cả đều là người dùng.

###### - Sử dụng nó
> Bạn có thể gõ hoặc nói chuyện.
![image](https://user-images.githubusercontent.com/93339285/216781007-8f9e4171-7b4e-4f20-b88d-6e8628b5a626.png)


#### d. Giải thích
> - web.py - là một file chứa mã nguồn của ứng dụng Flask. Nó được sử dụng để xây dựng một trang web cho phép người dùng giao tiếp với chatbot và có các tính năng như đăng nhập, đăng ký, lịch sử tin nhắn và quản lý tin nhắn của người dùng. Nó sử dụng Flask, Flask-SocketIO và các module khác để hoạt động. 
> - requirements.txt - là một tập tin chứa các thư viện (library) cần thiết để cài đặt và chạy một dự án phần mềm.
> - Chatbot.py - chứa code để tạo một Chatbot. Nó đọc dữ liệu đã được lưu trữ trong file words.pkl và classes.pkl, và load mô hình đã huấn luyện từ file chatbot_model.h5. Nó sử dụng các hàm clean_up_sentence, bag_of_word và predict_class để xử lý câu văn đầu vào và dự đoán nhãn của câu đó. Sau đó, nó sử dụng hàm get_response để tìm kiếm và trả lại một câu trả lời từ cơ sở dữ liệu.
> - training.py - là file được sử dụng để huấn luyện một mô hình chatbot để trả lời câu hỏi. Kết quả huấn luyện được lưu trữ và mô hình được lưu lại để sử dụng trong tương lai.
> - db.py - là file chứa các hàm để truy cập vào cơ sở dữ liệu MongoDB.
> - handle.py - file này đóng vai trò là một module giúp quản lý, lưu trữ, tìm kiếm và xử lý dữ liệu trong cơ sở dữ liệu của chương trình.
