"use strict";

app.controller('ArtistCtrl', function($scope,MusicStorage,$window) {
	$scope.artists = [];

	$scope.touchApiArtists =() => {
		console.log("happened artcsadsd ctrl");
		MusicStorage.getArtist()
		.then((data) => {
			console.log("data", data);
			$scope.artists = data;
			$scope.$apply();
		});

	};

	$scope.touchApiArtists();
});