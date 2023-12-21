# WfHelper.TryCreateResolutionPerformerRoleAsync - метод
Создаёт временную роль для исполнителей резолюции, объединяющую список ролей,
включая контекстные роли. Возвращает null, если создаваемая роль не содержит
пользователей. Метод имеет смысл использовать только в том случае, если
указано более одной роли исполнителей. Созданную роль необходимо сохранить
средствами [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm), прежде чем
использовать.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<(bool result, TaskRole taskRole)> TryCreateResolutionPerformerRoleAsync(
    	Guid cardID,
    	ICollection<Tuple<Guid, string>> performerRoles,
    	IRoleRepository roleRepository,
    	IDbScope dbScope,
    	IValidationResultBuilder validationResult,
    	string taskRoleName = "$WfResolution_TaskPerformersRole",
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryCreateResolutionPerformerRoleAsync ( 
    	cardID As Guid,
    	performerRoles As ICollection(Of Tuple(Of Guid, String)),
    	roleRepository As IRoleRepository,
    	dbScope As IDbScope,
    	validationResult As IValidationResultBuilder,
    	Optional taskRoleName As String = "$WfResolution_TaskPerformersRole",
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (result As Boolean, taskRole As TaskRole))
C++ __Копировать
     public:
    static ValueTask<ValueTuple<bool, TaskRole^>> TryCreateResolutionPerformerRoleAsync(
    	Guid cardID, 
    	ICollection<Tuple<Guid, String^>^>^ performerRoles, 
    	IRoleRepository^ roleRepository, 
    	IDbScope^ dbScope, 
    	IValidationResultBuilder^ validationResult, 
    	String^ taskRoleName = L"$WfResolution_TaskPerformersRole", 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryCreateResolutionPerformerRoleAsync : 
            cardID : Guid * 
            performerRoles : ICollection<Tuple<Guid, string>> * 
            roleRepository : IRoleRepository * 
            dbScope : IDbScope * 
            validationResult : IValidationResultBuilder * 
            ?taskRoleName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _taskRoleName = defaultArg taskRoleName "$WfResolution_TaskPerformersRole"
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, TaskRole>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки, для которой выполняется расчёт. Используется для определения состава контекстных и неконтекстных ролей. 
performerRoles
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Tuple](https://learn.microsoft.com/dotnet/api/system.tuple-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>
     Список ролей исполнителей в виде кортежей с идентификатором роли и именем роли. 
roleRepository [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm)
     Репозиторий для управления ролями. Используется для расчёта состава контекстных и неконтекстных ролей. 
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, посредством которого выполняются запросы к базе данных.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
taskRoleName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя созданной роли для исполнителей резолюции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[TaskRole](T_Tessa_Roles_TaskRole.htm)>>  
true, если в результат валидации validationResult не было добавлено ошибок;
false в противном случае.
## __Заметки
Метод не используется транзакции для расчёта контекстных ролей, т.к. сам будет
использоваться в транзакции на сохранение карточки с Workflow.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
