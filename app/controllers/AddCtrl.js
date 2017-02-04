"use strict";

app.controller('AddCtrl', function($scope,$window) {
// add model for each form



$scope.addArtist = () => {
	$scope.value = 'add';
	console.log("$scope.value", $scope.value);
};

});