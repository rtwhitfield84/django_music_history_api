"use strict";

var app = angular.module('MusicHistoryApp', ['ngRoute']); 

app.config(function($routeProvider) {
	$routeProvider
	.when('/artists', {
		templateUrl: 'partials/artist.html',
		controller: 'DjangularCtrl'
	})
	.when('/albums', {
		templateUrl: 'partials/album.html',
		controller: 'DjangularCtrl'
	})
	.when('/songs', {
		templateUrl: 'partials/song.html',
		controller: 'DjangularCtrl'
	});
});