"use strict";

var app = angular.module('MusicHistoryApp', ['ngRoute']); 

app.config(function($routeProvider) {
	$routeProvider
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
	.otherwise('/');
});