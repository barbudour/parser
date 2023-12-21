# IWorkflowEngineCardsScope - интерфейс
Scope для загрузки карточек в рамках обработки WorkflowEngine.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineCardsScope
VB __Копировать
     Public Interface IWorkflowEngineCardsScope
C++ __Копировать
     public interface class IWorkflowEngineCardsScope
F# __Копировать
     type IWorkflowEngineCardsScope = interface end
##  __Свойства
[CardStorePriorityComparer](P_Tessa_Workflow_IWorkflowEngineCardsScope_CardStorePriorityComparer.htm)|
Возвращает или задаёт компаратор определяющий порядок сохранения карточек.
Может иметь значение по умолчанию для типа, в этом случае упорядочивание
карточек при сохранении не выполняется.  
---|---  
## __Методы
[AddNewCard](M_Tessa_Workflow_IWorkflowEngineCardsScope_AddNewCard.htm)|
Добавляет указанную карточку в Scope.  
---|---  
[CardIsLoaded](M_Tessa_Workflow_IWorkflowEngineCardsScope_CardIsLoaded.htm)|
Проверяет, загружена ли карточка с заданным идентификатором или нет.  
[Create](M_Tessa_Workflow_IWorkflowEngineCardsScope_Create.htm)|  Создаёт
контекст загрузки карточек для WorkflowEngine.  
[GetCardAsync(Guid, IValidationResultBuilder,
CancellationToken)](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetCardAsync_1.htm)|
Загружает карточку с заданным идентификатором.  
[GetCardAsync(Guid, Func<Guid, CardGetRequest>, IValidationResultBuilder,
CancellationToken)](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetCardAsync.htm)|
Загружает карточку имеющую указанный идентификатор, если карточка не найдена в
кэше карточек, то она загружается из БД.  
[GetCardForSendTasksAsync](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetCardForSendTasksAsync.htm)|
Создаёт и возвращает карточку для отправки задания.  
[GetFileContainerAsync](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetFileContainerAsync.htm)|
Возвращает файловый контейнер для карточки с заданным идентификатором.  
[GetLoadedCards](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetLoadedCards.htm)|
Возвращает перечисление загруженных карточек.  
[GetLoadedFileContainers](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetLoadedFileContainers.htm)|
Возвращает перечисление загруженных контейнеров файлов.  
[GetSatelliteAsync](M_Tessa_Workflow_IWorkflowEngineCardsScope_GetSatelliteAsync.htm)|
Возвращает карточку сателлита.  
[InvalidateAsync](M_Tessa_Workflow_IWorkflowEngineCardsScope_InvalidateAsync.htm)|
Сбрасывает все загруженные объекты.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
