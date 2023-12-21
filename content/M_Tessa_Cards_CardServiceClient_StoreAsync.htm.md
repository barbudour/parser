# CardServiceClient.StoreAsync(Stream, CancellationToken) - метод
Сохраняет карточку и её файлы, переданные в потоке карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreResponse> StoreAsync(
    	Stream cardStream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	cardStream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual Task<CardStoreResponse^>^ StoreAsync(
    	Stream^ cardStream, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            cardStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
    override StoreAsync : 
            cardStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
cardStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
     Поток карточки, который содержит заголовок [Tessa.Cards.ComponentModel.CardHeader], запрос на сохранение данных карточки [Tessa.Cards.CardStoreRequest], а затем бинарные данные карточки в порядке, указанном в заголовке. Информация может быть записана в поток карточки посредством класса [Tessa.Cards.ComponentModel.CardWriter] и прочитана посредством класса [Tessa.Cards.ComponentModel.CardReader]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Ответ на запрос, содержащий информацию о валидации процесса сохранения
карточки и её файлов, включая сообщения об ошибках.
#### Реализации
[ICardService.StoreAsync(Stream,
CancellationToken)](M_Tessa_Cards_ICardService_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardServiceClient - ](T_Tessa_Cards_CardServiceClient.htm)
[StoreAsync -
перегрузка](Overload_Tessa_Cards_CardServiceClient_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
