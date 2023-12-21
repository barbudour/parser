# LdapProvider.GetReferralConnectionAsync - метод
Получает адрес referral сервера
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<LdapUrl> GetReferralConnectionAsync(
    	ILdapContext context,
    	AdConnection conn,
    	string distinguishedName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetReferralConnectionAsync ( 
    	context As ILdapContext,
    	conn As AdConnection,
    	distinguishedName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of LdapUrl)
C++ __Копировать
     public:
    virtual ValueTask<LdapUrl^> GetReferralConnectionAsync(
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
    override GetReferralConnectionAsync : 
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
    Основное соединение
distinguishedName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    DN referral сервера
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<LdapUrl>  
#### Реализации
[ILdapProvider.GetReferralConnectionAsync(ILdapContext, AdConnection, String,
CancellationToken)](M_Tessa_Extensions_Platform_Server_AdSync_ILdapProvider_GetReferralConnectionAsync.htm)  
##  __См. также
#### Ссылки
[LdapProvider - ](T_Tessa_Extensions_Platform_Server_AdSync_LdapProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
