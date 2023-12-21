# GetUserSettingsResponse - класс
Represents the response to a GetUsersSettings call for an individual user.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Autodiscover](N_Tessa_Exchange_WebServices_Autodiscover.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GetUserSettingsResponse : AutodiscoverResponse
VB __Копировать
     Public NotInheritable Class GetUserSettingsResponse
    	Inherits AutodiscoverResponse
C++ __Копировать
     public ref class GetUserSettingsResponse sealed : public AutodiscoverResponse
F# __Копировать
     [<SealedAttribute>]
    type GetUserSettingsResponse = 
        class
            inherit AutodiscoverResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[AutodiscoverResponse](T_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverResponse.htm) __ GetUserSettingsResponse
##  __Конструкторы
[GetUserSettingsResponse](M_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse__ctor.htm)|
Initializes a new instance of the GetUserSettingsResponse class.  
---|---  
## __Свойства
[ErrorCode](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverResponse_ErrorCode.htm)|
Gets the error code that was returned by the service.  
(Унаследован от
[AutodiscoverResponse](T_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverResponse.htm))  
---|---  
[ErrorMessage](P_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverResponse_ErrorMessage.htm)|
Gets the error message that was returned by the service.  
(Унаследован от
[AutodiscoverResponse](T_Tessa_Exchange_WebServices_Autodiscover_AutodiscoverResponse.htm))  
[RedirectTarget](P_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse_RedirectTarget.htm)|
Gets the redirectionTarget (URL or email address)  
[Settings](P_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse_Settings.htm)|
Gets the requested settings for the user.  
[SmtpAddress](P_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse_SmtpAddress.htm)|
Gets the SMTP address this response applies to.  
[UserSettingErrors](P_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse_UserSettingErrors.htm)|
Gets error information for settings that could not be returned.  
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
[TryGetSettingValue<T>](M_Tessa_Exchange_WebServices_Autodiscover_GetUserSettingsResponse_TryGetSettingValue__1.htm)|
Tries the get the user setting value.  
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
[Tessa.Exchange.WebServices.Autodiscover - пространство
имён](N_Tessa_Exchange_WebServices_Autodiscover.htm)
