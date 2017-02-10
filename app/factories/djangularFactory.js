	"use strict";

app.factory('MusicStorage',($http) =>{

//get artist
	function getArtist() {
		return new Promise((resolve,reject) => {
			$http.get(`http://localhost:8000/artists/`)
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}

//post artist
	function postArtist(artist) {
		return new Promise((resolve,reject) => {
			$http.post(`http://localhost:8000/artists.json`,
				angular.toJson(artist))
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}

//get album
	function getAlbum() {
		return new Promise((resolve,reject) => {
			$http.get(`http://localhost:8000/albums/`)
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}

//post album
	function postAlbum(album) {
		return new Promise((resolve,reject) => {
			$http.post(`http://localhost:8000/albums.json`,
				angular.toJson(album))
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}


//get song
	function getSong() {
		return new Promise((resolve,reject) => {
			$http.get(`http://localhost:8000/songs/`)
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}

//post song
	function postSong(song) {
		return new Promise((resolve,reject) => {
			$http.post(`http://localhost:8000/songs.json`,
				angular.toJson(song))
			.success((data) => {
				resolve(data);
			})
			.error((error) => {
				reject(error);
			});
		});
	}

//post song
function postGenre(genre) {
	return new Promise((resolve,reject) => {
		$http.post(`http://localhost:8000/genres.json`,
			angular.toJson(genre))
		.success((data) => {
			resolve(data);
		})
		.error((error) => {
			reject(error);
		});
	});
}


	return {getArtist, getAlbum, getSong, postArtist, postAlbum, postSong,postGenre};
});