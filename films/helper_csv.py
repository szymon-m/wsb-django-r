movie_list = []
x = 0

with open('csv_data/movies.csv', encoding="utf-8") as f:
    for row in f.readlines()[1:]:
        columns = row.split(',')

        if x<5:

            #Movies.objects.create(title=columns[1])
            print(columns[1])
            print(type(columns[1]))
            x += 1
        # movie_id = columns[0].split('/')[4]
        # genres = columns[1][:-1]
        # movie_list.append(movie_id)


    usr = []

with open('csv_data/ratings.csv', encoding="utf-8") as f:
    for row in f.readlines()[1:]:
        columns = row.split(',')

        usr.append(int(columns[0]))

            # if x < 5:
            #
            #     response += columns[0] + ' : ' + columns[1] + '<br>'
            #     m = Movie(movieid=columns[0], title=columns[1])
            #     m.save()
            #     x += 1
            #
            # response += '\n</body></html>'

usr = sorted(usr, reverse=True)

print(usr[0])