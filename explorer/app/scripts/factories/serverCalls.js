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
			var url = 'http://fantasy.eune.lolesports.com/en-US/api/season/4';

			return baseCalls.getCall(url);
		}
		/*,
		getNALoLEsportsData: function () {
			var url = 'http://na.lolesports.com/api/gameStatsFantasy.json?tournamentId=104';

			return baseCalls.getCall(url);
		},
		getEULoLEsportsData: function () {
			var url = 'http://na.lolesports.com/api/gameStatsFantasy.json?tournamentId=102';

			return baseCalls.getCall(url);
		},
		getLeagueData: function () {
			var url = 'http://fantasy.eune.lolesports.com/en-US/api/league/190024';

			return baseCalls.getCall(url);
		}*/
	};
}]);