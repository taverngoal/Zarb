/**
 * Created by tavern on 13-11-30.
 */
var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource', 'blog.setting'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {
        var path = $location.path();
        $scope.module = path.substr(1, path.substr(1).indexOf('/'));
    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/list', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/list.html'
            })
            .when('/post/new', {
                controller: 'postFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            })
            .when('/post/edit/:id', {
                controller: 'postFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            })
            .when('/post/edit/:id', {
                controller: 'postFormCTRL',
                templateUrl: '/static/templates/post/form.html'
            })
            .when('/setting/account', {
                controller: 'accountCTRL',
                templateUrl: '/static/templates/setting/account.html'
            })
            .otherwise({ redirectTo: '/home/' });
    }]);

var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post'}
        });
    })
    .controller('postListCTRL', ['$scope', 'postService', function ($scope, postService) {
        postService.getlist(function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postFormCTRL', ['$scope', 'postService', '$location', '$route', function ($scope, postService, $location, $route) {
        var id = $route.current.params.id;
        $scope.isEdit = id != undefined;
        var editor = new UE.ui.Editor();
        editor.render("postNew");
        if (id == undefined)
            $scope.post = new postService();
        else
            $scope.post = postService.get({ id: id }, function (content) {
                editor.setContent(content.content);
            });
        $scope.submit = function () {
            $scope.post.content = editor.getContent();
            $scope.post.$save(function (content) {
                if (content.success) {
                    $location.path("/post/list");
                    $(".alert-success").alert();
                } else {

                }
            });
        };

        $scope.delete = function () {
            postService.delete({id: Number(id)}, function (content) {
                if (content.success) {
                    $location.path("/post/list");
                } else {

                }
            });
        }
    }]);

var setting = angular.module('blog.setting', [])
    .directive('rPassword', [function () {              //验证密码重复和最少位数指令
        return {
            require: 'ngModel',
            priority: -1,
            link: function (scope, ele, attrs, c) {
                scope.$watch('account.psd+account.rpsd', function () {
                    if (scope.account.psd == '') {
                        c.$setValidity('same', true);
                        c.$setValidity('min6', true);
                    } else {
                        if (scope.account.psd == undefined) return;
                        scope.account.psd.length < 6 ? c.$setValidity('min6', false) : c.$setValidity('min6', true);
                        scope.account.psd != scope.account.rpsd ? c.$setValidity('same', false) : c.$setValidity('same', true)
                    }
                })
            }
        }
    }])
    .directive('accountUpdate', ['settingService', function (settingService) {
        return {
            link: function (scope, ele, attrs) {
                ele.bind("click", function () {
                    settingService.update(scope.account, function (content) {
                        if (content.success) {
                            alert('修改成功');
                            scope.account.psd = scope.account.rpsd = ''
                        }
                    });
                })
            }
        }
    }])
    .service('settingService', function ($resource) {
        var service = {
            account: $resource('/setting/account', {}).get(),
            update: function (account, callback) {
                $resource('/setting/account', {}).save(account, callback)
            }
        };
        return service;
    })
//    .factory('settingService', function ($resource) {
//        return $resource('/setting/account', {});
//    })
    .controller('accountCTRL', ["$scope", 'settingService', function ($scope, settingService) {
        $scope.account = {};
        $scope.account = settingService.account
    }]);
