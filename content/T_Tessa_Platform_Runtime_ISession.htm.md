# ISession - интерфейс
Сессия пользователя.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISession
VB __Копировать
     Public Interface ISession
C++ __Копировать
     public interface class ISession
F# __Копировать
     type ISession = interface end
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ISession_ApplicationID.htm)|
Идентификатор приложения, которое открыло сессию, или null, если в сессии
отсутствует токен.  
---|---  
[ClientCulture](P_Tessa_Platform_Runtime_ISession_ClientCulture.htm)|  Текущая
культура CurrentCulture на клиенте в момент вызова метода. Позволяет получить
на сервере культуру, которая использовалась на клиенте.  
[ClientUICulture](P_Tessa_Platform_Runtime_ISession_ClientUICulture.htm)|
Текущая культура CurrentUICulture на клиенте в момент вызова метода. Позволяет
получить на сервере культуру, которая использовалась на клиенте.  
[ClientUtcOffset](P_Tessa_Platform_Runtime_ISession_ClientUtcOffset.htm)|
Смещение относительно UTC на клиенте в момент вызова метода. Позволяет
получить на сервере информацию по временной зоне, которая использовалась на
клиенте.  
[ID](P_Tessa_Platform_Runtime_ISession_ID.htm)| Идентификатор сессии.  
[InstanceName](P_Tessa_Platform_Runtime_ISession_InstanceName.htm)| Имя
экземпляра сервера.  
[ServerCode](P_Tessa_Platform_Runtime_ISession_ServerCode.htm)| Код сервера.  
[Token](P_Tessa_Platform_Runtime_ISession_Token.htm)|  Токен, описывающий
сессию, или null, если сессия не связана с токеном.  
[Type](P_Tessa_Platform_Runtime_ISession_Type.htm)| Тип сессии, определяющий
место выполнения кода.  
[User](P_Tessa_Platform_Runtime_ISession_User.htm)| Информация о текущем
пользователе.  
##  __Методы расширения
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
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
