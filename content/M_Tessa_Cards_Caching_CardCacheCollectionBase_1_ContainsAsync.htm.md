# CardCacheCollectionBase<T>.ContainsAsync - метод
Возвращает признак того, что значение доступно в кэше по заданному ключу.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> ContainsAsync(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ContainsAsync ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> ContainsAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ContainsAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override ContainsAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, для которого требуется проверить наличие значения в кэше.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если значение доступно в кэше по заданному ключу; false в противном
случае.
## __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
## __См. также
#### Ссылки
[CardCacheCollectionBase<T> \-
](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
