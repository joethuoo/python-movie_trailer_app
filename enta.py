import fresh_tomatoe
import media

toy_story = media.Movie("Avatar","A story of a boy","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=QGfhS1hfTWw")

batman = media.Movie("BatmanVsSuperman",
                      "Vigilante on  the prow to kill superman",
                     "http://images-cdn.moviepilot.com/images/c_fill,h_876,w_1600/t_mp_quality/tj9qdllwbe1ulg3svl8q/new-batman-v-superman-promo-teases-a-link-to-nolan-s-the-dark-knight-connection-to-th-835181.jpg",
                    "https://www.youtube.com/watch?v=BvP4RIqSbiw")

captain = media.Movie("CaptainAmerica",
                      "SuperHeroes disagree on saving the world",
                      "http://static.comicvine.com/uploads/original/11/116475/3055392-ult.+cap.jpg",
                      "https://www.youtube.com/watch?v=dKrVegVI0Us")

deadpool = media.Movie("DeadPool",
                       "Funny Vigilante",
                       "http://cdn.neatorama.com/jill/THE-LEGEND-OF-DEADPOOL.jpg",
                       "https://www.youtube.com/watch?v=CnLGJHtdH1w") 

movies = [toy_story,batman,captain,deadpool]

fresh_tomatoe.open_movies_page(movies)


















