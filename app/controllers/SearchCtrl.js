"use strict";

app.controller('SearchCtrl', function($scope){

	// $scope.radioVal = '';

	$scope.getVal = (x) => {
		console.log("x", x);

	// console.log("$scope.radioVal",$scope.radioVal );
	};

	
	// $scope.search =() => {
	// 	console.log("happened search ctrl");
	// 	MusicStorage.getAlbum()
	// 	.then((data) => {
	// 		console.log("data", data);
	// 		$scope.albums = data;
	// 		$scope.$apply();

	// 	});

	// };

});