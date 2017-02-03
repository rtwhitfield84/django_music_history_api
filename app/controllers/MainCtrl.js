"use strict";

app.controller('MainCtrl', function($scope,$window) {


	$scope.touchMusicArtists =() => {
		console.log("happened ctrl");
		$window.location.href = '#/artist';

	};

		$scope.touchMusicAlbums =() => {
		console.log("happened ctrl");
			$window.location.href = '#/album';

	};

		$scope.touchMusicSongs =() => {
		console.log("happened ctrl");
			$window.location.href = '#/song';

	};

});