# WorkflowHelper.TryGetPersonalRoleIDAsync - метод
Возвращает персональную роль (пользователя) для роли имеющую указанный
идентификатор.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(bool , Guid? )> TryGetPersonalRoleIDAsync(
    	Guid roleID,
    	Guid cardID,
    	IRoleRepository roleRepository,
    	IValidationResultBuilder validationResult = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetPersonalRoleIDAsync ( 
    	roleID As Guid,
    	cardID As Guid,
    	roleRepository As IRoleRepository,
    	Optional validationResult As IValidationResultBuilder = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ( As Boolean,  As Guid?))
C++ __Копировать
     public:
    static Task<ValueTuple<bool, Nullable<Guid>>>^ TryGetPersonalRoleIDAsync(
    	Guid roleID, 
    	Guid cardID, 
    	IRoleRepository^ roleRepository, 
    	IValidationResultBuilder^ validationResult = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetPersonalRoleIDAsync : 
            roleID : Guid * 
            cardID : Guid * 
            roleRepository : IRoleRepository * 
            ?validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Nullable<Guid>>> 
#### Параметры
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор роли.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой требуется получить состав контекстной роли. Используется, если указанная роль является контекстной.
roleRepository [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm)
    Репозиторий для управления ролевой моделью.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
    Результат валидации. Если указан, то в него будут записываться сообщения об ошибках обработки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>>  
Кортеж содержащий: значение, показывающее, успешно ли завершена обработка и
идентификатор персональной роли или значение по умолчанию для типа, если
указанная роль является контекстной и не содержит участников или указанная
роль имеет тип отличный от [Personal](T_Tessa_Roles_RoleType.htm) или
[Context](T_Tessa_Roles_RoleType.htm). Если роль являющаяся контекстной
возвращает более одного участника, то берётся первый участник.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
