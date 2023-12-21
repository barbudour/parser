# ExchangeServiceBase - класс
Represents an abstract binding to an Exchange Service.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ExchangeServiceBase
VB __Копировать
     Public MustInherit Class ExchangeServiceBase
C++ __Копировать
     public ref class ExchangeServiceBase abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type ExchangeServiceBase = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExchangeServiceBase
Derived
[Tessa.Exchange.WebServices.Autodiscover.AutodiscoverService](T_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService.htm)
[Tessa.Exchange.WebServices.Data.ExchangeService](T_Tessa_Exchange_WebServices_Data_ExchangeService.htm)
##  __Свойства
[AcceptGzipEncoding](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_AcceptGzipEncoding.htm)|
Gets or sets a value indicating whether GZip compression encoding should be
accepted.  
---|---  
[ClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ClientRequestId.htm)|
Gets or sets the request id for the request.  
[ConnectionGroupName](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ConnectionGroupName.htm)|
Gets or sets the name of the connection group for the request.  
[CookieContainer](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_CookieContainer.htm)|
Gets or sets the cookie container.  
[Credentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Credentials.htm)|
Gets or sets the credentials used to authenticate with the Exchange Web
Services. Setting the Credentials property automatically sets the
UseDefaultCredentials to false.  
[HttpHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpHeaders.htm)|
Gets a collection of HTTP headers that will be sent with each request to EWS.  
[HttpResponseHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpResponseHeaders.htm)|
Gets a collection of HTTP headers from the last response.  
[KeepAlive](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_KeepAlive.htm)|
Gets or sets if the request to the internet resource should contain a
Connection HTTP header with the value Keep-alive  
[PreAuthenticate](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_PreAuthenticate.htm)|
Gets or sets a value that indicates whether HTTP pre-authentication should be
performed.  
[RequestedServerVersion](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_RequestedServerVersion.htm)|
Gets the requested server version.  
[ReturnClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ReturnClientRequestId.htm)|
Gets or sets a flag to indicate whether the client requires the server side to
return the request id.  
[SendClientLatencies](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_SendClientLatencies.htm)|
Gets or sets a value indicating whether client latency info is push to server.  
[ServerInfo](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ServerInfo.htm)|
Gets information associated with the server that processed the last request.
Will be null if no requests have been processed.  
[Timeout](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Timeout.htm)|
Gets or sets the timeout used when sending HTTP requests and when receiving
HTTP responses, in milliseconds. Defaults to 100000.  
[TimeZoneDefinition](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TimeZoneDefinition.htm)|
Gets a time zone definition generated from the time zone info to which this
service is scoped.  
[TraceEnabled](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceEnabled.htm)|
Gets or sets a value indicating whether tracing is enabled.  
[TraceFlags](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceFlags.htm)|
Gets or sets the trace flags.  
[TraceListener](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceListener.htm)|
Gets or sets the trace listener.  
[UseDefaultCredentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UseDefaultCredentials.htm)|
Gets or sets a value indicating whether the credentials of the user currently
logged into Windows should be used to authenticate with the Exchange Web
Services. Setting UseDefaultCredentials to true automatically sets the
Credentials property to null.  
[UserAgent](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UserAgent.htm)|
Gets or sets the user agent.  
[WebProxy](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_WebProxy.htm)|
Gets or sets the web proxy that should be used when sending requests to EWS.
Set this property to null to use the default web proxy.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[OnResponseHeadersCaptured](E_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_OnResponseHeadersCaptured.htm)|
Occurs when the http response headers of a server call is captured.  
---|---  
[OnSerializeCustomSoapHeaders](E_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_OnSerializeCustomSoapHeaders.htm)|
Provides an event that applications can implement to emit custom SOAP headers
in requests that are sent to Exchange.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
