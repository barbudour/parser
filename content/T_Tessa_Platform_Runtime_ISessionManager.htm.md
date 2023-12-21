# ISessionManager - интерфейс
Объект для управления клиентскими сессиями.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionManager : IDisposable
VB __Копировать
     Public Interface ISessionManager
    	Inherits IDisposable
C++ __Копировать
     public interface class ISessionManager : IDisposable
F# __Копировать
     type ISessionManager = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ISessionManager_ApplicationID.htm)|
Идентификатор приложения. По умолчанию значение свойства равно
[Tessa.Platform.Runtime.ApplicationIdentifiers.Other]. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
---|---  
[Credentials](P_Tessa_Platform_Runtime_ISessionManager_Credentials.htm)|
Параметры входа, используемые при первичном открытии сессии или при повторном
открытии, или null, если при следующем открытии сессии будут использоваться
параметры по умолчанию.  
[IsOpened](P_Tessa_Platform_Runtime_ISessionManager_IsOpened.htm)| Признак
того, что сессия открыта.  
[LoginParameters](P_Tessa_Platform_Runtime_ISessionManager_LoginParameters.htm)|
Параметры диалога входа (ввода логина и пароля), если используется диалог с
UI. Свойство нельзя установить равным null.  
## __Методы
[CloseAsync](M_Tessa_Platform_Runtime_ISessionManager_CloseAsync.htm)|
Закрывает открытую ранее сессию.  
---|---  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
[OpenAsync](M_Tessa_Platform_Runtime_ISessionManager_OpenAsync.htm)|
Открывает сессию от имени текущего пользователя и гарантирует её периодическое
поддержание. Возвращает признак того, что сессия была успешно открыта.  
## __События
[SessionClosed](E_Tessa_Platform_Runtime_ISessionManager_SessionClosed.htm)|
Событие, происходящее при каждом успешном закрытии сессии (методом Open или
повторное открытие по таймеру при истечении срока сессии).  
---|---  
[SessionOpened](E_Tessa_Platform_Runtime_ISessionManager_SessionOpened.htm)|
Событие, происходящее при каждом успешном открытии сессии (методом Open или
повторное открытие по таймеру при истечении срока сессии).  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
