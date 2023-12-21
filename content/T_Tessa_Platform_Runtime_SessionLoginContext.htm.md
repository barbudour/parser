# SessionLoginContext - класс
Контекст операции по входу в систему.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionLoginContext : ISessionLoginContext
VB __Копировать
     Public NotInheritable Class SessionLoginContext
    	Implements ISessionLoginContext
C++ __Копировать
     public ref class SessionLoginContext sealed : ISessionLoginContext
F# __Копировать
     [<SealedAttribute>]
    type SessionLoginContext = 
        class
            interface ISessionLoginContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionLoginContext
Implements
    [ISessionLoginContext](T_Tessa_Platform_Runtime_ISessionLoginContext.htm)
##  __Конструкторы
[SessionLoginContext(CancellationToken)](M_Tessa_Platform_Runtime_SessionLoginContext__ctor.htm)|
Создаёт экземпляр класса.  
---|---  
[SessionLoginContext(ISessionToken,
CancellationToken)](M_Tessa_Platform_Runtime_SessionLoginContext__ctor_1.htm)|
Создаёт экземпляр класса с указанием токена сессии, который используется для
заполнения свойств. Свойство
[ApplicationLicenseType](P_Tessa_Platform_Runtime_SessionLoginContext_ApplicationLicenseType.htm)
при этом не заполняется.  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_SessionLoginContext_ApplicationID.htm)|
Идентификатор приложения, для которого выполняется вход, или null, если
идентификатор не указан.  
---|---  
[ApplicationLicenseType](P_Tessa_Platform_Runtime_SessionLoginContext_ApplicationLicenseType.htm)|
Тип лицензии, потребляемой при входе.  
[CancellationToken](P_Tessa_Platform_Runtime_SessionLoginContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[ExpectedLoginType](P_Tessa_Platform_Runtime_SessionLoginContext_ExpectedLoginType.htm)|
Ожидаемый тип входа или null, если тип входа определяется автоматически.  
[HostIP](P_Tessa_Platform_Runtime_SessionLoginContext_HostIP.htm)|  IP адрес
компьютера, с которого выполняется вход, или null, если адрес недоступен.  
[HostName](P_Tessa_Platform_Runtime_SessionLoginContext_HostName.htm)|  DNS-
имя компьютера, с которого выполняется вход, или null, если имя недоступно.  
[Login](P_Tessa_Platform_Runtime_SessionLoginContext_Login.htm)| Логин
сотрудника.  
##  __Методы
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
