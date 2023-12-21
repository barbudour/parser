# ICardCachedMetadata.UpdateAsync - метод
Обновляет кэш метаинформации из сервиса типов карточек. Если объект защищён от
изменений посредством метода [Tessa.Platform.ISealable.Seal] и имеет доступ к
объектам метаинформации, переданным через конструктор, то выполняется более
эффективный запрос к серверу для получения актуальной метаинформации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task UpdateAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function UpdateAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ UpdateAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract UpdateAsync : 
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
