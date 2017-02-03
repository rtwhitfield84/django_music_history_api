"use strict";

var app = angular.module('MusicHistoryApp', ['ngRoute']); 

app.config(function($routeProvider) {
	$routeProvider
		.when('/', {
		templateUrl: 'partials/home.html',
	})
	.when('/artists', {
		templateUrl: 'partials/artist.html',
		controller: 'ArtistCtrl'
	})
	.when('/albums', {
		templateUrl: 'partials/album.html',
		controller: 'AlbumCtrl'
	})
	.when('/songs', {
		templateUrl: 'partials/song.html',
		controller: 'SongCtrl'
	})
	.when('/search', {
		templateUrl: 'partials/search.html'
		// controller: 'SearchCtrl'
	})
	.otherwise('/');
});