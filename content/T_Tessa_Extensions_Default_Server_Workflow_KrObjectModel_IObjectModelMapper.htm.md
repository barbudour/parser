# IObjectModelMapper - интерфейс
Описывает объект обеспечивающий работу с хранилищами Kr процесса и объектной
моделью процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IObjectModelMapper
VB __Копировать
     Public Interface IObjectModelMapper
C++ __Копировать
     public interface class IObjectModelMapper
F# __Копировать
     type IObjectModelMapper = interface end
##  __Методы
[CardRowsToObjectModelAsync(Card, ProcessCommonInfo, MainProcessCommonInfo,
String, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_CardRowsToObjectModelAsync.htm)|
Преобразовать секционную модель процесса маршрутов в объектную модель. Метод
предназначен для преобразования карточек документов.  
---|---  
[CardRowsToObjectModelAsync(IKrStageTemplate,
IReadOnlyCollection<IKrRuntimeStage>, MainProcessCommonInfo, Boolean, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_CardRowsToObjectModelAsync_1.htm)|
Преобразует секционную модель процесса маршрутов в объектную модель. Метод
предназначен для преобразования карточек шаблонов этапов.  
[FillWorkflowProcessFromPci](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_FillWorkflowProcessFromPci.htm)|
Заполняет информацию в объектной модели указанной информацией по текущем и
основному процессу.  
[GetMainProcessCommonInfo](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_GetMainProcessCommonInfo.htm)|
Загружает из сателлита-холдера информацию по текущему процессу.  
[GetNestedProcessCommonInfos](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_GetNestedProcessCommonInfos.htm)|
Загружает из сателлита-холдера основную информацию по вложенным процессам.  
[ObjectModelToCardRowsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_ObjectModelToCardRowsAsync.htm)|
Преобразует объектную модель процесса маршрутов в секционную модель с
отслеживанием изменений.  
[ObjectModelToPci](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_ObjectModelToPci.htm)|
Переносит информацию о процессе из объектной модели (process) в: pci, mainPci,
primaryPci.  
[RepairSettings](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_RepairSettings.htm)|
Исправляет ссылки StageRowID в подставленных настройках, а также выставляет
порядок сортировки.  
[SetMainProcessCommonInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_SetMainProcessCommonInfoAsync.htm)|
Асинхронно устанавливает в сателлите-холдере процесса информацию по основному
процессу.  
[SetNestedProcessCommonInfos](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper_SetNestedProcessCommonInfos.htm)|
Устанавливает в сателлит-холдер основную информацию по вложенным процессам.  
## __Методы расширения
[GetTemplateStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetTemplateStagesAsync.htm)|
Возвращает этапы из шаблона этапов.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)
