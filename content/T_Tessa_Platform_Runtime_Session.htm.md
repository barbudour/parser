# Session - класс
Сессия пользователя.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Session : ISession
VB __Копировать
     Public NotInheritable Class Session
    	Implements ISession
C++ __Копировать
     public ref class Session sealed : ISession
F# __Копировать
     [<SealedAttribute>]
    type Session = 
        class
            interface ISession
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Session
Implements
    [ISession](T_Tessa_Platform_Runtime_ISession.htm)
##  __Конструкторы
[Session(SessionType,
ISessionToken)](M_Tessa_Platform_Runtime_Session__ctor_1.htm)|  Создаёт
экземпляр класса с указанием токена. Тип сессии явно указывается в параметре
sessionType.  
---|---  
[Session(SessionType, Func<ISessionToken>, Func<ISession, String>,
Func<ISession, String>)](M_Tessa_Platform_Runtime_Session__ctor.htm)|  Создаёт
экземпляр класса с указанием функции, получающей токен.  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_Session_ApplicationID.htm)|
Идентификатор приложения, которое открыло сессию, или null, если в сессии
отсутствует токен.  
---|---  
[ClientCulture](P_Tessa_Platform_Runtime_Session_ClientCulture.htm)|  Текущая
культура CurrentCulture на клиенте в момент вызова метода. Позволяет получить
на сервере культуру, которая использовалась на клиенте.  
[ClientUICulture](P_Tessa_Platform_Runtime_Session_ClientUICulture.htm)|
Текущая культура CurrentUICulture на клиенте в момент вызова метода. Позволяет
получить на сервере культуру, которая использовалась на клиенте.  
[ClientUtcOffset](P_Tessa_Platform_Runtime_Session_ClientUtcOffset.htm)|
Смещение относительно UTC на клиенте в момент вызова метода. Позволяет
получить на сервере информацию по временной зоне, которая использовалась на
клиенте.  
[ID](P_Tessa_Platform_Runtime_Session_ID.htm)| Идентификатор сессии.  
[InstanceName](P_Tessa_Platform_Runtime_Session_InstanceName.htm)| Имя
экземпляра сервера.  
[ServerCode](P_Tessa_Platform_Runtime_Session_ServerCode.htm)| Код сервера.  
[Token](P_Tessa_Platform_Runtime_Session_Token.htm)|  Токен, описывающий
сессию, или null, если сессия не связана с токеном.  
[Type](P_Tessa_Platform_Runtime_Session_Type.htm)| Тип сессии, определяющий
место выполнения кода.  
[User](P_Tessa_Platform_Runtime_Session_User.htm)| Информация о текущем
пользователе.  
##  __Методы
[CreateSystemSession](M_Tessa_Platform_Runtime_Session_CreateSystemSession.htm)|
Создаёт сессию пользователя, назначенного для платформы.  
---|---  
[CreateSystemToken](M_Tessa_Platform_Runtime_Session_CreateSystemToken.htm)|
Создаёт токен для сессии пользователя, назначенного для платформы.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
##  __Поля
[SystemID](F_Tessa_Platform_Runtime_Session_SystemID.htm)|  Идентификатор
пользователя, назначенного для платформы.  
---|---  
[SystemName](F_Tessa_Platform_Runtime_Session_SystemName.htm)|  Имя
пользователя, назначенного для платформы.  
[SystemSatelliteID](F_Tessa_Platform_Runtime_Session_SystemSatelliteID.htm)|
Идентификатор карточки-сателлита с настройками пользователя
[SystemID](F_Tessa_Platform_Runtime_Session_SystemID.htm), назначенного для
платформы.  
## __Методы расширения
[CreateNestedSessionToken](M_Tessa_Platform_Runtime_RuntimeExtensions_CreateNestedSessionToken.htm)|
Создаёт токен [SessionToken](T_Tessa_Platform_Runtime_SessionToken.htm) для
сотрудника с заданными настройками, но наследующий информацию по серверу и
текущей культуре из текущей сессии session. Используйте возвращённый токен в
объекте [SessionContext](T_Tessa_Platform_Runtime_SessionContext.htm), который
создаётся для выполнения действий в пределах уже существующей сессии,
например, со стороны веб-сервисов.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsDesktopClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsDesktopClient.htm)|
Возвращает признак того, что сессия была открыта с десктопного клиента (т.е. с
"толстого" клиента). Это могут быть приложения TessaAdmin, TessaClient,
консольный tadmin, интеграционный веб-сервис и др.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[IsNotWebOrDesktopClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsNotWebOrDesktopClient.htm)|
Возвращает признак того, что сессия была открыта не с десктопного клиента и не
с Web-клиента. Обычно это плагины Chronos, интеграционные веб-сервисы с
собственной авторизацией и другие приложения.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[IsWebClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsWebClient.htm)|
Возвращает признак того, что сессия была открыта с Web-клиента (т.е. с
"лёгкого" клиента). Это или Web-клиент Tessa, или интеграция через Web API.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
