from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>One Piece</title>
    <style>
        a:hover{
            color: gray;
        }
        a{
            padding: 10px;
            color: blue;
            font-size: 20px;
            text-decoration: none;
            font-family: Verdana;
        }
        ::placeholder
        {
          font-family: 'Times New Roman';
          font-size: 30px;
          font-style: initial;
          text-align: center;
        }
        input[type="submit"]:hover
        {
            border-width: 3px;
            border-color: black;
            background-color: gray;
        }
        input[type="text"]
        {
            border-radius: 25px;
            background-color: lightskyblue;
        }
        h1{
          font-family: Tahoma;
          color: crimson;
          border-color: black;
        }
        
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body style="background-color: black;">
    
        <div style="display: flex;">
            <div >
                <img src="across.webp" alt="" height="200px">
            </div>
            
            <div >
                <center>
                <a href="spiderman.jpg" >spyd</a>
                <a href="anime.png" >Anime</a>
                <a href="boy1.webp" >Boywithuke</a>
                <a href="valorant png.png" style="padding-right: 40px;">Valo</a>
                <input type="text" name="sear" style="border-radius: 20px;border-color: black;width: 200px;height: 40px;background-image: url(see.png);background-size: contain;
                background-repeat: no-repeat;background-position: 2%;text-align: center;font-size: 30px;border: 5px solid black;" placeholder="Search">
                <input type="submit" class="se" name="sub" value="Go">
            </center>
            </div>

            <div>
                <img src="wallspy.jpg" alt="" height="250px" style="padding-left: 200px;">
            </div>
        </div><br>
        <center>
        <h1 style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-style: italic;font-size: 50px;color: black;background-color:cornsilk;">Superior is Deadlier Than His Predecessor
        </h1>
      </center>
        <div id="carouselExampleIndicators" class="carousel slide">
            <div class="carousel-indicators">
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
              <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img src="peakpx.jpg" class="d-block w-100" alt="..." height="800px">
              </div>
              <div class="carousel-item">
                <img src="spypy.jpg" class="d-block w-100" alt="..." height="800px">
              </div>
              <div class="carousel-item">
                <img src="spy4.jpg" class="d-block w-100" alt="..." height="800px">
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
          </div>
          <div style="display: flex;">
            <div class="card" style="width: 18rem;margin: 10px;">
              <img src="spiderman.jpg" class="card-img-top" alt="..." height="300px">
              <div class="card-body">
                <h5 class="card-title">Spider-Man: Across the Spider-Verse</h5>
                <p class="card-text">Spider-Man: Across the Spider-Verse is a 2023 American animated superhero film featuring the Marvel Comics character Miles Morales / Spider-Man, produced by Columbia Pictures and Sony Pictures Animation in association with Marvel Entertainment, and distributed by Sony Pictures</p>
                <a href="https://www.imdb.com/title/tt9362722/" class="btn btn-primary">More</a>
              </div>
            </div>
            <div class="card" style="width: 18rem;margin: 10px;">
              <img src="Nezuko-PNG-Photo.webp" class="card-img-top" alt="..." height="350px">
              <div class="card-body">
                <h5 class="card-title">Nezuko Kamado 竈門 (かまど) 禰 (ね) 豆 (ず) 子 (こ)</h5>
                <p class="card-text">Nezuko isn’t like other demons, which is how she was given the name "The Chosen Demon." The reason behind this is because unlike other demons, she can actually walk in the sunlight without getting burned.</p>
                <a href="https://kimetsu-no-yaiba.fandom.com/wiki/Nezuko_Kamado" class="btn btn-primary">More</a>
              </div>
            </div>
            <div class="card" style="width: 18rem;margin: 10px;">
              <img src="boy2.webp" class="card-img-top" alt="..." height="200px" >
              <div class="card-body">
                <h5 class="card-title">Boywithuke</h5>
                <p class="card-text">Charley Yang, known professionally as BoyWithUke, is a Korean-American singer, musician and internet personality. Yang first gained popularity on the online platform TikTok with his single "Two Moons" and later releases "Toxic" and "Understand". </p>
                <a href="https://www.boywithukemusic.com/#/" class="btn btn-primary">More</a>
              </div>
            </div>
            <div class="card" style="width: 18rem;margin: 10px;">
              <img src="valorant png.png" class="card-img-top" alt="..." height="300px">
              <div class="card-body">
                <h5 class="card-title">Valorant</h5>
                <p class="card-text">Valorant is a tactical shooting game involving two teams with 5 players in each team. ... Wondering why social media and web portals are abuzz with news about a video game called Valorant? It is because the game has come out of closed beta and is now available to gamers across the world including </p>
                <a href="https://playvalorant.com/en-sg/" class="btn btn-primary">More</a>
              </div>
            </div>
            
          
    
</body>
</html>"""
class myhandler(BaseHTTPRequestHandler):
def do_GET(self):
print("request received")
self.send_response(200)
self.send_header('content-type', 'text/html; charset=utf-8')
self.end_headers()
self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()