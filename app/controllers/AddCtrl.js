"use strict";

app.controller('AddCtrl', function($scope,$window,MusicStorage) {
// add model for each form

$scope.artistAdd = {};
$scope.albumAdd = {};
$scope.songAdd = {};
$scope.genreAdd = {};

$scope.addArtist = () => {

	MusicStorage.postArtist($scope.artistAdd)
	.then((data) => {
	$scope.artistAdd = {};
		$scope.$apply();
	});

};

$scope.addAlbum = () => {

	MusicStorage.postAlbum($scope.albumAdd)
	.then((data) => {
	$scope.albumAdd = {};
		$scope.$apply();
	});

};

$scope.addSong = () => {

	MusicStorage.postSong($scope.songAdd)
	.then((data) => {
	$scope.songAdd = {};
		$scope.$apply();
	});

};

$scope.addGenre = () => {

	MusicStorage.postSong($scope.genreAdd)
	.then((data) => {
	$scope.genreAdd = {};
		$scope.$apply();
	});

};


});