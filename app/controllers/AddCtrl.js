"use strict";

app.controller('AddCtrl', function($scope,$window,MusicStorage) {
// add model for each form

$scope.artistAdd = {};


	console.log("$scope.artist", $scope.artistAdd);
$scope.addArtist = () => {
		console.log("$scope.artist", $scope.artistAdd);

	MusicStorage.postArtist($scope.artistAdd)
	.then((data) => {
		$scope.$apply();
	});

};


});