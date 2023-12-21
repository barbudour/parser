# NotificationHelper.GetMobileApprovalEmailAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<string> GetMobileApprovalEmailAsync(
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetMobileApprovalEmailAsync ( 
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    static ValueTask<String^> GetMobileApprovalEmailAsync(
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetMobileApprovalEmailAsync : 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[NotificationHelper -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationHelper.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
