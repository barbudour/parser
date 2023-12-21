# CardStreamServerRepository.GetFileContentAsAggregatedStreamAsync - метод
Получает контент версии файла в виде агрегированного потока, в котором
содержится ответ на запрос и собственно контент.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Stream> GetFileContentAsAggregatedStreamAsync(
    	CardGetFileContentRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileContentAsAggregatedStreamAsync ( 
    	request As CardGetFileContentRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
     public:
    virtual Task<Stream^>^ GetFileContentAsAggregatedStreamAsync(
    	CardGetFileContentRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFileContentAsAggregatedStreamAsync : 
            request : CardGetFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
    override GetFileContentAsAggregatedStreamAsync : 
            request : CardGetFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Stream> 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на получение контента версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток, содержащий ответ на запрос по получению контента версии файла, а также
собственно контент.
#### Реализации
[ICardStreamServerRepository.GetFileContentAsAggregatedStreamAsync(CardGetFileContentRequest,
CancellationToken)](M_Tessa_Cards_ICardStreamServerRepository_GetFileContentAsAggregatedStreamAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamServerRepository - ](T_Tessa_Cards_CardStreamServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
