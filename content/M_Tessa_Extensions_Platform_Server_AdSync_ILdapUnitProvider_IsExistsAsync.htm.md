# ILdapUnitProvider.IsExistsAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> IsExistsAsync(
    	Guid objectGuid,
    	RoleType role,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function IsExistsAsync ( 
    	objectGuid As Guid,
    	role As RoleType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ IsExistsAsync(
    	Guid objectGuid, 
    	RoleType role, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract IsExistsAsync : 
            objectGuid : Guid * 
            role : RoleType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
objectGuid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
role [RoleType](T_Tessa_Roles_RoleType.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
