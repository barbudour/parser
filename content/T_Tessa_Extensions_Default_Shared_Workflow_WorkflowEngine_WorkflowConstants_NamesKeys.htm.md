# WorkflowConstants.NamesKeys - класс
Предоставляет названия ключей по которым содержатся значения хранящиеся в
параметрах объектов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NamesKeys
VB __Копировать
     Public NotInheritable Class NamesKeys
C++ __Копировать
     public ref class NamesKeys abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NamesKeys = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowConstants.NamesKeys
##  __Поля
[CanEditAnyFiles](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CanEditAnyFiles.htm)|
Имя ключа, по которому в [Settings](P_Tessa_Cards_CardTask_Settings.htm)
содержится значение флага дающего права на редактирование карточки договора
исполнителями. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false.  
---|---  
[CanEditCard](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CanEditCard.htm)|
Имя ключа, по которому в [Settings](P_Tessa_Cards_CardTask_Settings.htm)
содержится значение флага дающего права на редактирование приложенных файлов
исполнителями. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false.  
[CompletedTaskRowID](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CompletedTaskRowID.htm)|
Имя ключа, по которому в
[Hash](P_Tessa_Workflow_Signals_IWorkflowEngineSignal_Hash.htm)[WorkflowEngineTaskSignal](T_Tessa_Workflow_Signals_WorkflowEngineTaskSignal.htm)
содержится идентификатор завершаемого задания, отправленного в процессе типа
[ResolutionProcessName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionProcessName.htm).
Тип значения: [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[CurrentPerformerIndex](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_CurrentPerformerIndex.htm)|
Имя ключа, по которому в
[ActionInstance](P_Tessa_Workflow_IWorkflowEngineContext_ActionInstance.htm)
хранится порядковый номер текущего исполнителя. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[EditInterjectAuthorID](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_EditInterjectAuthorID.htm)|
Имя ключа, по которому в
[ActionInstance](P_Tessa_Workflow_IWorkflowEngineContext_ActionInstance.htm)
хранится идентификатор автора задания используемый, если не задано иное, в
качестве автора задания доработки автором
([KrEditInterjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrEditInterjectTypeID.htm)).
Тип значения: [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[IsDisableAutoApproval](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_IsDisableAutoApproval.htm)|
Имя ключа, по которому в [Settings](P_Tessa_Cards_CardTask_Settings.htm)
содержится значение флага отключающего автоматическое согласование задания.
Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false.  
[IsNegativeActionResult](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_IsNegativeActionResult.htm)|
Имя ключа, по которому в
[ActionInstance](P_Tessa_Workflow_IWorkflowEngineContext_ActionInstance.htm)
хранится флаг, показывающий, будет ли результат обработки действия
отрицательным. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[ProcessCycle](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_ProcessCycle.htm)|
Имя ключа, по которому в
[Hash](P_Tessa_Workflow_Storage_WorkflowStorageBase_Hash.htm)[ProcessInstance](P_Tessa_Workflow_IWorkflowEngineContext_ProcessInstance.htm)
содержится номер цикла согласования. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[RoleList](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_NamesKeys_RoleList.htm)|
Имя ключа, по которому в
[ActionInstance](P_Tessa_Workflow_IWorkflowEngineContext_ActionInstance.htm)
хранится полный список исполнителей. Тип значения: список
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1),
где T - словарь [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)
представляющий соответствующий объект
[RoleEntryStorage](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_RoleEntryStorage.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
