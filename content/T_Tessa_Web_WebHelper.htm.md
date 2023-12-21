# WebHelper - класс
##  __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WebHelper
VB __Копировать
     Public NotInheritable Class WebHelper
C++ __Копировать
     public ref class WebHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WebHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebHelper
##  __Свойства
[ControllerAssemblies](P_Tessa_Web_WebHelper_ControllerAssemblies.htm)|
Список сборок, из которых были загружены контроллеры для обработки REST-
запросов.  
---|---  
[HttpContext](P_Tessa_Web_WebHelper_HttpContext.htm)|  
## __Методы
[Configure](M_Tessa_Web_WebHelper_Configure.htm)|  
---|---  
[GetBoundary](M_Tessa_Web_WebHelper_GetBoundary.htm)|  
[GetRewrittenPathStartsWithServiceName](M_Tessa_Web_WebHelper_GetRewrittenPathStartsWithServiceName.htm)|
/web/route => /route  
[GetSessionCallback](M_Tessa_Web_WebHelper_GetSessionCallback.htm)|  
[GetTypedJsonBodyFlags](M_Tessa_Web_WebHelper_GetTypedJsonBodyFlags.htm)|  
[GetWebContext](M_Tessa_Web_WebHelper_GetWebContext.htm)|  
[InitializeLocalizationAsync](M_Tessa_Web_WebHelper_InitializeLocalizationAsync.htm)|  
[InitializeWebServerAsync](M_Tessa_Web_WebHelper_InitializeWebServerAsync.htm)|
Выполняет инициализацию веб-приложения, построенного на платформе Tessa.
Рекомендуется вызвать перед методом CreateHostBuilder. Также обычно требуется
вызвать метод [InitializeFromConfigurationAsync(Boolean,
IConfigurationManager,
CancellationToken)](M_Tessa_Platform_TessaPlatform_InitializeFromConfigurationAsync.htm)
для инициализации платформы из конфигурации.  
[IsCheckPath](M_Tessa_Web_WebHelper_IsCheckPath.htm)|  
[IsDesktopOrUtilitaryPath](M_Tessa_Web_WebHelper_IsDesktopOrUtilitaryPath.htm)|  
[IsDesktopPath](M_Tessa_Web_WebHelper_IsDesktopPath.htm)|  
[IsDevelopmentHotEnvironment](M_Tessa_Web_WebHelper_IsDevelopmentHotEnvironment.htm)|  
[IsMultipartContentType](M_Tessa_Web_WebHelper_IsMultipartContentType.htm)|  
[IsSwaggerPath](M_Tessa_Web_WebHelper_IsSwaggerPath.htm)|  
[LoadCertificate(WebServerOptions, Boolean,
String)](M_Tessa_Web_WebHelper_LoadCertificate_1.htm)|  
[LoadCertificate(String, String, String, Nullable<StoreName>,
Nullable<StoreLocation>, String, Boolean,
String)](M_Tessa_Web_WebHelper_LoadCertificate.htm)|  
[LoadDataProtectionCertificate](M_Tessa_Web_WebHelper_LoadDataProtectionCertificate.htm)|  
[ParseBooleanFromStorage](M_Tessa_Web_WebHelper_ParseBooleanFromStorage.htm)|  
[ParseDoubleFromStorage](M_Tessa_Web_WebHelper_ParseDoubleFromStorage.htm)|  
[ParseEnumFromStorage<T>](M_Tessa_Web_WebHelper_ParseEnumFromStorage__1.htm)|  
[ParseInt32FromStorage](M_Tessa_Web_WebHelper_ParseInt32FromStorage.htm)|  
[ParseInt64FromStorage](M_Tessa_Web_WebHelper_ParseInt64FromStorage.htm)|  
[ParseNullableEnumFromStorage<T>](M_Tessa_Web_WebHelper_ParseNullableEnumFromStorage__1.htm)|  
[ParseStringFromStorage](M_Tessa_Web_WebHelper_ParseStringFromStorage.htm)|  
[ParseUrlsFromCommandLine](M_Tessa_Web_WebHelper_ParseUrlsFromCommandLine.htm)|  
[ParseUrlToEndPoint](M_Tessa_Web_WebHelper_ParseUrlToEndPoint.htm)|  
[PathStartsWithServiceName](M_Tessa_Web_WebHelper_PathStartsWithServiceName.htm)|  
[SetSessionCallback](M_Tessa_Web_WebHelper_SetSessionCallback.htm)|  
[SetTypedJsonBodyFlags](M_Tessa_Web_WebHelper_SetTypedJsonBodyFlags.htm)|  
[SetWebContext](M_Tessa_Web_WebHelper_SetWebContext.htm)|  
## __Поля
[ContextSystemKeyPrefix](F_Tessa_Web_WebHelper_ContextSystemKeyPrefix.htm)|  
---|---  
[HttpProtocol](F_Tessa_Web_WebHelper_HttpProtocol.htm)|  
[HttpsProtocol](F_Tessa_Web_WebHelper_HttpsProtocol.htm)|  
## __См. также
#### Ссылки
[Tessa.Web - пространство имён](N_Tessa_Web.htm)
