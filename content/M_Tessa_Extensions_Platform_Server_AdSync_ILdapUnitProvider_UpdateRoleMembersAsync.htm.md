# ILdapUnitProvider.UpdateRoleMembersAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task UpdateRoleMembersAsync(
    	Card card,
    	List<Guid> newUsersList,
    	RoleType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function UpdateRoleMembersAsync ( 
    	card As Card,
    	newUsersList As List(Of Guid),
    	type As RoleType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ UpdateRoleMembersAsync(
    	Card^ card, 
    	List<Guid>^ newUsersList, 
    	RoleType type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract UpdateRoleMembersAsync : 
            card : Card * 
            newUsersList : List<Guid> * 
            type : RoleType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
newUsersList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
type [RoleType](T_Tessa_Roles_RoleType.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
