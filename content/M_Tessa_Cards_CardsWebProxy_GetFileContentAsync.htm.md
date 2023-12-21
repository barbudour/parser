# CardsWebProxy.GetFileContentAsync - метод
Получает контент версии файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Stream> GetFileContentAsync(
    	CardGetFileContentRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileContentAsync ( 
    	request As CardGetFileContentRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Stream)
C++ __Копировать
     public:
    Task<Stream^>^ GetFileContentAsync(
    	CardGetFileContentRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetFileContentAsync : 
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
    Объект, посредством которого можно отменить выполнение запроса с клиента на сервер.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток, содержащий ответ на запрос по получению контента версии файла, а также
собственно контент.
##  __См. также
#### Ссылки
[CardsWebProxy - ](T_Tessa_Cards_CardsWebProxy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
