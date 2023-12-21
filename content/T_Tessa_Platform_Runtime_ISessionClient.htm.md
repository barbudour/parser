# ISessionClient - интерфейс
Объект, обеспечивающий взаимодействие с сессиями на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionClient
VB __Копировать
     Public Interface ISessionClient
C++ __Копировать
     public interface class ISessionClient
F# __Копировать
     type ISessionClient = interface end
##  __Методы
[CloseSessionAsAdminAsync](M_Tessa_Platform_Runtime_ISessionClient_CloseSessionAsAdminAsync.htm)|
Закрывает сессию с заданным идентификатором от имени администратора. Закрытие
сессии удаляет её, а также может дополнительно добавить запись в логах аудита
или выполнить другие действия. Возвращает признак того, что сессия ещё была
открыта на момент вызова метода.  
---|---  
[CloseSessionAsync](M_Tessa_Platform_Runtime_ISessionClient_CloseSessionAsync.htm)|
Закрывает текущую сессию. Закрытие сессии удаляет её, а также может
дополнительно добавить запись в логах аудита или выполнить другие действия.
Возвращает признак того, что сессия ещё была открыта на момент вызова метода.  
[IncrementConfigurationVersionAsync](M_Tessa_Platform_Runtime_ISessionClient_IncrementConfigurationVersionAsync.htm)|
Увеличивает версию конфигурации без внесения в неё фактических изменений, а
также обновляет информацию по текущей версии платформы. Может использоваться,
например, для сброса клиентского кэша. Метод доступен только администраторам.  
[OpenSessionAsync](M_Tessa_Platform_Runtime_ISessionClient_OpenSessionAsync.htm)|
Выполняет аутентификацию пользователя, используя анонимную аутентификацию по
учётной записи Windows и по заданным параметрам логин/пароль/доменное имя, или
используя аутентификацию для пользователя Tessa. Открывает сессию и возвращает
её токен [Tessa.Platform.Runtime.SessionToken], сериализованный в формате XML.  
[OpenSessionWindowsAuthAsync](M_Tessa_Platform_Runtime_ISessionClient_OpenSessionWindowsAuthAsync.htm)|
Выполняет аутентификацию пользователя по учётной записи Windows. Открывает
сессию и возвращает её токен [Tessa.Platform.Runtime.SessionToken],
сериализованный в формате XML.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
