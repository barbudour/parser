# ICardCacheCollection<T>.TryAddAsync - метод
Добавляет значение в кэш по заданному ключу, если значение отсутствовало в
кэше. Возвращает признак того, что значение было успешно добавлено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> TryAddAsync(
    	string key,
    	T value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryAddAsync ( 
    	key As String,
    	value As T,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> TryAddAsync(
    	String^ key, 
    	T value, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryAddAsync : 
            key : string * 
            value : 'T * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому добавляется значение в кэше.
value [T](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)
     Добавляемое значение. Не может быть равно null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если значение было успешно добавлено; false, если значение уже
существовало и поэтому не было добавлено.
## __См. также
#### Ссылки
[ICardCacheCollection<T> \-
](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
