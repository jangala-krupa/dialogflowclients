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
def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    import dialogflow_v2 as dialogflow
    try :
      intents_client = dialogflow.IntentsClient()

      parent = intents_client.project_agent_path(project_id)
      training_phrases = []
      for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
      text = dialogflow.types.Intent.Message.Text(text=message_texts)
      message = dialogflow.types.Intent.Message(text=text)

      intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

      response = intents_client.create_intent(parent, intent)
      parent_followup_intent_name = "testing intent1"
      print('Intent created: {}'.format(response))
      #print ("follow up intent is{}".format(parent_followup_intent_name))
   # print training_phrases
    except Exception as e:
       print ("Intent already exists!")
if choice == 1:
 display_name = raw_input("Enter the intent name!")
 print ("enter number of training phrases")
 n = eval(raw_input())
 print ("enter the training phrases")
 tp_parts = []
 for tp in range(1,n+1):
  part = raw_input()
  tp_parts.append(part)
 print ("enter the number of responses")
 m = eval(raw_input())
 re_parts = []
 print ("enter the responses")
 for re in range(1,m+1):
  repart = raw_input()
  re_parts.append(repart)
 create_intent(project_id,display_name, training_phrases_parts=tp_parts, message_texts=re_parts)
elif choice == 2:
  list_intents(project_id)
