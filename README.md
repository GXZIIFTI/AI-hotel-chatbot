# AI-hotel-chatbot
Amazon Lex is a service for building conversational interfaces into any application using voice and text, enabling you to add sophisticated, natural language chatbots to your applications.


I used Amazon Lex to create a hotel chatbot and used AWS Lambda to connect with it ensuring a smooth serverless workflow and also for the calling of the functions.

At first, I went to Lex and created a new intent named ‘bookIntent’. An intent represents an action that fulfills a user’s request. I started with some basic sample utterances to help the chatbot understand user input. This is useful as the Lex Chatbot knows how to respond to user inputs like this.

![image](https://github.com/user-attachments/assets/6f5c7cbb-1067-423b-8182-8bc730291328)

 
As you can see there is some colored information inside the curly brackets, and these are called slots. Slots are information that a bot needs to fulfill the intent. For example, we cannot put a specific number for the nights we stay in as they can vary. Slots come in handy as these are used for the information that the bot needs in order to further process the booking.

 ![image](https://github.com/user-attachments/assets/7cdcbcd0-85ed-41df-8e34-b73a4959d3e5)


There are also slot types that can help the bot to understand what type of input they should expect from the user and a prompt for them to ask about. Note that the slots need to be arranged in order as Lex follows a specific sequence for the information it needs from the user.

 ![image](https://github.com/user-attachments/assets/df7685b7-d39f-4dc2-9d82-dde981259eec)

You can also create custom slot types for better understanding such as the ‘RoomType’ slot shown above. The prompt section is for what the chatbot will ask the user for the specific information it wants to gather.

![image](https://github.com/user-attachments/assets/c9efcc2a-848e-4dbd-a7a2-5b62aa1d87de)

This is a custom slot made with slot type values which are some information to help the machine learning model recognize it. I added the 4 types of rooms as the values and restricted the type to just ask for the slot value. If I used to expand values, lex might have taken the wrong word input and put it as the type of room the user wants. Restricting is also good for this case as whenever the user types something wrong, the chatbot will ask the question again.

![image](https://github.com/user-attachments/assets/e4d37b38-1a9a-4b36-8dea-afc246848a46)
 
This is the confirmation tab where you can customize the prompts for final confirmation before fulfilling the request. Fulfillment is connected with a Lambda function to ensure successful or unsuccessful fulfillment. Save the intent so that every progress is saved.

Now, we have to connect it with AWS Lambda. To do that I created a new Lambda function named ‘Hotel Booking Lambda’.AWS Lambda is a serverless compute service for running code without having to provision or manage servers. I used Python for this project

In order to connect it,I went to the alias section of Deployment in Lex and put my Alias language support source as the lambda function I just created. This will connect your AWS lambda function to the chatbot.
 
![image](https://github.com/user-attachments/assets/d5802de0-da91-4f39-9374-7a06e31bad4d)

Save changes and build and run the chatbot. There should be an error as we have not put anything into the lambda function yet.

 ![image](https://github.com/user-attachments/assets/6dc6fa74-d727-4c26-89d0-a62ee03eaf54)

Here I used a quick hack to help me speed up my process. Since there is a lot of code to write for the lambda function, I went to monitor my lambda function using AWS CloudWatch logs as it will show me the event that took place while incurring my Lambda function.
 
![image](https://github.com/user-attachments/assets/b20d4856-7154-4e05-82fc-046147915b52)

As we can see, there is Python code written over here. I just copied the whole code and put it in a Python formatting website to arrange the order. By using that, I can easily understand any errors I have in my code.

I took some help from AWS Documentations and a GitHub repo (https://github.com/PradipNichite/Youtube-Tutorials/blob/main/Amazon_Lex/Part2.py), implemented my learnings, and added more stuff to fit my conditions. I deployed the code in Lambda and then had to test things to ensure everything worked properly. This part can be problematic due to code changes which may cause an error, so I made sure to check CloudWatch logs time after time to check my errors. I added my AWS Lambda code in my repo

I also made an Amazon Lex v2 Model Cards for the type of rooms since it would look better as an interface. You can do this my going to the slot information and on **advanced options** you will find **slot prompts** where you can add the type of prompt you want to use. Add a model card and then put the buttons you want the modle cars to show.

![image](https://github.com/user-attachments/assets/99e0cf6c-faa8-4243-8644-de3343dac132)


The draft conversation flow looks like this.

![image](https://github.com/user-attachments/assets/99a40d47-975f-4485-bc37-4f3b61e9837e)

![image](https://github.com/user-attachments/assets/0a2036ae-2125-48a9-a676-d331bbb7824a)

![image](https://github.com/user-attachments/assets/5cd93a39-f069-49e5-99dd-bc4fe9b4d1ad)

![image](https://github.com/user-attachments/assets/19307bda-eb8e-455a-a72b-8489b56bee6c)

This is just a demo conversation for my AI hotel chatbot. It is also very easy to make more improvements using AWS services like Lambda, Lex, S3 etc. and you can link it to an external website like Kommunicate as well.




