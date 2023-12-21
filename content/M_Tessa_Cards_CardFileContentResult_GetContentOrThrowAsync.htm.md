# CardFileContentResult.GetContentOrThrowAsync - метод
Возвращает поток с данными контента. Выбрасывает исключение, если данные
отсутствуют.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<Stream> GetContentOrThrowAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetContentOrThrowAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     public:
    virtual ValueTask<Stream^> GetContentOrThrowAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetContentOrThrowAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
    override GetContentOrThrowAsync : 
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
#### Реализации
[ICardFileContentResult.GetContentOrThrowAsync(CancellationToken)](M_Tessa_Cards_ICardFileContentResult_GetContentOrThrowAsync.htm)  
##  __См. также
#### Ссылки
[CardFileContentResult - ](T_Tessa_Cards_CardFileContentResult.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
