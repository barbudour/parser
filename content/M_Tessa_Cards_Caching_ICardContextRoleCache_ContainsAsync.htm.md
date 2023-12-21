# ICardContextRoleCache.ContainsAsync - метод
Возвращает признак того, что контекстная роль с заданным идентификатором
присутствует в кэше.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> ContainsAsync(
    	Guid roleID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ContainsAsync ( 
    	roleID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> ContainsAsync(
    	Guid roleID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ContainsAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор контекстной роли, наличие которой требуется проверить в кэше.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если контекстная роль с заданным идентификатором присутствует в кэше;
false в противном случае.
## __См. также
#### Ссылки
[ICardContextRoleCache - ](T_Tessa_Cards_Caching_ICardContextRoleCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
