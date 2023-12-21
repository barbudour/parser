# ILdapUnitProvider.GetAdSyncDistinguishedNameAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<string> GetAdSyncDistinguishedNameAsync(
    	Guid adSyncID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAdSyncDistinguishedNameAsync ( 
    	adSyncID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
    Task<String^>^ GetAdSyncDistinguishedNameAsync(
    	Guid adSyncID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAdSyncDistinguishedNameAsync : 
            adSyncID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
adSyncID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
