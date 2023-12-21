# ILdapProvider.FindAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<List<AdEntry>> FindAsync(
    	ILdapContext context,
    	AdConnection conn,
    	string distinguishedName,
    	string ldapSearchFilter = null,
    	int searchScope = 0,
    	bool skipReferral = false,
    	List<string> connList = null,
    	string[] attributeList = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function FindAsync ( 
    	context As ILdapContext,
    	conn As AdConnection,
    	distinguishedName As String,
    	Optional ldapSearchFilter As String = Nothing,
    	Optional searchScope As Integer = 0,
    	Optional skipReferral As Boolean = false,
    	Optional connList As List(Of String) = Nothing,
    	Optional attributeList As String() = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of AdEntry))
C++ __Копировать
    ValueTask<List<AdEntry^>^> FindAsync(
    	ILdapContext^ context, 
    	AdConnection^ conn, 
    	String^ distinguishedName, 
    	String^ ldapSearchFilter = nullptr, 
    	int searchScope = 0, 
    	bool skipReferral = false, 
    	List<String^>^ connList = nullptr, 
    	array<String^>^ attributeList = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract FindAsync : 
            context : ILdapContext * 
            conn : AdConnection * 
            distinguishedName : string * 
            ?ldapSearchFilter : string * 
            ?searchScope : int * 
            ?skipReferral : bool * 
            ?connList : List<string> * 
            ?attributeList : string[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _ldapSearchFilter = defaultArg ldapSearchFilter null
            let _searchScope = defaultArg searchScope 0
            let _skipReferral = defaultArg skipReferral false
            let _connList = defaultArg connList null
            let _attributeList = defaultArg attributeList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<AdEntry>> 
#### Параметры
context
[ILdapContext](T_Tessa_Extensions_Platform_Server_AdSync_ILdapContext.htm)
conn
[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)
distinguishedName
[String](https://learn.microsoft.com/dotnet/api/system.string)
ldapSearchFilter
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
searchScope [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
skipReferral [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
connList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
attributeList [String](https://learn.microsoft.com/dotnet/api/system.string)[]
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[AdEntry](T_Tessa_Extensions_Platform_Server_AdSync_AdEntry.htm)>>
##  __См. также
#### Ссылки
[ILdapProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
