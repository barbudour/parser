# CardStreamClientRepository.StoreAsync - метод
Сохраняет карточку с контентом файлов, которые упаковываются в поток карточки
перед отправкой на сервер.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardStoreAsyncResponse StoreAsync(
    	CardStoreRequest request,
    	CardHeader header,
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> fileStreams,
    	long totalFileLength,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	request As CardStoreRequest,
    	header As CardHeader,
    	fileStreams As IReadOnlyCollection(Of Func(Of CancellationToken, ValueTask(Of Stream))),
    	totalFileLength As Long,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ICardStoreAsyncResponse
C++ __Копировать
     public:
    virtual ICardStoreAsyncResponse^ StoreAsync(
    	CardStoreRequest^ request, 
    	CardHeader^ header, 
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ fileStreams, 
    	long long totalFileLength, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            request : CardStoreRequest * 
            header : CardHeader * 
            fileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> * 
            totalFileLength : int64 * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ICardStoreAsyncResponse 
    override StoreAsync : 
            request : CardStoreRequest * 
            header : CardHeader * 
            fileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> * 
            totalFileLength : int64 * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ICardStoreAsyncResponse 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
header [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)
    Заголовок потока карточки, в котором производится сохранение.
fileStreams
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>
     Коллекция функций, создающих потоки для сохранения каждого из файлов. Функции должны быть упорядочены в соответствии с порядком файлов в заголовке потока header. 
totalFileLength [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Суммарная длина файлов, требуемая для расчёта процента готовности операции. Не может быть отрицательным числом. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ICardStoreAsyncResponse](T_Tessa_Cards_ICardStoreAsyncResponse.htm)  
Ответ на запрос по сохранению карточки.
#### Реализации
[ICardStreamClientRepository.StoreAsync(CardStoreRequest, CardHeader,
IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>>, Int64,
CancellationToken)](M_Tessa_Cards_ICardStreamClientRepository_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardStreamClientRepository - ](T_Tessa_Cards_CardStreamClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
