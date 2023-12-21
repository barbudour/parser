# WorkflowEngineExtensions - класс
Класс, расширяющий функциональность некоторых классов, необходимых для работы
WorkflowEngine
## __Definition
 **Пространство имён:** [Tessa.Workflow.Helpful](N_Tessa_Workflow_Helpful.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowEngineExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class WorkflowEngineExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class WorkflowEngineExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type WorkflowEngineExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineExtensions
##  __Методы
[AddTiles](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_AddTiles.htm)|
Метод для добавления тайлов  
---|---  
[CreatePlaceholderInfo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_CreatePlaceholderInfo.htm)|
Метод для создания объекта с дополнительний информацией для контекста
плейсхолдеров из контекста обработки бизнес-процессов.  
[CreatePlaceholderInfoWithoutTask](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_CreatePlaceholderInfoWithoutTask.htm)|
Метод для создания объекта с дополнительний информацией для контекста
плейсхолдеров из контекста обработки бизнес-процессов без передачи информации
о задании.  
[GetActionInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetActionInstance.htm)|
Метод для получения экземпляра действия из Info запроса  
[GetActionTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetActionTemplate.htm)|
Метод для получения шаблона действия из Info запроса  
[GetDialogInfos](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetDialogInfos.htm)|  
[GetEventName](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetEventName.htm)|
Метод для получения события из Info запроса  
[GetHashBinder](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetHashBinder.htm)|
Метод для получения биндера хеша из Info  
[GetHistoryGroup](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetHistoryGroup.htm)|  
[GetNodeInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetNodeInstance.htm)|
Метод для получения экземпляра узла из Info запроса  
[GetNodeTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetNodeTemplate.htm)|
Метод для получения шаблона узла из Info запроса  
[GetProcessID](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessID.htm)|
Метод для получения ID экземпляра процесса из Info запроса  
[GetProcessInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessInstance.htm)|
Метод для получения экземпляра процесса из Info запроса  
[GetProcessRequest](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessRequest.htm)|
Возвращает запрос на обработку процесса WorkflowEngine и его подпись.  
[GetProcessTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessTemplate.htm)|
Метод для получения шаблона процесса из Info запроса  
[GetProcessTemplateCardID](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessTemplateCardID.htm)|
Метод для получения ID карточки шаблона процесса из Info запроса  
[GetSources](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetSources.htm)|
Метод для получения исходников скриптов шаблона прцоесса из Info запроса  
[GetWorkflowAccessChecked](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowAccessChecked.htm)|
Метод для получения из Info информации о том, что проверка на выполнение
операции в WorkflowEngine пройдена.  
[GetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowContext.htm)|
Метод для получения контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) из
контекста проверки условий
[IConditionContext](T_Tessa_Platform_Conditions_IConditionContext.htm)  
[GetWorkflowTileID](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowTileID.htm)|
Метод для получения ID выполняемой кнопки из info  
[GetWorkflowType](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowType.htm)|
Метод для получения типа Workflow из info  
[Has](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_Has.htm)| Возвращает
признак того, что заданный флаг установлен.  
[HasAny](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_HasAny.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasNot](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_HasNot.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[SerializeTo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SerializeTo.htm)|
Метод для сериализации карточки процесса напрямую в Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
[SetActionInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetActionInstance.htm)|
Метод для установки экземпляра дейсвтия в Info запроса  
[SetActionTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetActionTemplate.htm)|
Метод для установки шаблона действия в Info запроса  
[SetHashBinder](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetHashBinder.htm)|
Метод для установки биндера хеша в Info  
[SetHistoryGroup](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetHistoryGroup.htm)|  
[SetNodeInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetNodeInstance.htm)|
Метод для установки экземпляра узла в Info запроса  
[SetNodeTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetNodeTemplate.htm)|
Метод для установки шаблона узла в Info запроса  
[SetProcessInfo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetProcessInfo.htm)|
Метод для установки параметров запуска или выполнения процесса WorkflowEngine
в Info запроса  
[SetProcessInstance](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetProcessInstance.htm)|
Метод для установки экземпляра процесса в Info запроса  
[SetProcessRequest](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetProcessRequest.htm)|
Метод для установки в Info запроса на обработку процесса WorkflowEngine с его
подписью. Если подпись не валидна, при попытке обработки переданного запроса
произойдет ошибка. Если подпись отсутствует, то выполняется проверка доступа
пользователя на редактирование шаблона бизнес-процесса.  
[SetProcessTemplate](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetProcessTemplate.htm)|
Метод для установки шаблона процесса в Info запроса  
[SetSources](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetSources.htm)|
Метод для установки исходников скриптов шаблона прцоесса в Info запроса  
[SetWorkflowAccessChecked](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowAccessChecked.htm)|
Метод для установки в Info информации о том, что проверка на выполнение
операции в WorkflowEngine пройдена.  
[SetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowContext.htm)|
Метод для установки контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) в
контекст проверки условий
[IConditionContext](T_Tessa_Platform_Conditions_IConditionContext.htm)  
[SetWorkflowTileID](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowTileID.htm)|
Метод для установки ID выполняемй кнопки в info  
[SetWorkflowType](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowType.htm)|
Метод для установки типа Workflow в info  
[TryDeserializeFrom](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_TryDeserializeFrom.htm)|
Метод для десирализации карточки процесса напрямую из Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
[TryGetTiles](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_TryGetTiles.htm)|
Метод для получения тайлов из info  
## __Поля
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)|
Ключ, по которому устанавливается сериализованный с помощью
[IWorkflowEngineProcessSerializer](T_Tessa_Workflow_IWorkflowEngineProcessSerializer.htm)
объект с данными и подписью.  
---|---  
## __См. также
#### Ссылки
[Tessa.Workflow.Helpful - пространство имён](N_Tessa_Workflow_Helpful.htm)
