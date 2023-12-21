# ISessionVersionHolder - интерфейс
Объект, содержащий версию платформы на сервере, связанную с текущей сессией.
Используется на клиенте после успешного логина.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionVersionHolder
VB __Копировать
     Public Interface ISessionVersionHolder
C++ __Копировать
     public interface class ISessionVersionHolder
F# __Копировать
     type ISessionVersionHolder = interface end
##  __Свойства
[PlatformVersion](P_Tessa_Platform_Runtime_ISessionVersionHolder_PlatformVersion.htm)|
Версия платформы на сервере или null, если логин ещё не выполнен или сервер не
сообщил версию. Возвращается после успешного логина, если сервер её сообщает.
Используйте значение
[UnknownServerPlatformVersion](P_Tessa_Platform_Runtime_RuntimeHelper_UnknownServerPlatformVersion.htm),
если известно, что логин выполнен, но свойство возвращает null.  
---|---  
## __Методы
[SetPlatformVersionAsync](M_Tessa_Platform_Runtime_ISessionVersionHolder_SetPlatformVersionAsync.htm)|
Устанавливает версию платформы для текущей сессии. Может быть равен null, если
считается, что версия неизвестна.  
---|---  
## __События
[PlatformVersionChanged](E_Tessa_Platform_Runtime_ISessionVersionHolder_PlatformVersionChanged.htm)|
Событие, происходящее при изменении токена для текущей сессии.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
