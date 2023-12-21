# ApplicationsController - класс
Предоставляет доступ для скачивания приложений в Tessa Applications (desktop-
клиент).
## __Definition
 **Пространство имён:** [Tessa.Web.Controllers](N_Tessa_Web_Controllers.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
    [RouteAttribute("api/v1/applications")]
    [AllowAnonymousAttribute]
    [ApiControllerAttribute]
    [ProducesErrorResponseTypeAttribute(typeof(PlainValidationResult))]
    [ProducesResponseTypeAttribute(400)]
    [ProducesResponseTypeAttribute(401)]
    [ProducesResponseTypeAttribute(403)]
    public sealed class ApplicationsController : Controller
VB __Копировать
    <RouteAttribute("api/v1/applications")>
    <AllowAnonymousAttribute>
    <ApiControllerAttribute>
    <ProducesErrorResponseTypeAttribute(GetType(PlainValidationResult))>
    <ProducesResponseTypeAttribute(400)>
    <ProducesResponseTypeAttribute(401)>
    <ProducesResponseTypeAttribute(403)>
    Public NotInheritable Class ApplicationsController
    	Inherits Controller
C++ __Копировать
    [RouteAttribute(L"api/v1/applications")]
    [AllowAnonymousAttribute]
    [ApiControllerAttribute]
    [ProducesErrorResponseTypeAttribute(typeof(PlainValidationResult))]
    [ProducesResponseTypeAttribute(400)]
    [ProducesResponseTypeAttribute(401)]
    [ProducesResponseTypeAttribute(403)]
    public ref class ApplicationsController sealed : public Controller
F# __Копировать
     [<SealedAttribute>]
    [<RouteAttribute("api/v1/applications")>]
    [<AllowAnonymousAttribute>]
    [<ApiControllerAttribute>]
    [<ProducesErrorResponseTypeAttribute(typeof(PlainValidationResult))>]
    [<ProducesResponseTypeAttribute(400)>]
    [<ProducesResponseTypeAttribute(401)>]
    [<ProducesResponseTypeAttribute(403)>]
    type ApplicationsController = 
        class
            inherit Controller
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase) __[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller) __ ApplicationsController
##  __Конструкторы
[ApplicationsController](M_Tessa_Web_Controllers_ApplicationsController__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationsController  
---|---  
##  __Свойства
[ControllerContext](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.controllercontext#microsoft-
aspnetcore-mvc-controllerbase-controllercontext)|  Gets or sets the
[ControllerContext](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllercontext).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
---|---  
[HttpContext](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.httpcontext#microsoft-
aspnetcore-mvc-controllerbase-httpcontext)|  Gets the
[HttpContext](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpcontext)
for the executing action.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[MetadataProvider](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.metadataprovider#microsoft-
aspnetcore-mvc-controllerbase-metadataprovider)|  Gets or sets the
[IModelMetadataProvider](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.imodelmetadataprovider).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ModelBinderFactory](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.modelbinderfactory#microsoft-
aspnetcore-mvc-controllerbase-modelbinderfactory)|  Gets or sets the
[IModelBinderFactory](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.imodelbinderfactory).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ModelState](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.modelstate#microsoft-
aspnetcore-mvc-controllerbase-modelstate)|  Gets the
[ModelStateDictionary](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.modelstatedictionary)
that contains the state of the model and of model-binding validation.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ObjectValidator](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.objectvalidator#microsoft-
aspnetcore-mvc-controllerbase-objectvalidator)|  Gets or sets the
[IObjectModelValidator](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.modelbinding.validation.iobjectmodelvalidator).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ProblemDetailsFactory](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.problemdetailsfactory#microsoft-
aspnetcore-mvc-controllerbase-problemdetailsfactory)|  Gets or sets the
[ProblemDetailsFactory](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.problemdetailsfactory#microsoft-
aspnetcore-mvc-controllerbase-problemdetailsfactory).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Request](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.request#microsoft-
aspnetcore-mvc-controllerbase-request)|  Gets the
[HttpRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httprequest)
for the executing action.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Response](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.response#microsoft-
aspnetcore-mvc-controllerbase-response)|  Gets the
[HttpResponse](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpresponse)
for the executing action.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RouteData](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.routedata#microsoft-
aspnetcore-mvc-controllerbase-routedata)|  Gets the
[RouteData](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.routing.routedata)
for the executing action.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[TempData](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.tempdata#microsoft-
aspnetcore-mvc-controller-tempdata)|  Gets or sets
[ITempDataDictionary](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewfeatures.itempdatadictionary)
used by
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult).  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[Url](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.url#microsoft-
aspnetcore-mvc-controllerbase-url)|  Gets or sets the
[IUrlHelper](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.iurlhelper).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[User](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.user#microsoft-
aspnetcore-mvc-controllerbase-user)|  Gets the
[ClaimsPrincipal](https://learn.microsoft.com/dotnet/api/system.security.claims.claimsprincipal)
for user associated with the executing action.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ViewBag](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewbag#microsoft-
aspnetcore-mvc-controller-viewbag)|  Gets the dynamic view bag.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[ViewData](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewdata#microsoft-
aspnetcore-mvc-controller-viewdata)|  Gets or sets
[ViewDataDictionary](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewfeatures.viewdatadictionary)
used by
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult)
and
[ViewBag](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewbag#microsoft-
aspnetcore-mvc-controller-viewbag).  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
##  __Методы
[Accepted()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted)|  Creates a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
---|---  
[Accepted(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted\(system-object\))|  Creates a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Accepted(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted\(system-string\))|  Creates a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Accepted(Uri)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted\(system-uri\))|  Creates a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Accepted(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted\(system-string-system-object\))|
Creates a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Accepted(Uri,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.accepted#microsoft-
aspnetcore-mvc-controllerbase-accepted\(system-uri-system-object\))|  Creates
a
[AcceptedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string-system-
object\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string-system-
string\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string-system-object-
system-object\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String, String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string-system-string-
system-object\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtAction(String, String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedataction#microsoft-
aspnetcore-mvc-controllerbase-acceptedataction\(system-string-system-string-
system-object-system-object\))|  Creates a
[AcceptedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatactionresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtRoute(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedatroute#microsoft-
aspnetcore-mvc-controllerbase-acceptedatroute\(system-object\))|  Creates a
[AcceptedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatrouteresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtRoute(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedatroute#microsoft-
aspnetcore-mvc-controllerbase-acceptedatroute\(system-string\))|  Creates a
[AcceptedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatrouteresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtRoute(Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedatroute#microsoft-
aspnetcore-mvc-controllerbase-acceptedatroute\(system-object-system-object\))|
Creates a
[AcceptedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatrouteresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtRoute(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedatroute#microsoft-
aspnetcore-mvc-controllerbase-acceptedatroute\(system-string-system-object\))|
Creates a
[AcceptedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatrouteresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[AcceptedAtRoute(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.acceptedatroute#microsoft-
aspnetcore-mvc-controllerbase-acceptedatroute\(system-string-system-object-
system-object\))|  Creates a
[AcceptedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.acceptedatrouteresult)
object that produces an
[Status202Accepted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status202accepted)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[BadRequest()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.badrequest#microsoft-
aspnetcore-mvc-controllerbase-badrequest)|  Creates an
[BadRequestResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.badrequestresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[BadRequest(ModelStateDictionary)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.badrequest#microsoft-
aspnetcore-mvc-controllerbase-badrequest\(microsoft-aspnetcore-mvc-
modelbinding-modelstatedictionary\))|  Creates an
[BadRequestObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.badrequestobjectresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[BadRequest(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.badrequest#microsoft-
aspnetcore-mvc-controllerbase-badrequest\(system-object\))|  Creates an
[BadRequestObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.badrequestobjectresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Challenge()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.challenge#microsoft-
aspnetcore-mvc-controllerbase-challenge)|  Creates a
[ChallengeResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.challengeresult).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Challenge(AuthenticationProperties)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.challenge#microsoft-
aspnetcore-mvc-controllerbase-challenge\(microsoft-aspnetcore-authentication-
authenticationproperties\))|  Creates a
[ChallengeResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.challengeresult)
with the specified properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Challenge(String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.challenge#microsoft-
aspnetcore-mvc-controllerbase-challenge\(system-string\(\)\))|  Creates a
[ChallengeResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.challengeresult)
with the specified authentication schemes.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Challenge(AuthenticationProperties,
String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.challenge#microsoft-
aspnetcore-mvc-controllerbase-challenge\(microsoft-aspnetcore-authentication-
authenticationproperties-system-string\(\)\))|  Creates a
[ChallengeResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.challengeresult)
with the specified authentication schemes and properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Conflict()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.conflict#microsoft-
aspnetcore-mvc-controllerbase-conflict)|  Creates an
[ConflictResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.conflictresult)
that produces a
[Status409Conflict](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status409conflict)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Conflict(ModelStateDictionary)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.conflict#microsoft-
aspnetcore-mvc-controllerbase-conflict\(microsoft-aspnetcore-mvc-modelbinding-
modelstatedictionary\))|  Creates an
[ConflictObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.conflictobjectresult)
that produces a
[Status409Conflict](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status409conflict)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Conflict(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.conflict#microsoft-
aspnetcore-mvc-controllerbase-conflict\(system-object\))|  Creates an
[ConflictObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.conflictobjectresult)
that produces a
[Status409Conflict](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status409conflict)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Content(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.content#microsoft-
aspnetcore-mvc-controllerbase-content\(system-string\))|  Creates a
[ContentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.contentresult)
object by specifying a content string.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Content(String,
MediaTypeHeaderValue)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.content#microsoft-
aspnetcore-mvc-controllerbase-content\(system-string-microsoft-net-http-
headers-mediatypeheadervalue\))|  Creates a
[ContentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.contentresult)
object by specifying a content string and a contentType.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Content(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.content#microsoft-
aspnetcore-mvc-controllerbase-content\(system-string-system-string\))|
Creates a
[ContentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.contentresult)
object by specifying a content string and a content type.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Content(String, String,
Encoding)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.content#microsoft-
aspnetcore-mvc-controllerbase-content\(system-string-system-string-system-
text-encoding\))|  Creates a
[ContentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.contentresult)
object by specifying a content string, a contentType, and contentEncoding.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Created(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.created#microsoft-
aspnetcore-mvc-controllerbase-created\(system-string-system-object\))|
Creates a
[CreatedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Created(Uri,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.created#microsoft-
aspnetcore-mvc-controllerbase-created\(system-uri-system-object\))|  Creates a
[CreatedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtAction(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdataction#microsoft-
aspnetcore-mvc-controllerbase-createdataction\(system-string-system-object\))|
Creates a
[CreatedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatactionresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtAction(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdataction#microsoft-
aspnetcore-mvc-controllerbase-createdataction\(system-string-system-object-
system-object\))|  Creates a
[CreatedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatactionresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtAction(String, String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdataction#microsoft-
aspnetcore-mvc-controllerbase-createdataction\(system-string-system-string-
system-object-system-object\))|  Creates a
[CreatedAtActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatactionresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtRoute(Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdatroute#microsoft-
aspnetcore-mvc-controllerbase-createdatroute\(system-object-system-object\))|
Creates a
[CreatedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatrouteresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtRoute(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdatroute#microsoft-
aspnetcore-mvc-controllerbase-createdatroute\(system-string-system-object\))|
Creates a
[CreatedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatrouteresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[CreatedAtRoute(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.createdatroute#microsoft-
aspnetcore-mvc-controllerbase-createdatroute\(system-string-system-object-
system-object\))|  Creates a
[CreatedAtRouteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.createdatrouteresult)
object that produces a
[Status201Created](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status201created)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Dispose()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.dispose#microsoft-
aspnetcore-mvc-controller-dispose)|  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.dispose#microsoft-
aspnetcore-mvc-controller-dispose\(system-boolean\))|  Releases all resources
currently used by this
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller)
instance.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[File(Byte[],
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-byte\(\)-system-string\))|  Returns
a file with the specified fileContents as content
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
and the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Stream,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-io-stream-system-string\))|
Returns a file in the specified fileStream
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-string-system-string\))|  Returns
the file specified by virtualPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Byte[], String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-byte\(\)-system-string-system-
boolean\))|  Returns a file with the specified fileContents as content
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
and the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Byte[], String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-byte\(\)-system-string-system-
string\))|  Returns a file with the specified fileContents as content
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Stream, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-io-stream-system-string-system-
boolean\))|  Returns a file in the specified fileStream
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Stream, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-io-stream-system-string-system-
string\))|  Returns a file in the specified fileStream
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-string-system-string-system-
boolean\))|  Returns the file specified by virtualPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-string-system-string-system-
string\))|  Returns the file specified by virtualPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.Byte[],System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Byte[], String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-byte\(\)-system-string-system-
string-system-boolean\))|  Returns a file with the specified fileContents as
content
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)),
the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.IO.Stream,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(Stream, String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-io-stream-system-string-system-
string-system-boolean\))|  Returns a file in the specified fileStream
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[File(String, String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.file#microsoft-
aspnetcore-mvc-controllerbase-file\(system-string-system-string-system-string-
system-boolean\))|  Returns the file specified by virtualPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.Byte[],System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.Byte[],System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.IO.Stream,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.IO.Stream,System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.String,System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.Byte[],System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.IO.Stream,System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.File(System.String,System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Forbid()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.forbid#microsoft-
aspnetcore-mvc-controllerbase-forbid)|  Creates a
[ForbidResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.forbidresult)
([Status403Forbidden](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status403forbidden)
by default).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Forbid(AuthenticationProperties)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.forbid#microsoft-
aspnetcore-mvc-controllerbase-forbid\(microsoft-aspnetcore-authentication-
authenticationproperties\))|  Creates a
[ForbidResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.forbidresult)
([Status403Forbidden](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status403forbidden)
by default) with the specified properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Forbid(String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.forbid#microsoft-
aspnetcore-mvc-controllerbase-forbid\(system-string\(\)\))|  Creates a
[ForbidResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.forbidresult)
([Status403Forbidden](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status403forbidden)
by default) with the specified authentication schemes.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Forbid(AuthenticationProperties,
String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.forbid#microsoft-
aspnetcore-mvc-controllerbase-forbid\(microsoft-aspnetcore-authentication-
authenticationproperties-system-string\(\)\))|  Creates a
[ForbidResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.forbidresult)
([Status403Forbidden](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status403forbidden)
by default) with the specified authentication schemes and properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[GetApplications](M_Tessa_Web_Controllers_ApplicationsController_GetApplications.htm)|
Возвращает список всех приложений, доступных пользователю, в форме
типизированного JSON.  
[GetAttributesByAlias](M_Tessa_Web_Controllers_ApplicationsController_GetAttributesByAlias.htm)|
Возвращает дату изменения приложения и признак того, что приложение является
64-битным. Возвращает объект, содержащий дату изменения карточки приложения
Modified и признак того, является ли приложение 64-битным Client64Bit, или 204
(No Content), если данные получить не удалось.  
[GetFaultedResult](M_Tessa_Web_Controllers_ApplicationsController_GetFaultedResult.htm)|
Возвращает ошибки при скачивании приложения как объект
[PlainValidationResult](T_Tessa_Platform_Validation_PlainValidationResult.htm)
или 204 (No Content), если информация недоступна: ошибок не было или
пользователь не имеет доступа к этой записи в истории.  
[GetIdByAlias](M_Tessa_Web_Controllers_ApplicationsController_GetIdByAlias.htm)|
Осуществляет попытку получения идентификатора приложения по его алиасу.
Возвращает идентификатор приложения или 204 (No Content), если данные получить
не удалось.  
[Json(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.json#microsoft-
aspnetcore-mvc-controller-json\(system-object\))|  Creates a
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult)
object that serializes the specified data object to JSON.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[Json(Object,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.json#microsoft-
aspnetcore-mvc-controller-json\(system-object-system-object\))|  Creates a
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult)
object that serializes the specified data object to JSON.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[LocalRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.localredirect#microsoft-
aspnetcore-mvc-controllerbase-localredirect\(system-string\))|  Creates a
[LocalRedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult)
object that redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified local localUrl.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[LocalRedirectPermanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.localredirectpermanent#microsoft-
aspnetcore-mvc-controllerbase-localredirectpermanent\(system-string\))|
Creates a
[LocalRedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult.permanent#microsoft-
aspnetcore-mvc-localredirectresult-permanent) set to true
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
using the specified localUrl.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[LocalRedirectPermanentPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.localredirectpermanentpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-localredirectpermanentpreservemethod\(system-
string\))|  Creates a
[LocalRedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult.permanent#microsoft-
aspnetcore-mvc-localredirectresult-permanent) set to true and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult.preservemethod#microsoft-
aspnetcore-mvc-localredirectresult-preservemethod) set to true
([Status308PermanentRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect))
using the specified localUrl.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[LocalRedirectPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.localredirectpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-localredirectpreservemethod\(system-string\))|
Creates a
[LocalRedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult.permanent#microsoft-
aspnetcore-mvc-localredirectresult-permanent) set to false and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.localredirectresult.preservemethod#microsoft-
aspnetcore-mvc-localredirectresult-preservemethod) set to true
([Status307TemporaryRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect))
using the specified localUrl.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[NoContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.nocontent#microsoft-
aspnetcore-mvc-controllerbase-nocontent)|  Creates a
[NoContentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.nocontentresult)
object that produces an empty
[Status204NoContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status204nocontent)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[NotFound()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.notfound#microsoft-
aspnetcore-mvc-controllerbase-notfound)|  Creates an
[NotFoundResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.notfoundresult)
that produces a
[Status404NotFound](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status404notfound)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[NotFound(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.notfound#microsoft-
aspnetcore-mvc-controllerbase-notfound\(system-object\))|  Creates an
[NotFoundObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.notfoundobjectresult)
that produces a
[Status404NotFound](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status404notfound)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Ok()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.ok#microsoft-
aspnetcore-mvc-controllerbase-ok)|  Creates a
[OkResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.okresult)
object that produces an empty
[Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Ok(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.ok#microsoft-
aspnetcore-mvc-controllerbase-ok\(system-object\))|  Creates an
[OkObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.okobjectresult)
object that produces an
[Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[OnActionExecuted](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.onactionexecuted#microsoft-
aspnetcore-mvc-controller-onactionexecuted\(microsoft-aspnetcore-mvc-filters-
actionexecutedcontext\))|  Called after the action method is invoked.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[OnActionExecuting](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.onactionexecuting#microsoft-
aspnetcore-mvc-controller-onactionexecuting\(microsoft-aspnetcore-mvc-filters-
actionexecutingcontext\))|  Called before the action method is invoked.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[OnActionExecutionAsync](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.onactionexecutionasync#microsoft-
aspnetcore-mvc-controller-onactionexecutionasync\(microsoft-aspnetcore-mvc-
filters-actionexecutingcontext-microsoft-aspnetcore-mvc-filters-
actionexecutiondelegate\))|  Called before the action method is invoked.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[PartialView()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.partialview#microsoft-
aspnetcore-mvc-controller-partialview)|  Creates a
[PartialViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.partialviewresult)
object that renders a partial view to the response.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[PartialView(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.partialview#microsoft-
aspnetcore-mvc-controller-partialview\(system-object\))|  Creates a
[PartialViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.partialviewresult)
object by specifying a model to be rendered by the partial view.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[PartialView(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.partialview#microsoft-
aspnetcore-mvc-controller-partialview\(system-string\))|  Creates a
[PartialViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.partialviewresult)
object by specifying a viewName.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[PartialView(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.partialview#microsoft-
aspnetcore-mvc-controller-partialview\(system-string-system-object\))|
Creates a
[PartialViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.partialviewresult)
object by specifying a viewName and the model to be rendered by the partial
view.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[PhysicalFile(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.physicalfile#microsoft-
aspnetcore-mvc-controllerbase-physicalfile\(system-string-system-string\))|
Returns the file specified by physicalPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[PhysicalFile(String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.physicalfile#microsoft-
aspnetcore-mvc-controllerbase-physicalfile\(system-string-system-string-
system-boolean\))|  Returns the file specified by physicalPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type. This supports range
requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[PhysicalFile(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.physicalfile#microsoft-
aspnetcore-mvc-controllerbase-physicalfile\(system-string-system-string-
system-string\))|  Returns the file specified by physicalPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.PhysicalFile(System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[PhysicalFile(String, String, String,
Boolean)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.physicalfile#microsoft-
aspnetcore-mvc-controllerbase-physicalfile\(system-string-system-string-
system-string-system-boolean\))|  Returns the file specified by physicalPath
([Status200OK](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status200ok))
with the specified contentType as the Content-Type and the specified
fileDownloadName as the suggested file name. This supports range requests
([Status206PartialContent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status206partialcontent)
or
[Status416RangeNotSatisfiable](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status416rangenotsatisfiable)
if the range is not satisfiable).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.PhysicalFile(System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.PhysicalFile(System.String,System.String,System.String,System.Nullable`1,System.Void)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.PhysicalFile(System.String,System.String,System.String,System.Nullable`1,System.Void,System.DateTimeOffset)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[PostDownload](M_Tessa_Web_Controllers_ApplicationsController_PostDownload.htm)|
Скачивает поток с бинарными данными приложения.  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.Problem(System.String,System.String,System.Nullable`1,System.Void,System.Int32)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Redirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirect#microsoft-
aspnetcore-mvc-controllerbase-redirect\(system-string\))|  Creates a
[RedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult)
object that redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified url.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectPermanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirectpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirectpermanent\(system-string\))|  Creates a
[RedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult.permanent#microsoft-
aspnetcore-mvc-redirectresult-permanent) set to true
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
using the specified url.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectPermanentPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirectpermanentpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirectpermanentpreservemethod\(system-
string\))|  Creates a
[RedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult.permanent#microsoft-
aspnetcore-mvc-redirectresult-permanent) set to true and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult.preservemethod#microsoft-
aspnetcore-mvc-redirectresult-preservemethod) set to true
([Status308PermanentRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect))
using the specified url.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirectpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirectpreservemethod\(system-string\))|
Creates a
[RedirectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult)
object with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult.permanent#microsoft-
aspnetcore-mvc-redirectresult-permanent) set to false and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirectresult.preservemethod#microsoft-
aspnetcore-mvc-redirectresult-preservemethod) set to true
([Status307TemporaryRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect))
using the specified url.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction)|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to an action with the same name as current one. The 'controller' and 'action'
names are retrieved from the ambient values of the current request.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the actionName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string-system-
object\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the actionName and routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string-system-
string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the actionName and the controllerName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String, String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string-system-string-
system-object\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the specified actionName, controllerName, and
routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string-system-string-
system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the specified actionName, controllerName, and
fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToAction(String, String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoaction#microsoft-
aspnetcore-mvc-controllerbase-redirecttoaction\(system-string-system-string-
system-object-system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified action using the specified actionName, controllerName,
routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string\))|
Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string-system-
object\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName and routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string-system-
string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName and controllerName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String, String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string-system-
string-system-object\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName, controllerName, and routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string-system-
string-system-string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName, controllerName, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanent(String, String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanent\(system-string-system-
string-system-object-system-string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true using the
specified actionName, controllerName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPermanentPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpermanentpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpermanentpreservemethod\(system-
string-system-string-system-object-system-string\))|  Redirects
([Status308PermanentRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to true and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttoactionresult-preservemethod) set to true, using the
specified actionName, controllerName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToActionPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoactionpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttoactionpreservemethod\(system-string-
system-string-system-object-system-string\))|  Redirects
([Status307TemporaryRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect))
to the specified action with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.permanent#microsoft-
aspnetcore-mvc-redirecttoactionresult-permanent) set to false and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttoactionresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttoactionresult-preservemethod) set to true, using the
specified actionName, controllerName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string-system-object\))|
Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName using the specified routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string-system-string\))|
Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName using the specified pageHandler.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String, String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string-system-string-
system-object\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string-system-string-
system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName using the specified fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPage(String, String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopage#microsoft-
aspnetcore-mvc-controllerbase-redirecttopage\(system-string-system-string-
system-object-system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified pageName using the specified routeValues and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanent(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanent\(system-string\))|
Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified pageName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanent(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanent\(system-string-system-
object\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified pageName using the specified routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanent(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanent\(system-string-system-
string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified pageName using the specified pageHandler.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanent(String, String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanent\(system-string-system-
string-system-string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified pageName using the specified fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanent(String, String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanent\(system-string-system-
string-system-object-system-string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified pageName using the specified routeValues and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePermanentPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepermanentpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepermanentpreservemethod\(system-
string-system-string-system-object-system-string\))|  Redirects
([Status308PermanentRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttorouteresult-preservemethod) set to true, using the
specified pageName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToPagePreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttopagepreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttopagepreservemethod\(system-string-
system-string-system-object-system-string\))|  Redirects
([Status307TemporaryRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect))
to the specified page with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to false and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttorouteresult-preservemethod) set to true, using the
specified pageName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoute(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroute#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroute\(system-object\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified route using the specified routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoute(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroute#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroute\(system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified route using the specified routeName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoute(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroute#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroute\(system-string-system-object\))|
Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified route using the specified routeName and routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoute(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroute#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroute\(system-string-system-string\))|
Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified route using the specified routeName and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoute(String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroute#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroute\(system-string-system-object-
system-string\))|  Redirects
([Status302Found](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status302found))
to the specified route using the specified routeName, routeValues, and
fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanent(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanent\(system-object\))|
Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true using the
specified routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanent(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanent\(system-string\))|
Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true using the
specified routeName.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanent(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanent\(system-string-system-
object\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true using the
specified routeName and routeValues.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanent(String,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanent\(system-string-system-
string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true using the
specified routeName and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanent(String, Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanent#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanent\(system-string-system-
object-system-string\))|  Redirects
([Status301MovedPermanently](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status301movedpermanently))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true using the
specified routeName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePermanentPreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepermanentpreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepermanentpreservemethod\(system-
string-system-object-system-string\))|  Redirects
([Status308PermanentRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to true and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttorouteresult-preservemethod) set to true, using the
specified routeName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[RedirectToRoutePreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.redirecttoroutepreservemethod#microsoft-
aspnetcore-mvc-controllerbase-redirecttoroutepreservemethod\(system-string-
system-object-system-string\))|  Redirects
([Status307TemporaryRedirect](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect))
to the specified route with
[Permanent](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.permanent#microsoft-
aspnetcore-mvc-redirecttorouteresult-permanent) set to false and
[PreserveMethod](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.redirecttorouteresult.preservemethod#microsoft-
aspnetcore-mvc-redirecttorouteresult-preservemethod) set to true, using the
specified routeName, routeValues, and fragment.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignIn(ClaimsPrincipal)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signin#microsoft-
aspnetcore-mvc-controllerbase-signin\(system-security-claims-
claimsprincipal\))|  Creates a
[SignInResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signinresult).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignIn(ClaimsPrincipal,
AuthenticationProperties)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signin#microsoft-
aspnetcore-mvc-controllerbase-signin\(system-security-claims-claimsprincipal-
microsoft-aspnetcore-authentication-authenticationproperties\))|  Creates a
[SignInResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signinresult)
with properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignIn(ClaimsPrincipal,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signin#microsoft-
aspnetcore-mvc-controllerbase-signin\(system-security-claims-claimsprincipal-
system-string\))|  Creates a
[SignInResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signinresult)
with the specified authentication scheme.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignIn(ClaimsPrincipal, AuthenticationProperties,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signin#microsoft-
aspnetcore-mvc-controllerbase-signin\(system-security-claims-claimsprincipal-
microsoft-aspnetcore-authentication-authenticationproperties-system-string\))|
Creates a
[SignInResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signinresult)
with the specified authentication scheme and properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignOut()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signout#microsoft-
aspnetcore-mvc-controllerbase-signout)|  Creates a
[SignOutResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signoutresult).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignOut(AuthenticationProperties)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signout#microsoft-
aspnetcore-mvc-controllerbase-signout\(microsoft-aspnetcore-authentication-
authenticationproperties\))|  Creates a
[SignOutResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signoutresult)
with properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignOut(String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signout#microsoft-
aspnetcore-mvc-controllerbase-signout\(system-string\(\)\))|  Creates a
[SignOutResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signoutresult)
with the specified authentication schemes.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[SignOut(AuthenticationProperties,
String[])](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.signout#microsoft-
aspnetcore-mvc-controllerbase-signout\(microsoft-aspnetcore-authentication-
authenticationproperties-system-string\(\)\))|  Creates a
[SignOutResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.signoutresult)
with the specified authentication schemes and properties.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[StatusCode(Int32)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.statuscode#microsoft-
aspnetcore-mvc-controllerbase-statuscode\(system-int32\))|  Creates a
[StatusCodeResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.statuscoderesult)
object by specifying a statusCode.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[StatusCode(Int32,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.statuscode#microsoft-
aspnetcore-mvc-controllerbase-statuscode\(system-int32-system-object\))|
Creates a
[ObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.objectresult)
object by specifying a statusCode and value  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync(Void, Boolean, Object)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync(Void, Boolean, Object, Type, String)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync``1(Void)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync``1(Void, Boolean)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync``1(Void, Boolean, UMP)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
TryUpdateModelAsync``1(Void, Boolean, UMP, String)|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[TryValidateModel(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.tryvalidatemodel#microsoft-
aspnetcore-mvc-controllerbase-tryvalidatemodel\(system-object\))|  Validates
the specified model instance.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[TryValidateModel(Object,
String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.tryvalidatemodel#microsoft-
aspnetcore-mvc-controllerbase-tryvalidatemodel\(system-object-system-
string\))|  Validates the specified model instance.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Unauthorized()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.unauthorized#microsoft-
aspnetcore-mvc-controllerbase-unauthorized)|  Creates an
[UnauthorizedResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.unauthorizedresult)
that produces an
[Status401Unauthorized](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status401unauthorized)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[Unauthorized(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.unauthorized#microsoft-
aspnetcore-mvc-controllerbase-unauthorized\(system-object\))|  Creates an
[UnauthorizedObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.unauthorizedobjectresult)
that produces a
[Status401Unauthorized](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status401unauthorized)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[UnprocessableEntity()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.unprocessableentity#microsoft-
aspnetcore-mvc-controllerbase-unprocessableentity)|  Creates an
[UnprocessableEntityResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.unprocessableentityresult)
that produces a
[Status422UnprocessableEntity](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status422unprocessableentity)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[UnprocessableEntity(ModelStateDictionary)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.unprocessableentity#microsoft-
aspnetcore-mvc-controllerbase-unprocessableentity\(microsoft-aspnetcore-mvc-
modelbinding-modelstatedictionary\))|  Creates an
[UnprocessableEntityObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.unprocessableentityobjectresult)
that produces a
[Status422UnprocessableEntity](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status422unprocessableentity)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[UnprocessableEntity(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.unprocessableentity#microsoft-
aspnetcore-mvc-controllerbase-unprocessableentity\(system-object\))|  Creates
an
[UnprocessableEntityObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.unprocessableentityobjectresult)
that produces a
[Status422UnprocessableEntity](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status422unprocessableentity)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ValidationProblem()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.validationproblem#microsoft-
aspnetcore-mvc-controllerbase-validationproblem)|  Creates an
[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response with validation errors from
[ModelState](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.modelstate#microsoft-
aspnetcore-mvc-controllerbase-modelstate).  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ValidationProblem(ModelStateDictionary)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.validationproblem#microsoft-
aspnetcore-mvc-controllerbase-validationproblem\(microsoft-aspnetcore-mvc-
modelbinding-modelstatedictionary\))|  Creates an
[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response with validation errors from modelStateDictionary.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[ValidationProblem(ValidationProblemDetails)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase.validationproblem#microsoft-
aspnetcore-mvc-controllerbase-validationproblem\(microsoft-aspnetcore-mvc-
validationproblemdetails\))|  Creates an
[BadRequestObjectResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.badrequestobjectresult)
that produces a
[Status400BadRequest](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.statuscodes.status400badrequest)
response.  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[M:Microsoft.AspNetCore.Mvc.ControllerBase.ValidationProblem(System.String,System.String,System.Nullable`1,System.Void,System.Int32,System.String)]|  
(Унаследован от
[ControllerBase](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controllerbase))  
[View()](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.view#microsoft-
aspnetcore-mvc-controller-view)|  Creates a
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult)
object that renders a view to the response.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[View(Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.view#microsoft-
aspnetcore-mvc-controller-view\(system-object\))|  Creates a
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult)
object by specifying a model to be rendered by the view.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[View(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.view#microsoft-
aspnetcore-mvc-controller-view\(system-string\))|  Creates a
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult)
object by specifying a viewName.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[View(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.view#microsoft-
aspnetcore-mvc-controller-view\(system-string-system-object\))|  Creates a
[ViewResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewresult)
object by specifying a viewName and the model to be rendered by the view.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[ViewComponent(String)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewcomponent#microsoft-
aspnetcore-mvc-controller-viewcomponent\(system-string\))|  Creates a
[ViewComponentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewcomponentresult)
by specifying the name of a view component to render.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[ViewComponent(Type)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewcomponent#microsoft-
aspnetcore-mvc-controller-viewcomponent\(system-type\))|  Creates a
[ViewComponentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewcomponentresult)
by specifying the [Type](https://learn.microsoft.com/dotnet/api/system.type)
of a view component to render.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[ViewComponent(String,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewcomponent#microsoft-
aspnetcore-mvc-controller-viewcomponent\(system-string-system-object\))|
Creates a
[ViewComponentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewcomponentresult)
by specifying the name of a view component to render.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
[ViewComponent(Type,
Object)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller.viewcomponent#microsoft-
aspnetcore-mvc-controller-viewcomponent\(system-type-system-object\))|
Creates a
[ViewComponentResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.viewcomponentresult)
by specifying the [Type](https://learn.microsoft.com/dotnet/api/system.type)
of a view component to render.  
(Унаследован от
[Controller](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.controller))  
##  __Методы расширения
[BinaryStream](M_Tessa_Web_WebExtensions_BinaryStream.htm)|  
(Определяется [WebExtensions](T_Tessa_Web_WebExtensions.htm))  
---|---  
[Bson](M_Tessa_Web_WebExtensions_Bson.htm)|  
(Определяется [WebExtensions](T_Tessa_Web_WebExtensions.htm))  
[Multipart](M_Tessa_Web_WebExtensions_Multipart.htm)|  
(Определяется [WebExtensions](T_Tessa_Web_WebExtensions.htm))  
[TypedJson](M_Tessa_Web_WebExtensions_TypedJson.htm)|  
(Определяется [WebExtensions](T_Tessa_Web_WebExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Web.Controllers - пространство имён](N_Tessa_Web_Controllers.htm)
