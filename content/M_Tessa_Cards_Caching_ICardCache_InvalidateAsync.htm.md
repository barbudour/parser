# ICardCache.InvalidateAsync - метод
Сбрасывает локальный кэш.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InvalidateAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InvalidateAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InvalidateAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InvalidateAsync : 
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
[ICardCache - ](T_Tessa_Cards_Caching_ICardCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
