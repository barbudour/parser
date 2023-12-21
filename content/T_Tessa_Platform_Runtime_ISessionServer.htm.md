# ISessionServer - интерфейс
Объект, обеспечивающий взаимодействие с сессиями на сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionServer
VB __Копировать
     Public Interface ISessionServer
C++ __Копировать
     public interface class ISessionServer
F# __Копировать
     type ISessionServer = interface end
##  __Методы
[AddSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_AddSessionAsync.htm)|
Добавляет информацию по сессии (обычно в базу данных). Сессия автоматически
добавляется в методе открытия сессии.  
---|---  
[ApplyTokenParameters](M_Tessa_Platform_Runtime_ISessionServer_ApplyTokenParameters.htm)|
Устанавливает параметры текущего потока для сессии по заданному токену.  
[CloseSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_CloseSessionAsync.htm)|
Закрывает сессию с заданным идентификатором. Закрытие сессии удаляет её, а
также может дополнительно добавить запись в логах аудита или выполнить другие
действия. Возвращает признак того, что сессия ещё была открыта на момент
вызова метода.  
[DeleteUserSessionsAsync](M_Tessa_Platform_Runtime_ISessionServer_DeleteUserSessionsAsync.htm)|
Удаляет все сессии заданного сотрудника.  
[OpenSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_OpenSessionAsync.htm)|
Открывает сессию по заданным параметрам. Возвращает токен для открытой сессии.  
[RemoveSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_RemoveSessionAsync.htm)|
Удаляет сессию с заданным идентификатором. Возвращает признак того, что сессия
ещё была открыта на момент вызова метода.  
[SetSessionIsActiveAsync](M_Tessa_Platform_Runtime_ISessionServer_SetSessionIsActiveAsync.htm)|
Устанавливает признак активности сессии. Возвращает true, если признак
активности был изменён для существующей сессии.  
[TryGetSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_TryGetSessionAsync.htm)|
Загружает информацию по сессии для заданного идентификатора сессии. Возвращает
null, если сессия не найдена.  
[TryGetSessionIDToDeactivateAsync](M_Tessa_Platform_Runtime_ISessionServer_TryGetSessionIDToDeactivateAsync.htm)|
Возвращает идентификатор сессии, которую можно деактивировать, чтобы получить
лицензию (обычно конкурентную), или null, если такая сессия отсутствует.  
[UpdateLastActivityAsync](M_Tessa_Platform_Runtime_ISessionServer_UpdateLastActivityAsync.htm)|
Обновляет дату последней активности для сессии. Рекомендуется периодически
вызывать метод, чтобы сессия не была удалена автоматически при отсутствии
другой активности. Возвращает признак того, что сессия была открыта на момент
вызова метода.  
[ValidateAndGetSessionAsync](M_Tessa_Platform_Runtime_ISessionServer_ValidateAndGetSessionAsync.htm)|
Проверяет всю информацию по сессии, которая может быть получена со стороны
клиента. Возвращает объект сессии (отличный от null) со всей актуальной
информацией. Для сессии также обновляет дату последней активности. В случае
ошибок (в т.ч. при отсутствии сессии, добавленной в системе) выбрасывается
исключение [Tessa.Platform.Runtime.SessionException].  
[ValidateBasicFields](M_Tessa_Platform_Runtime_ISessionServer_ValidateBasicFields.htm)|
Проверяет основную информацию по сессии, которая может быть получена со
стороны клиента. В случае ошибок выбрасывается исключение
[Tessa.Platform.Runtime.SessionException].  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
