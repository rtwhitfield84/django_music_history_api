"use strict";

app.controller('MainCtrl', function($scope,$window) {

	$scope.home =() => {
		console.log("happened art ctrl");
		$window.location.href = '#/';

	};


	$scope.touchMusicArtists =() => {
		console.log("happened art ctrl");
		$window.location.href = '#/artists';

	};

		$scope.touchMusicAlbums =() => {
		console.log("happened ctrl");
			$window.location.href = '#/albums';

	};

		$scope.touchMusicSongs =() => {
		console.log("happened ctrl");
			$window.location.href = '#/songs';

	};

	$scope.search =() => {
		console.log("happened art ctrl");
		$window.location.href = '#/search';

	};

});