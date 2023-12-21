# AutodiscoverService - свойства
##  __Свойства
[AcceptGzipEncoding](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_AcceptGzipEncoding.htm)|
Gets or sets a value indicating whether GZip compression encoding should be
accepted.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
---|---  
[ClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ClientRequestId.htm)|
Gets or sets the request id for the request.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ConnectionGroupName](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ConnectionGroupName.htm)|
Gets or sets the name of the connection group for the request.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[CookieContainer](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_CookieContainer.htm)|
Gets or sets the cookie container.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Credentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Credentials.htm)|
Gets or sets the credentials used to authenticate with the Exchange Web
Services. Setting the Credentials property automatically sets the
UseDefaultCredentials to false.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Domain](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_Domain.htm)|
Gets or sets the domain this service is bound to. When this property is set,
the domain name is used to automatically determine the Autodiscover service
URL.  
[EnableScpLookup](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_EnableScpLookup.htm)|
Gets or sets a value indicating whether the AutodiscoverService should perform
SCP (ServiceConnectionPoint) record lookup when determining the Autodiscover
service URL.  
[GetScpUrlsForDomainCallback](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_GetScpUrlsForDomainCallback.htm)|
Gets or sets the delegate used to resolve Autodiscover SCP urls for a
specified domain.  
[HttpHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpHeaders.htm)|
Gets a collection of HTTP headers that will be sent with each request to EWS.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[HttpResponseHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpResponseHeaders.htm)|
Gets a collection of HTTP headers from the last response.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[IsExternal](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_IsExternal.htm)|
Gets a value indicating whether the Autodiscover service that URL points to is
internal (inside the corporate network) or external (outside the corporate
network).  
[KeepAlive](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_KeepAlive.htm)|
Gets or sets if the request to the internet resource should contain a
Connection HTTP header with the value Keep-alive  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[PreAuthenticate](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_PreAuthenticate.htm)|
Gets or sets a value that indicates whether HTTP pre-authentication should be
performed.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[RedirectionUrlValidationCallback](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_RedirectionUrlValidationCallback.htm)|
Gets or sets the redirection URL validation callback.  
[RequestedServerVersion](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_RequestedServerVersion.htm)|
Gets the requested server version.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ReturnClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ReturnClientRequestId.htm)|
Gets or sets a flag to indicate whether the client requires the server side to
return the request id.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[SendClientLatencies](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_SendClientLatencies.htm)|
Gets or sets a value indicating whether client latency info is push to server.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ServerInfo](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ServerInfo.htm)|
Gets information associated with the server that processed the last request.
Will be null if no requests have been processed.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Timeout](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Timeout.htm)|
Gets or sets the timeout used when sending HTTP requests and when receiving
HTTP responses, in milliseconds. Defaults to 100000.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TimeZoneDefinition](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TimeZoneDefinition.htm)|
Gets a time zone definition generated from the time zone info to which this
service is scoped.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceEnabled](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceEnabled.htm)|
Gets or sets a value indicating whether tracing is enabled.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceFlags](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceFlags.htm)|
Gets or sets the trace flags.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceListener](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceListener.htm)|
Gets or sets the trace listener.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Url](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService_Url.htm)|
Gets or sets the URL this service is bound to.  
[UseDefaultCredentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UseDefaultCredentials.htm)|
Gets or sets a value indicating whether the credentials of the user currently
logged into Windows should be used to authenticate with the Exchange Web
Services. Setting UseDefaultCredentials to true automatically sets the
Credentials property to null.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[UserAgent](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UserAgent.htm)|
Gets or sets the user agent.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[WebProxy](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_WebProxy.htm)|
Gets or sets the web proxy that should be used when sending requests to EWS.
Set this property to null to use the default web proxy.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
##  __См. также
#### Ссылки
[AutodiscoverService -
](T_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverService.htm)
[Tessa.Exchange.WebServices.Autodiscover - пространство
имён](N_Tessa_Exchange_WebServices_Autodiscover.htm)
