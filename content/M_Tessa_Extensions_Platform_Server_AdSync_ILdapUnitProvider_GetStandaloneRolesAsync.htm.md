# ILdapUnitProvider.GetStandaloneRolesAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<List<Guid>> GetStandaloneRolesAsync(
    	DateTime syncDate,
    	RoleType roleType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetStandaloneRolesAsync ( 
    	syncDate As DateTime,
    	roleType As RoleType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of Guid))
C++ __Копировать
    Task<List<Guid>^>^ GetStandaloneRolesAsync(
    	DateTime syncDate, 
    	RoleType roleType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetStandaloneRolesAsync : 
            syncDate : DateTime * 
            roleType : RoleType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<Guid>> 
#### Параметры
syncDate [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
roleType [RoleType](T_Tessa_Roles_RoleType.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
