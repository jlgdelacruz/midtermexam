import webexteamssdk

access_token = "ZDE2MWU2MGUtZDc5Ny00NjRlLWFlN2MtMTFhNzNjM2ExM2RjZjg2NTFjZTMtZmIz_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d"
webex = webexteamssdk.WebexTeamsAPI(access_token=access_token)

room_name = input("Enter room name: ")
message = input("Enter welcome message: ")

room = webex.rooms.create(title=room_name)

webex.messages.create(roomId=room.id, text=message)

print(f"Room '{room_name}' created!")

def add_participants(room_id):
    participant_emails = []
    while True:
        email = input("Enter a participant's email address (or 'done' to finish): ")
        if email.lower() == 'done':
            break
        participant_emails.append(email)
    
    for email in participant_emails:
        webex.memberships.create(roomId=room_id, personEmail=email)
        print(f"Added {email} to the room")

add_participants(room.id)

messageList = webex.messages.list(roomId=room.id)

print("Messages in the room:")
for message in messageList:
    print(f"Message ID: {message.id}, Text: {message.text}")

messageDelete = input("Enter message ID to delete: ")

webex.messages.delete(messageId=messageDelete)
print(f"Message with ID {messageDelete} deleted!")