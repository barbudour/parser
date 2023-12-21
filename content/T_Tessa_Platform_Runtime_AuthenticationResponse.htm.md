# AuthenticationResponse - класс
Ответ на запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AuthenticationResponse : IAuthenticationResponse
VB __Копировать
     Public NotInheritable Class AuthenticationResponse
    	Implements IAuthenticationResponse
C++ __Копировать
     public ref class AuthenticationResponse sealed : IAuthenticationResponse
F# __Копировать
     [<SealedAttribute>]
    type AuthenticationResponse = 
        class
            interface IAuthenticationResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AuthenticationResponse
Implements
    [IAuthenticationResponse](T_Tessa_Platform_Runtime_IAuthenticationResponse.htm)
##  __Свойства
[ErrorMessage](P_Tessa_Platform_Runtime_AuthenticationResponse_ErrorMessage.htm)|
Текстовое описание возникшей ошибки или null, если ошибка не возникла или с
ошибкой не связано текстовое описание (оно будет предоставлено автоматически).
Точка в конце сообщения ставится автоматически.  
---|---  
[Exception](P_Tessa_Platform_Runtime_AuthenticationResponse_Exception.htm)|
Возникшее исключение или null, если ошибка не возникла или ошибка не связана с
исключением.  
[ExceptionCode](P_Tessa_Platform_Runtime_AuthenticationResponse_ExceptionCode.htm)|
Код ошибки для исключения [SessionException] или
[SessionExceptionCode.Unknown], если ошибка не возникла или код ошибки не
предоставляется.  
[Info](P_Tessa_Platform_Runtime_AuthenticationResponse_Info.htm)|
Дополнительная информация для классов-расширений.  
[Success](P_Tessa_Platform_Runtime_AuthenticationResponse_Success.htm)|
Признак того, что аутентификация прошла успешно.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Error](M_Tessa_Platform_Runtime_AuthenticationResponse_Error.htm)|  Создаёт
объект с описанием произошедшей ошибки.  
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
[Successful](M_Tessa_Platform_Runtime_AuthenticationResponse_Successful.htm)|
Создаёт объект успешного ответа на запрос.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
