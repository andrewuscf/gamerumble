'use strict';

angular.module('fantasyLcs').factory('serverCalls', ['$http', function ($http) {
	var baseCalls = {
			getCall: function (url, headers) {
				var callObj = {
						method: 'GET',
						url: url
					};

				if (typeof headers !== 'undefined') {
					callObj.headers = headers;
				}

				return $http(callObj);
			}
		};
	return {
		getFantasyLcsData: function () {
			var url = 'http://na.lolesports.com:80/api/gameStatsFantasy.json?tournamentId=197';

			return baseCalls.getCall(url);
		}
		,
		getNALoLEsportsData: function () {
			var url = 'http://na.lolesports.com:80/api/tournament/197.json';

			return baseCalls.getCall(url);
		},
		getLeagueData: function () {
			var url = 'http://na.lolesports.com:80/api/league/1.json';

			return baseCalls.getCall(url);
		}
	};
}]);