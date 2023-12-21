# WorkflowHelper.CombinePerformers - метод
Формирует единый список исполнителей, составленный из исполнителей указанных в
настройках действия и вычисляемых исполнителей.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<RoleEntryStorage> CombinePerformers(
    	IEnumerable<RoleEntryStorage> performers,
    	IReadOnlyCollection<RoleEntryStorage> sqlPerformers,
    	Guid sqlPerformerRoleID
    )
VB __Копировать
     Public Shared Function CombinePerformers ( 
    	performers As IEnumerable(Of RoleEntryStorage),
    	sqlPerformers As IReadOnlyCollection(Of RoleEntryStorage),
    	sqlPerformerRoleID As Guid
    ) As List(Of RoleEntryStorage)
C++ __Копировать
     public:
    static List<RoleEntryStorage^>^ CombinePerformers(
    	IEnumerable<RoleEntryStorage^>^ performers, 
    	IReadOnlyCollection<RoleEntryStorage^>^ sqlPerformers, 
    	Guid sqlPerformerRoleID
    )
F# __Копировать
     static member CombinePerformers : 
            performers : IEnumerable<RoleEntryStorage> * 
            sqlPerformers : IReadOnlyCollection<RoleEntryStorage> * 
            sqlPerformerRoleID : Guid -> List<RoleEntryStorage> 
#### Параметры
performers
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RoleEntryStorage](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_RoleEntryStorage.htm)>
    Коллекция исполнителей указанных в настройках действия. Список должен быть отсортирован в соответствии с порядком следования элементов.
sqlPerformers
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[RoleEntryStorage](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_RoleEntryStorage.htm)>
    Коллекция вычисляемых исполнителей.
sqlPerformerRoleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор роли на место которой будет подставлен список с вычисляемыми исполнителями.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[RoleEntryStorage](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_RoleEntryStorage.htm)>  
Единый список исполнителей.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
