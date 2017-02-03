"use strict";

app.controller('AlbumCtrl', function($scope,MusicStorage,$window) {
	$scope.albums = [];

		$scope.touchApiAlbums =() => {
		console.log("happened album ctrl");
		MusicStorage.getAlbum()
		.then((data) => {
			console.log("data", data);
			$scope.albums = data;
			$scope.$apply();

		});

	};

	$scope.touchApiAlbums();
});