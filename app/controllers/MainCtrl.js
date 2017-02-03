"use strict";

app.controller('MainCtrl', function($scope,MusicStorage,$window) {
	$scope.artists = [];
	$scope.albums = [];
	$scope.songs = [];

	$scope.touchMusicArtists =() => {
		console.log("happened ctrl");
		MusicStorage.getArtist()
		.then((data) => {
			console.log("data", data);
			$scope.artists = data;
			$window.location.href = '#/artist';
			$scope.$apply();
		});

	};

		$scope.touchMusicAlbums =() => {
		console.log("happened ctrl");
		MusicStorage.getAlbum()
		.then((data) => {
			console.log("data", data);
			$scope.albums = data;
			$window.location.href = '#/album';
			$scope.$apply();

		});

	};

		$scope.touchMusicSongs =() => {
		console.log("happened ctrl");
		MusicStorage.getSong()
		.then((data) => {
			console.log("data", data);
			$scope.songs = data;
			$window.location.href = '#/song';
			$scope.$apply();

		});

	};

});