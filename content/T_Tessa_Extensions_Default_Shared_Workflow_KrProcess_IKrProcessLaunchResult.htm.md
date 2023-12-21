# IKrProcessLaunchResult - интерфейс
Результат запуска процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessLaunchResult
VB __Копировать
     Public Interface IKrProcessLaunchResult
C++ __Копировать
     public interface class IKrProcessLaunchResult
F# __Копировать
     type IKrProcessLaunchResult = interface end
##  __Свойства
[CardResponse](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_CardResponse.htm)|
Ответ на универсальный запрос, при котором был запущен процесс.  
---|---  
[LaunchStatus](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_LaunchStatus.htm)|
Статус запуска процесса.  
[ProcessID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_ProcessID.htm)|
Идентификатор запущенного асинхронного процесса или значение null, если при
запуске процесса произошла ошибка или запускался синхронный процесс.  
[ProcessInfo](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_ProcessInfo.htm)|
Дополнительная информация процесса после его завершения.  
[StoreResponse](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_StoreResponse.htm)|
Ответ на запрос на сохранение, при котором был запущен процесс.  
[ValidationResult](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_ValidationResult.htm)|
Объект, используемый для построения результата валидации.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
