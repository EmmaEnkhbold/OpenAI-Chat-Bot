import openai

openai.api_key = "insert-personal-openai-key-here"

def chatBot(question)
  #initialize OpenAI object
  response = openai.Completion.create(
    #latest update
    model="gpt-4"
    #conversation history
    messages = [
          {"role": "system", "content": "You are a personal assistant."},
          {"role": "user", "content": question}
      ]
  )
  #removes whitespace from the first item from the API list
  return response.choices[0].message.content.strip()

#run the file
if __name__ == "__main__":
  while True:
      userInput = input("User: ")
      #user key to exit the loop
      if userInput.lower() == "done":
          break
      #OpenAI response
      response = chatBot(userInput)
      print("Personal Assistant:", response)
