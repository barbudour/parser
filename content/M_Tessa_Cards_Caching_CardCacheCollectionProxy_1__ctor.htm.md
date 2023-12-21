# CardCacheCollectionProxy<T> \- конструктор
Создаёт экземпляр класса с указанием декорируемого объекта и методов,
выполняемых при очистке кэша вызовом методов интерфейса
[ICardCacheCollection<T>](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCacheCollectionProxy(
    	Func<CancellationToken, ValueTask<ICardCacheCollection<T>>> getSourceAsync,
    	Func<CancellationToken, Task> invalidatedActionAsync = null,
    	Func<string, CancellationToken, Task> invalidatedByKeyActionAsync = null
    )
VB __Копировать
     Public Sub New ( 
    	getSourceAsync As Func(Of CancellationToken, ValueTask(Of ICardCacheCollection(Of T))),
    	Optional invalidatedActionAsync As Func(Of CancellationToken, Task) = Nothing,
    	Optional invalidatedByKeyActionAsync As Func(Of String, CancellationToken, Task) = Nothing
    )
C++ __Копировать
     public:
    CardCacheCollectionProxy(
    	Func<CancellationToken, ValueTask<ICardCacheCollection<T>^>>^ getSourceAsync, 
    	Func<CancellationToken, Task^>^ invalidatedActionAsync = nullptr, 
    	Func<String^, CancellationToken, Task^>^ invalidatedByKeyActionAsync = nullptr
    )
F# __Копировать
     new : 
            getSourceAsync : Func<CancellationToken, ValueTask<ICardCacheCollection<'T>>> * 
            ?invalidatedActionAsync : Func<CancellationToken, Task> * 
            ?invalidatedByKeyActionAsync : Func<string, CancellationToken, Task> 
    (* Defaults:
            let _invalidatedActionAsync = defaultArg invalidatedActionAsync null
            let _invalidatedByKeyActionAsync = defaultArg invalidatedByKeyActionAsync null
    *)
    -> CardCacheCollectionProxy
#### Параметры
getSourceAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardCacheCollection](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)<[T](T_Tessa_Cards_Caching_CardCacheCollectionProxy_1.htm)>>>
    Функция, асинхронно возвращающая декорируемый объект, для которого создаётся прокси.
invalidatedActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, выполняемый при сбросе кэша для всех ключей или null, если не требуется выполнять дополнительных действий при сбросе кэша для всех ключей. 
invalidatedByKeyActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, выполняемый при сбросе кэша для заданного в параметре ключа или null, если не требуется выполнять дополнительных действий при сбросе кэша для ключа. 
## __См. также
#### Ссылки
[CardCacheCollectionProxy<T> \-
](T_Tessa_Cards_Caching_CardCacheCollectionProxy_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
