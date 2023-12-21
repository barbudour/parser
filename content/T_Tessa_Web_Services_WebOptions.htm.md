# WebOptions - класс
Настройки из app.json для серверной части веб-сервиса.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class WebOptions
VB __Копировать
     Public Class WebOptions
C++ __Копировать
     public ref class WebOptions
F# __Копировать
     type WebOptions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebOptions
##  __Конструкторы
[WebOptions](M_Tessa_Web_Services_WebOptions__ctor.htm)| Инициализирует новый
экземпляр класса WebOptions  
---|---  
##  __Свойства
[AllowedRefererValues](P_Tessa_Web_Services_WebOptions_AllowedRefererValues.htm)|
Допустимые значения HTTP-заголовка Referer, которые проверяются на каждый
запрос или пустая коллекция, если проверка заголовка отключена. При проверке
актуальное значение заголовка должно начинаться с подстроки, указанной в этом
списке, без учёта регистра. Например, возможно перечислить все допустимые
доменные имена с указанием схемы подключения вида: https://tessa.server-
name.org  
---|---  
[CookiesSameSite](P_Tessa_Web_Services_WebOptions_CookiesSameSite.htm)|
Настройка Cookies, создаваемых при логине, для разрешения или запрета их
отправки при выполнении cross site запросов.  
[HealthCheckIsEnabled](P_Tessa_Web_Services_WebOptions_HealthCheckIsEnabled.htm)|
Признак того, что разрешён запрос по адресу /check для проверки
работоспособности веб-сервиса. По умолчанию false, т.е. проверка запрещена,
если в конфигурационном файле нет настройки HealthCheckEnabled.  
[KerberosDisableRealmCheck](P_Tessa_Web_Services_WebOptions_KerberosDisableRealmCheck.htm)|
Признак того, что отключена проверка соответствия Realm целевому объекту. По
умолчанию false, т.е. включена проверка соответствия Realm целевому объекту,
если если в конфигурационном файле нет настройки Kerberos.DisableRealmCheck.  
[KerberosIsEnabled](P_Tessa_Web_Services_WebOptions_KerberosIsEnabled.htm)|
Признак того, что разрешена Kerberos авторизация. По умолчанию false, т.е.
авторизация отключена, если в конфигурационном файле нет настройки
Kerberos.IsEnabled.  
[KerberosKeytabFileMask](P_Tessa_Web_Services_WebOptions_KerberosKeytabFileMask.htm)|
Название маски для поиска Keytab файлов для Kerberos авторизации. По умолчанию
null, т.е. файл не задан, если в конфигурационном файле нет настройки
Kerberos.Keytab.  
[PathBase](P_Tessa_Web_Services_WebOptions_PathBase.htm)|  Базовый путь
приложения. Необходимо использовать, если веб-сервис запускается без
использования IIS. По умолчанию null, т.е. базовый путь не задан, если в
конфигурационном файле нет настройки PathBase.  
[ResponseHeaders](P_Tessa_Web_Services_WebOptions_ResponseHeaders.htm)|
Значения заголовков, передаваемых с каждым ответом на запрос.  
[SwaggerDocIsEnabled](P_Tessa_Web_Services_WebOptions_SwaggerDocIsEnabled.htm)|
Признак того, что разрешён запрос по адресу /swagger для вывода документации
по API. По умолчанию false, т.е. проверка запрещена, если в конфигурационном
файле нет настройки SwaggerDocIsEnabled.  
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
##  __Методы расширения
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
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
