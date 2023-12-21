# ILdapProvider.GetConnectionAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<AdConnection> GetConnectionAsync(
    	ILdapContext context,
    	string host,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetConnectionAsync ( 
    	context As ILdapContext,
    	host As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of AdConnection)
C++ __Копировать
     ValueTask<AdConnection^> GetConnectionAsync(
    	ILdapContext^ context, 
    	String^ host, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetConnectionAsync : 
            context : ILdapContext * 
            host : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<AdConnection> 
#### Параметры
context
[ILdapContext](T_Tessa_Extensions_Platform_Server_AdSync_ILdapContext.htm)
host [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)>
##  __См. также
#### Ссылки
[ILdapProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
