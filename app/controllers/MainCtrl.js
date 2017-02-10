"use strict";

app.controller('MainCtrl', function($scope,$window) {

	$scope.home =() => {
		$window.location.href = '#/';

	};


	$scope.touchMusicArtists =() => {
		$window.location.href = '#/artists';

	};

		$scope.touchMusicAlbums =() => {
			$window.location.href = '#/albums';

	};

		$scope.touchMusicSongs =() => {
			$window.location.href = '#/songs';

	};

	$scope.search =() => {
		$window.location.href = '#/search';

	};

	$scope.add =() => {
		$window.location.href = '#/add';

	};

});