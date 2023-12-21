# ICardCacheCollection<T>.TryGetAlreadyCachedAsync - метод
Возвращает значение из кэша по заданному ключу или null, если значение
отсутствует в кэше. Значение может отсутствовать, если оно ещё не было
загружено, например, если карточка с указанным именем не была загружена из
базы данных или от сервера. Используйте индексатор коллекции, если требуется
загрузить значение, когда оно недоступно, например: await
cardCache.Cards.GetAsync("CardTypeName").
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<T> TryGetAlreadyCachedAsync(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetAlreadyCachedAsync ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     ValueTask<T> TryGetAlreadyCachedAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetAlreadyCachedAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется вернуть значение из кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[T](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)>  
Значение из кэша по заданному ключу или null, если значение отсутствует в
кэше.
## __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[ICardCacheCollection<T> \-
](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
