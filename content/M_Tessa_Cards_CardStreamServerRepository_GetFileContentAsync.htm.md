# CardStreamServerRepository.GetFileContentAsync - метод
Получает контент версии файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ICardFileContentResult> GetFileContentAsync(
    	CardGetFileContentRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileContentAsync ( 
    	request As CardGetFileContentRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardFileContentResult)
C++ __Копировать
     public:
    virtual Task<ICardFileContentResult^>^ GetFileContentAsync(
    	CardGetFileContentRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileContentResult> 
    override GetFileContentAsync : 
            request : CardGetFileContentRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileContentResult> 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на получение контента версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardFileContentResult](T_Tessa_Cards_ICardFileContentResult.htm)>  
Ответ на запрос по получению контента версии файла.
#### Реализации
[ICardStreamServerRepository.GetFileContentAsync(CardGetFileContentRequest,
CancellationToken)](M_Tessa_Cards_ICardStreamServerRepository_GetFileContentAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamServerRepository - ](T_Tessa_Cards_CardStreamServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
