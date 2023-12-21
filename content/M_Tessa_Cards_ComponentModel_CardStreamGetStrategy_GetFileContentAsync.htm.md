# CardStreamGetStrategy.GetFileContentAsync - метод
Получает контент версии файла. Возвращает ответ на запрос по получению
контента версии файла. Вторым параметром возвращает функцию, открывающую поток
на чтение контента файла, или null, если при получении информации о файле
возникла ошибка, причём отличное от null значение возвращается только в случае
отсутствия ошибок.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(CardGetFileContentResponse response, Func<CancellationToken, ValueTask<Stream>> getContentFuncAsync)> GetFileContentAsync(
    	CardGetFileContentRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileContentAsync ( 
    	request As CardGetFileContentRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (response As CardGetFileContentResponse, getContentFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream))))
C++ __Копировать
     public:
    virtual Task<ValueTuple<CardGetFileContentResponse^, Func<CancellationToken, ValueTask<Stream^>>^>>^ GetFileContentAsync(
    	CardGetFileContentRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardGetFileContentResponse, Func<CancellationToken, ValueTask<Stream>>>> 
    override GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardGetFileContentResponse, Func<CancellationToken, ValueTask<Stream>>>> 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на получение контента версии файла.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего сохранение карточки с контентом файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm),
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>>  
Ответ на запрос по получению контента версии файла.
#### Реализации
[ICardStreamGetStrategy.GetFileContentAsync(CardGetFileContentRequest,
ICardMetadata, ISession,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStreamGetStrategy_GetFileContentAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamGetStrategy -
](T_Tessa_Cards_ComponentModel_CardStreamGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
