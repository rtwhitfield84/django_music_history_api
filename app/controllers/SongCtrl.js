"use strict";

app.controller('SongCtrl', function($scope,MusicStorage,$window) {
	$scope.songs = [];

		$scope.touchApiSongs =() => {
		console.log("happened ctrl");
		MusicStorage.getSong()
		.then((data) => {
			console.log("data", data);
			$scope.songs = data;
			$scope.$apply();

		});

	};

	$scope.touchApiSongs();

});