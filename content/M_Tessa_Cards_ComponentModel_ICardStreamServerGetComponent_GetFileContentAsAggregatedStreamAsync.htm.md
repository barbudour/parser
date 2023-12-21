# ICardStreamServerGetComponent.GetFileContentAsAggregatedStreamAsync - метод
Получает контент версии файла в виде агрегированного потока, в котором
содержится ответ на запрос и собственно контент.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<Stream> GetFileContentAsAggregatedStreamAsync(
    	CardGetFileContentRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetFileContentAsAggregatedStreamAsync ( 
    	request As CardGetFileContentRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
    Task<Stream^>^ GetFileContentAsAggregatedStreamAsync(
    	CardGetFileContentRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFileContentAsAggregatedStreamAsync : 
            request : CardGetFileContentRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
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
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток, содержащий ответ на запрос по получению контента версии файла, а также
собственно контент.
##  __См. также
#### Ссылки
[ICardStreamServerGetComponent -
](T_Tessa_Cards_ComponentModel_ICardStreamServerGetComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
