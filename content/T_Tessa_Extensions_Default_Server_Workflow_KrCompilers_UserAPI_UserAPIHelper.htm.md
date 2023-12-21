# UserAPIHelper - класс
Предоставляет статические методы, используемые в скриптах подсистемы
маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class UserAPIHelper
VB __Копировать
     Public NotInheritable Class UserAPIHelper
C++ __Копировать
     public ref class UserAPIHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type UserAPIHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserAPIHelper
##  __Методы
[AddPerformer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_AddPerformer.htm)|
Добавляет исполнителя в этап с режимом множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).
Исполнитель будет добавлен только если на указанном месте для вставки стоит
другой исполнитель.  
---|---  
[AddStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_AddStageAsync.htm)|
Добавляет новый этап в маршрут.  
[AddTaskHistoryRecordAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_AddTaskHistoryRecordAsync.htm)|
Добавляет запись в текущую группу истории заданий.  
[CardRowsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_CardRowsAsync.htm)|
Возвращает строго типизированную коллекцию строк из секции основной карточки.  
[ForEachStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_ForEachStage.htm)|
Выполняет указанное действие над строкой (из коллекционной секции KrStages)
этапа текущего процесса в обход объектной модели. Секция KrStages получается
из ProcessHolder-сателлита.  
[ForEachStageInMainProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_ForEachStageInMainProcessAsync.htm)|
Асинхронно выполняет указанное действие над строкой (из коллекционной секции
KrStages) этапа основного процесса карточки в обход объектной модели. Секция
KrStages получается из контекстуального сателлита.  
[GetCurrentTaskHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetCurrentTaskHistoryGroupAsync.htm)|
Асинхронно возвращает идентификатор текущей группы истории заданий.  
[GetCycleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetCycleAsync.htm)|
Возвращает номер текущего цикла.  
[GetNewCardAccessStrategy](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetNewCardAccessStrategy.htm)|
Возвращает стратегию загрузки карточки, получаемой из
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Info.htm)
этапа по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[GetNewCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetNewCardAsync.htm)|
Возвращает карточку из
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Info.htm)
этапа, содержащуюся по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[GetOrAddStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetOrAddStageAsync.htm)|
Возвращает или добавляет новый этап в маршрут, если он отсутствует в маршруте.  
[GetPrimaryProcessInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetPrimaryProcessInfoAsync.htm)|
Возвращает хранилище Info для основного процесса карточки.  
[GetProcessInfoForBranch](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetProcessInfoForBranch.htm)|
Возвращает хранилище Info ветки вторичного процесса перед стартом. Актуально
только для этапа ветвления.  
[GetSecondaryProcessInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_GetSecondaryProcessInfoAsync.htm)|
Возвращает хранилище Info для вторичного процесса карточки.  
[HasKrComponents(IKrScript,
KrComponents)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_HasKrComponents.htm)|
Проверяет, поддерживаются ли указанные компоненты настроек типового решения
для текущей карточки.  
[HasKrComponents(IKrScript,
KrComponents[])](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_HasKrComponents_1.htm)|
Проверяет, поддерживаются ли указанные компоненты настроек типового решения
для текущей карточки.  
[IsMainProcess](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_IsMainProcess.htm)|
Текущий выполняемый процесс является основным (KrProcess)  
[IsMainProcessInactiveAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_IsMainProcessInactiveAsync.htm)|
Все этапы основного процесса (KrProcess) для текущей карточки находятся в
состоянии
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)
.  
[IsMainProcessStartedAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_IsMainProcessStartedAsync.htm)|
Возвращает признак, показывающий, что для текущей карточки запущен основной
процесс (KrProcess).  
[PrepareFileInDialogCardForStore](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_PrepareFileInDialogCardForStore.htm)|
Подготавливает файлы карточки диалога к сохранению.  
[PrepareFilesInSettingsDialogCardForStoreAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_PrepareFilesInSettingsDialogCardForStoreAsync.htm)|
Подготавливает файлы карточки диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm) к сохранению.  
[RemovePerformer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_RemovePerformer.htm)|
Удаляет исполнителей имеющих указанные идентификаторы.  
[RemoveStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_RemoveStage.htm)|
Удаляет этап из маршрута, добавленный ранее в скриптах.  
[ResetSinglePerformer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_ResetSinglePerformer.htm)|
Сбрасывает исполнителя для этапа с режимом одиночного исполнителя
[Single](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[Resolve<T>](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_Resolve__1.htm)|
Получить из UnityContainer зависимость.  
[ResolveTaskHistoryGroup](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_ResolveTaskHistoryGroup.htm)|
Возвращает группу истории заданий.  
[SetCycleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_SetCycleAsync.htm)|
Задаёт номер текущего цикла.  
[SetSinglePerformer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_SetSinglePerformer.htm)|
Устанавливает исполнителя для этапа с режимом одиночного исполнителя
[Single](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[SetStageStateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_UserAPIHelper_SetStageStateAsync.htm)|
Асинхронно устанавливает состояние этапа в строке коллекционной секции
KrStages.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)
