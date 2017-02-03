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

	return {getArtist, getAlbum, getSong};
});