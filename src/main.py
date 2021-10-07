from optimizer import Recommender

if __name__=='__main__':
    list_music_time = [257, 229, 266, 226, 278, 220, 273, 271, 206, 284, 187, 194, 201, 186, 278, 274, 195, 288, 181, 230]

    recommender = Recommender()
    list_selected_index = recommender.get_selected_music_index(list_music_time)
    print(list_selected_index)
    for l in list_selected_index:
        print(sum([list_music_time[i] for i in l]))
