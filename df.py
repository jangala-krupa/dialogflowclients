import dialogflow_v2beta1 as dialogflow
import pandas as pd
import dialogflow_v2 as dialogflow
project_id = raw_input("Please enter your project I'd")
print "HELLO! WELCOME TO DDIALOGFLOW! PLEASE SELECT ONE OF THE FOLLOWING OPTIONS"
print "1. Create an intent\n"
print "2. List of all existing entities\n"
choice= eval(raw_input())
def list_intents(project_id):
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)

    intents = intents_client.list_intents(parent)

    for intent in intents:
        print('=' * 20)
        print('Intent name: {}'.format(intent.name))
        print('Intent display_name: {}'.format(intent.display_name))
        print('Action: {}\n'.format(intent.action))
        print('Root followup intent: {}'.format(
            intent.root_followup_intent_name))
        print('Parent followup intent: {}\n'.format(
            intent.parent_followup_intent_name))

        print('Input contexts:')
        for input_context_name in intent.input_context_names:
            print('\tName: {}'.format(input_context_name))

        print('Output contexts:')
        for output_context in intent.output_contexts:
            print('\tName: {}'.format(output_context.name))
def create_intent(project_id, display_name, training_phrases_parts,message_texts):
    """Create an intent of the given intent type."""
    import dialogflow_v2 as dialogflow
    try :
      intents_client = dialogflow.IntentsClient()

      parent = intents_client.project_agent_path(project_id)
      training_phrases = []
      for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
      text = dialogflow.types.Intent.Message.Text(text=message_texts)
      message = dialogflow.types.Intent.Message(text=text)

      intent = dialogflow.types.Intent(
        display_name=display_name,training_phrases=training_phrases,
        messages=[message])
      parent_response = intents_client.create_intent(parent, intent)
      training_phrases_parts1= ["yes","yep","ok","sure"]
      training_phrases1 = []
      for training_phrases_part1 in training_phrases_parts1:
        part1 = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part1)
        training_phrase1 = dialogflow.types.Intent.TrainingPhrase(parts=[part1])
        training_phrases1.append(training_phrase1)
      message_texts1=["ok thanks"]
      text1 = dialogflow.types.Intent.Message.Text(text=message_texts1)
      message1 = dialogflow.types.Intent.Message(text=text)    
      intent = dialogflow.types.Intent(
        display_name="book-follow_up-intent_yes",training_phrases=training_phrases1,
        messages=[message1],parent_followup_intent_name= parent_response.name)
      response1 = intents_client.create_intent(parent, intent)
      training_phrases_parts2= ["no","nope","not","not now"]
      training_phrases2 = []
      for training_phrases_part2 in training_phrases_parts2:
        part2 = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part2)
        training_phrase2 = dialogflow.types.Intent.TrainingPhrase(parts=[part2])
        training_phrases2.append(training_phrase2)
      message_texts2=["ok thanks see you soon"]
      text2 = dialogflow.types.Intent.Message.Text(text=message_texts2)
      message2 = dialogflow.types.Intent.Message(text=text)    
      intent = dialogflow.types.Intent(
        display_name="book-follow_up-intent_no",training_phrases=training_phrases2,
        messages=[message2],parent_followup_intent_name= parent_response.name)
      response2 = intents_client.create_intent(parent, intent)
      
      print('Intent created: {}'.format(parent_response, response1, response2))
    except Exception as e:
       print ("Intent already exists!", e)
if choice == 1:
 display_name = raw_input("Enter the intent name!")
 create_intent(project_id,display_name, training_phrases_parts=["buy a ticket","book a ticket"], message_texts=["ok thanks"])
elif choice == 2:
  list_intents(project_id)