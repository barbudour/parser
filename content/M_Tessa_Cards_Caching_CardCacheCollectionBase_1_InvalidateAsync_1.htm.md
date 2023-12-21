# CardCacheCollectionBase<T>.InvalidateAsync(CancellationToken) - метод
Очищает кэш, при этом удаляются все значения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InvalidateAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InvalidateAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvalidateAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardCacheCollectionBase<T> \-
](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)
[InvalidateAsync -
перегрузка](Overload_Tessa_Cards_Caching_CardCacheCollectionBase_1_InvalidateAsync.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
