# ICardFileContentProvider.GetContentAsync - метод
Возвращает контент файла. Возвращаемое значение не равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<Stream> GetContentAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetContentAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     ValueTask<Stream^> GetContentAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetContentAsync : 
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
Контент файла. Возвращаемое значение не равно null.
## __См. также
#### Ссылки
[ICardFileContentProvider - ](T_Tessa_Cards_ICardFileContentProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
