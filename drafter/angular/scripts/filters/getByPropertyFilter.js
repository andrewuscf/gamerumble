'use strict';

angular.module('fantasyLcs').filter('getByProperty', function () {
	return function (collection, propertyName, propertyValue) {
        var result = [];

        angular.forEach(collection, function(value) {
            if (value[propertyName] == propertyValue) {
                result.push(value);
            }
        });
        return result;
	};
});

angular.module('fantasyLcs').filter('getByPosition', ['$filter', function ($filter) {
    return function (collection, position) {
		if(position === '') {
			return collection;
		}
        return $filter('getByProperty')(collection, 'positions', position);
    };
}]);