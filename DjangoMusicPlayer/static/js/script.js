// Initialize the Variables
let songIndex = 0;
let audioElement = new Audio();
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar');
let gif = document.getElementById('gif');
let masterSongName = document.getElementById('masterSongName');
let songItems = Array.from(document.getElementsByClassName('songItem'));

let songs = []

function loadSongs(endpoint) {
    $.ajax({
        url: endpoint,
        type: "GET",
        data: {},
        dataType: "json",
        success: (jsonResponse) => {
            audioElement.src = jsonResponse[0].song

            let i = 0

            jsonResponse.forEach(song => {
                let name = song.title
                song.artists.forEach(artist => {
                    name += ", "
                    name += artist.name
                })
                const kv = {id: song.id, songName: name, filePath: song.song, coverPath: song.thumbnail}

                if (song.is_liked == 'true') {
                    console.log("ahahahahahahaha")
                    $('.songItemContainer').append(
                        `<div class="songItem">
                        <img src="${song.thumbnail}" alt="cover"/>
                        <span class="songName">${name}</span>
                        <span class="songlistplay"
                          ><span class="timestamp"
                            ><span id="like-${song.id}" class="bi bi-heart-fill" style="color: red; cursor: pointer;"></span>
                            <i id="${i}" data-song-src="${song.song}" class="far songItemPlay fa-play-circle"></i> </span
                        ></span>
                      </div>`
                    )
                } else {
                    console.log("hahahahahahahah")
                    $('.songItemContainer').append(
                        `<div class="songItem">
                        <img src="${song.thumbnail}" alt="cover"/>
                        <span class="songName">${name}</span>
                        <span class="songlistplay"
                          ><span class="timestamp"
                            ><span id="like-${song.id}" class="bi bi-heart" style="color: black; cursor: pointer;"></span>
                            <i id="${i}" data-song-src="${song.song}" class="far songItemPlay fa-play-circle"></i> </span
                        ></span>
                      </div>`
                    )
                }

                $(`#like-${song.id}`).on('click', (e) => {
                    let d = false
                    if (e.target.classList.contains('bi-heart-fill')) {
                        d = true
                    }
                    const csrftoken = getCookie('csrftoken')

                    $.ajaxSetup({
                        headers: {
                            'X-CSRFToken': csrftoken
                        }
                    });

                    $.ajax({
                        url: `/song/like/${song.id}/`, // Add the correct song ID in the URL
                        type: "POST",
                        data: {del: d},
                        dataType: "json",
                        success: (jsonResponse) => {
                            if (d) {
                                e.target.classList.remove('bi-heart-fill');
                                e.target.classList.add('bi-heart');
                                e.target.style.color = "black";
                            } else {
                                e.target.classList.remove('bi-heart');
                                e.target.classList.add('bi-heart-fill');
                                e.target.style.color = "red";
                            }
                        },
                        error: () => console.log("error occurred while liking song"),
                    });
                });
                i += 1
                songs.push(kv)
            });

            Array.from(document.getElementsByClassName('songItemPlay')).forEach((element) => {
                element.addEventListener('click', (e) => {
                    makeAllPlays();
                    songIndex = parseInt(e.target.id);
                    e.target.classList.remove('fa-play-circle');
                    e.target.classList.add('fa-pause-circle');
                    audioElement.src = `${e.target.getAttribute('data-song-src')}`;
                    masterSongName.innerText = songs[songIndex].songName;
                    audioElement.currentTime = 0;
                    audioElement.play();
                    gif.style.opacity = 1;
                    masterPlay.classList.remove('fa-play-circle');
                    masterPlay.classList.add('fa-pause-circle');
                })
            })

        },
        error: () => console.log("Failed to fetch data")
    });
}

loadSongs('/songs/')

songItems.forEach((element, i) => {
    element.getElementsByTagName("img")[0].src = songs[i].coverPath;
    element.getElementsByClassName("songName")[0].innerText = songs[i].songName;
})


// Handle play/pause click
masterPlay.addEventListener('click', () => {
    if (audioElement.paused || audioElement.currentTime <= 0) {
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        gif.style.opacity = 1;
    } else {
        audioElement.pause();
        masterPlay.classList.remove('fa-pause-circle');
        masterPlay.classList.add('fa-play-circle');
        gif.style.opacity = 0;
    }
})
// Listen to Events
audioElement.addEventListener('timeupdate', () => {
    // Update Seekbar
    progress = parseInt((audioElement.currentTime / audioElement.duration) * 100);
    myProgressBar.value = progress;
})

myProgressBar.addEventListener('change', () => {
    audioElement.currentTime = myProgressBar.value * audioElement.duration / 100;
})

const makeAllPlays = () => {
    Array.from(document.getElementsByClassName('songItemPlay')).forEach((element) => {
        element.classList.remove('fa-pause-circle');
        element.classList.add('fa-play-circle');
    })
}

Array.from(document.getElementsByClassName('songItemPlay')).forEach((element) => {
    element.addEventListener('click', (e) => {
        makeAllPlays();
        songIndex = parseInt(e.target.id);
        console.log(e.target)
        e.target.classList.remove('fa-play-circle');
        e.target.classList.add('fa-pause-circle');
        audioElement.src = `songs/${songIndex + 1}.mp3`;
        masterSongName.innerText = songs[songIndex].songName;
        audioElement.currentTime = 0;
        audioElement.play();
        gif.style.opacity = 1;
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
    })
})

document.getElementById('next').addEventListener('click', () => {
    if (songIndex >= 9) {
        songIndex = 0
    } else {
        songIndex += 1;
    }
    audioElement.src = `${songs[songIndex].filePath}`;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');

})

document.getElementById('previous').addEventListener('click', () => {
    if (songIndex <= 0) {
        songIndex = 0
    } else {
        songIndex -= 1;
    }
    audioElement.src = `${songs[songIndex].filePath}`;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
})