# ISessionService - интерфейс
Сервис, управляющий открытыми сессиями.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionService
VB __Копировать
     Public Interface ISessionService
C++ __Копировать
     public interface class ISessionService
F# __Копировать
     type ISessionService = interface end
##  __Методы
[CloseSessionAsAdminAsync](M_Tessa_Platform_Runtime_ISessionService_CloseSessionAsAdminAsync.htm)|
Закрывает сессию с заданным идентификатором от имени администратора. Закрытие
сессии удаляет её, а также может дополнительно добавить запись в логах аудита
или выполнить другие действия. Возвращает признак того, что сессия ещё была
открыта на момент вызова метода.  
---|---  
[CloseSessionAsync](M_Tessa_Platform_Runtime_ISessionService_CloseSessionAsync.htm)|
Закрывает текущую сессию. Закрытие сессии удаляет её, а также может
дополнительно добавить запись в логах аудита или выполнить другие действия.
Возвращает признак того, что сессия ещё была открыта на момент вызова метода.  
[CloseSessionWithTokenAsync](M_Tessa_Platform_Runtime_ISessionService_CloseSessionWithTokenAsync.htm)|
Закрывает текущую сессию, причём сессия определяется по токену, передаваемому
в параметре. Закрытие сессии удаляет её, а также может дополнительно добавить
запись в логах аудита или выполнить другие действия. Возвращает признак того,
что сессия ещё была открыта на момент вызова метода.  
[IncrementConfigurationVersionAsync](M_Tessa_Platform_Runtime_ISessionService_IncrementConfigurationVersionAsync.htm)|
Увеличивает версию конфигурации без внесения в неё фактических изменений, а
также обновляет информацию по текущей версии платформы. Может использоваться,
например, для сброса клиентского кэша. Метод доступен только администраторам.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
