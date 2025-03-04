from nested_data import albums

SONGS_LISTS_INDEX = 3
SONG_NAME_INDEX = 1
while True:
    print("Please choose your album (invalid choice to exits):")
    for number, (name, artist, year, songs) in enumerate(albums):
        print(f"{number + 1}: {name}")

    choice = int(input())
    # if choice in range(1, len(albums) + 1):
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LISTS_INDEX]
    else:
        break
    print("Please choose your song name: ")
    for number, song in songs_list:
        print(f"{number}: {song}")
    song_choice = int(input())
    # if song_choice in range(1, len(songs_list) + 1):
    if 1 <= song_choice <= len(songs_list):
        print(f"Playing {songs_list[song_choice - 1][SONG_NAME_INDEX]}")
    else:
        print("They is no such song ")
    print("=" * 50)
    input()
