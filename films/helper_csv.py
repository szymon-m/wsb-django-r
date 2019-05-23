movie_list = []
x = 0

with open('csv_data/movies.csv', encoding="utf-8") as f:
    for row in f.readlines()[1:]:
        columns = row.split(',')

        if x<5:
            print(columns[1])
            x += 1
        # movie_id = columns[0].split('/')[4]
        # genres = columns[1][:-1]
        # movie_list.append(movie_id)
