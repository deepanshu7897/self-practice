import json
def load_data():
    try : 
        with open('youtube.txt','r') as file :
            test = json.load(file)
            #print( type (test))
            return test 
    except FileNotFoundError:
        return []
    
def  save_data_helper(videos):
    with open ('youtube.txt','w') as file :
        json.dump(videos,file)


def list_all_video(videos):
   print("*" * 70)
   for index , video in  enumerate(videos, start = 1):
       
       
       
       print(f"{index}. {video['name']} ,Duration: {video['time']}" )
   print("*" * 70)       
       

 
def add_video(videos):
   name = input("ENTER VIDEO NAME:")
   time = input("enter video time:")
   videos.append({'name': name  , 'time': time})
   save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index  = int(input("enter the video to update"))
    if 1 <= index <= len(videos):
        name = input("enter video name")
        time = input("enter video time")
        videos[index-1]= {'name': name , 'time': time}
        save_data_helper(videos)
    else :
        print("invalid index selected")    
    

def delete_video(videos):
    list_all_video(videos)
    index = input("enter the video number to be deleted")
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else : 
        print ("invalid video index selected")    

def main():
    videos = load_data()
    while True :
        print("\n youtube manmager")
        print("1. List all favourite video")
        print("2. Add youtube video")
        print("3. update a  youtube video detail")
        print("4.  delete a youtube video")
        print("5. exit the app")
        choice = input("enter your choice:")
        #print(videos)
        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3' :
                update_video(videos)    
            case '4':
                delete_video(videos)       
            case '5' :
                break  
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()       