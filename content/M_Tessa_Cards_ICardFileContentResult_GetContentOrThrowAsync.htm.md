# ICardFileContentResult.GetContentOrThrowAsync - метод
Возвращает поток с данными контента. Выбрасывает исключение, если данные
отсутствуют.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<Stream> GetContentOrThrowAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetContentOrThrowAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     ValueTask<Stream^> GetContentOrThrowAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetContentOrThrowAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток с данными контента.
##  __См. также
#### Ссылки
[ICardFileContentResult - ](T_Tessa_Cards_ICardFileContentResult.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
