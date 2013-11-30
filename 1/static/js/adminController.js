/**
 * Created by tavern on 13-11-30.
 */
var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource'])
    .controller('generalCTRL',['$scope','$location', function($scope, $location){

    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/list', {
                controller: 'blogPostListCTRL',
                templateUrl: '/static/templates/post/list.html'
            }).when('/post/new', {
                controller: 'blogFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            }).when('/post/edit/:id', {
                controller: 'deviceListCTRL',
                templateUrl: '/Device/GridView'
            });
    }]);

var blog = angular.module('blog.post', [])
    .factory('blogService', function ($resource) {
        return $resource('/post/:id', {'id':'@id'});
    })
    .controller('blogPostListCTRL', ['$scope','blogService', function($scope, blogService){
//        $scope.posts = blogService.query();
    }])
    .controller('blogFormCTRL',['$scope', 'blogService', function($scope, blogService){
        var editor = new UE.ui.Editor();
        editor.render("postNew");

        $scope.post = new blogService();

        $scope.submit =  function(){
            $scope.post.content = editor.getContent();
            $scope.post.$save(function(content){
                alert(content)
            });
        };
    }]);