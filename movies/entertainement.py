import media
import fresh_tomatoes

lord_of_the_rings = media.Movie(
    "The Lord of the Rings",
    "The former Fellowship of the Ring prepare for the final battle\
    for Middle Earth, while Frodo (Elijah Wood) & Sam (Sean Astin)\
    approach Mount Doom to destroy the One Ring.",
    "https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/4/1/410920150509-uau-posters-filmes-senhor-dos-aneis-lord-of-the-rings-1.jpg",  #noqa
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

harry_potter = media.Movie("Harry Potter",
    "Adventures of a young wizard",
    "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg",  #noqa
    "https://www.youtube.com/watch?v=772UlkDZSPY")

star_wars = media.Movie("Star Wars",
    "A star wars film of last Jedi",
    "http://sm.ign.com/t/ign_pt/gallery/s/star-wars-/star-wars-hidden-easter-eggs-in-the-last-jedi-poster_f4x6.640.jpg",  #noqa
    "https://www.youtube.com/watch?v=CbjyqkPyRf8")

spider_man = media.Movie("Spider Man",
    "Adventures of Spider Man - Homecoming",
    "http://oyster.ignimgs.com/wordpress/stg.ign.com/2017/05/Spiderman.jpg",  #noqa
    "https://www.youtube.com/watch?v=U0D3AOldjMU")

justice_league = media.Movie("Justice League",
    "Batman, Wonder Woman, Flash and others",
    "http://www.thescifiworld.com/PT/media/k2/items/cache/3756131af6e7f9af5f10fd1ac8678051_XL.jpg",  #noqa
    "https://www.youtube.com/watch?v=RWCQ22JyCL4")

avengers = media.Movie("The Avengers",
    "Avengers",
    "https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/9/6/969420150620-uau-posters-filmes-os-vindagores-avengers-herois.jpeg.jpg",  #noqa
    "https://www.youtube.com/watch?v=pPqUuXEzIP4")

movies = [lord_of_the_rings, harry_potter, star_wars, spider_man, justice_league, avengers]
fresh_tomatoes.open_movies_page(movies)
