# Chatot Corgiman

## Table of content
1. [English - Tiếng Anh](#english)
2. [Vietnamese - Tiếng Việt](#vietnam)

### English (Tiếng Anh) <a name="english"></a>
#### a. Introduction
Introducing Corgiman, the simple yet efficient chatbot designed to answer your questions with ease. Built using the Flask framework and utilizing MongoDB for data storage, Corgiman is the perfect tool for those looking for a fun and engaging conversation. Despite its simplicity, this project is a great opportunity to practice and showcase what has been learned in the field of chatbot development. So sit back, ask away, and enjoy the conversation with Corgiman!

#### b. Quick start

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
> First, we will create new database with name is "chatbot" and collection "data_train" <br>
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

###### - Go to tab "Training data" and training the model
> Before 
![image](https://user-images.githubusercontent.com/93339285/216780523-9e357f40-bee5-4532-b640-4c6eabde2aa2.png)
> After 
![image](https://user-images.githubusercontent.com/93339285/216780697-b092cf2b-0442-4674-87f8-ffbd3a03ab66.png)

###### - After that, you can logout and register another account
> Only one account is admin, the rest will all be users

###### - Enjoy
> Use can type or speak
![image](https://user-images.githubusercontent.com/93339285/216781007-8f9e4171-7b4e-4f20-b88d-6e8628b5a626.png)




### Vietnamese (Tiếng Việt) <a name="vietnam"></a>
