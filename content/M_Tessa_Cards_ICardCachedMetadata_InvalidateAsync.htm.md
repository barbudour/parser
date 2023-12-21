# ICardCachedMetadata.InvalidateAsync - метод
Сбрасывает кэш метаинформации. При следующем обращении к содержимому
метаинформации будет выполнен запрос на получение её из сервиса типов
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
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
[ICardCachedMetadata - ](T_Tessa_Cards_ICardCachedMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
