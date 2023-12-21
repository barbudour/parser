# IKrProcessCache - интерфейс
Кэш данных из карточек подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessCache
VB __Копировать
     Public Interface IKrProcessCache
C++ __Копировать
     public interface class IKrProcessCache
F# __Копировать
     type IKrProcessCache = interface end
##  __Методы
[GetActionsByTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetActionsByTypeAsync.htm)|
Возвращает коллекцию, содержащую информацию о действиях указанного типа.  
---|---  
[GetAllActionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllActionsAsync.htm)|
Возвращает словарь, содержащий информацию о всех действиях.  
[GetAllButtonsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllButtonsAsync.htm)|
Возвращает словарь, содержащий информацию о всех кнопках вторичных процессов.  
[GetAllCommonMethodsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllCommonMethodsAsync.htm)|
Возвращает коллекцию с информацией о всех базовых методах.  
[GetAllPureProcessesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllPureProcessesAsync.htm)|
Возвращает информацию о всех вторичных процессах типа "простой процесс".  
[GetAllRuntimeStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllRuntimeStagesAsync.htm)|
Возвращает словарь, содержащий информацию о всех рантайм скриптах.  
[GetAllStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllStageGroupsAsync.htm)|
Возвращает информацию о всех группах этапов.  
[GetAllStagesByTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllStagesByTemplatesAsync.htm)|
Возвращает коллекцию, содержащую информацию о этапах, расположенных в шаблонах
этапов.  
[GetAllStageTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetAllStageTemplatesAsync.htm)|
Возвращает словарь, содержащий информацию о всех шаблонах этапов.  
[GetOrderedStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetOrderedStageGroupsAsync.htm)|
Возвращает список всех групп этапов.  
[GetStageGroupsForSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetStageGroupsForSecondaryProcessAsync.htm)|
Возвращает коллекцию с информацией о группах этапов для заданного процесса.  
[GetStageTemplatesForGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_GetStageTemplatesForGroupAsync.htm)|
Возвращает коллекцию с информацией о всех шаблонах этапов, входящих в заданную
группу.  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_InvalidateAsync.htm)|
Сбрасывает кэш.  
[TryGetSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache_TryGetSecondaryProcessAsync.htm)|
Возвращает вторичный процесс по его идентификатору.  
## __Методы расширения
[GetSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCacheExtensions_GetSecondaryProcessAsync.htm)|
Возвращает вторичный процесс по его идентификатору.  
(Определяется
[KrProcessCacheExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCacheExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
