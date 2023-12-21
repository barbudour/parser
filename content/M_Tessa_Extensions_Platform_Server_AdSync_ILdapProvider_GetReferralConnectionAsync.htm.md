# ILdapProvider.GetReferralConnectionAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<LdapUrl> GetReferralConnectionAsync(
    	ILdapContext context,
    	AdConnection conn,
    	string distinguishedName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetReferralConnectionAsync ( 
    	context As ILdapContext,
    	conn As AdConnection,
    	distinguishedName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of LdapUrl)
C++ __Копировать
     ValueTask<LdapUrl^> GetReferralConnectionAsync(
    	ILdapContext^ context, 
    	AdConnection^ conn, 
    	String^ distinguishedName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetReferralConnectionAsync : 
            context : ILdapContext * 
            conn : AdConnection * 
            distinguishedName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<LdapUrl> 
#### Параметры
context
[ILdapContext](T_Tessa_Extensions_Platform_Server_AdSync_ILdapContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
distinguishedName
[String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<LdapUrl>
##  __См. также
#### Ссылки
[ILdapProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
