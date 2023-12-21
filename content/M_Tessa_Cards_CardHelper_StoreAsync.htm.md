# CardHelper.StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamClientRepository, Func<Double, CancellationToken, ValueTask>,
Int32, CancellationToken) - метод
Выполняет асинхронное сохранение карточки на клиенте с возможным наличием
файлов. Не выполняет проверку на наличие изменений в контенте файлов. Метод
для внутреннего использования, рекомендуется использовать объект
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) для сохранения карточки
с файлами, обратитесь к руководству разработчика за примерами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardStoreOperationToken StoreAsync(
    	CardStoreRequest request,
    	IFileContainer fileContainer,
    	ICardRepository cardRepository,
    	ICardStreamClientRepository cardStreamClientRepository,
    	Func<double, CancellationToken, ValueTask> updateProgressAsync = null,
    	int updateProgressMillisecondInterval = -1,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function StoreAsync ( 
    	request As CardStoreRequest,
    	fileContainer As IFileContainer,
    	cardRepository As ICardRepository,
    	cardStreamClientRepository As ICardStreamClientRepository,
    	Optional updateProgressAsync As Func(Of Double, CancellationToken, ValueTask) = Nothing,
    	Optional updateProgressMillisecondInterval As Integer = -1,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As CardStoreOperationToken
C++ __Копировать
     public:
    static CardStoreOperationToken^ StoreAsync(
    	CardStoreRequest^ request, 
    	IFileContainer^ fileContainer, 
    	ICardRepository^ cardRepository, 
    	ICardStreamClientRepository^ cardStreamClientRepository, 
    	Func<double, CancellationToken, ValueTask>^ updateProgressAsync = nullptr, 
    	int updateProgressMillisecondInterval = -1, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member StoreAsync : 
            request : CardStoreRequest * 
            fileContainer : IFileContainer * 
            cardRepository : ICardRepository * 
            cardStreamClientRepository : ICardStreamClientRepository * 
            ?updateProgressAsync : Func<float, CancellationToken, ValueTask> * 
            ?updateProgressMillisecondInterval : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _updateProgressAsync = defaultArg updateProgressAsync null
            let _updateProgressMillisecondInterval = defaultArg updateProgressMillisecondInterval -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardStoreOperationToken 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
fileContainer [IFileContainer](T_Tessa_Files_IFileContainer.htm)
     Контейнер с файлами карточки или null, если карточка не может содержать файлов. 
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
cardStreamClientRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
    Репозиторий для потокового управления карточками на клиенте.
updateProgressAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, получающий прогресс сохранения файлов как число от 0 до 1. Метод не вызывается, если карточка сохраняется без файлов. 
updateProgressMillisecondInterval
[Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Интервал в миллисекундах между обновлениями прогресса по сохранению файлов. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[CardStoreOperationToken](T_Tessa_Cards_CardStoreOperationToken.htm)  
Объект, предоставляющий доступ к асинхронной операции по сохранению карточки с
файлами и к её результату.
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметры request, fileContainer, cardRepository, cardStreamClientRepository
или updateProgressAsync равны null.  
---|---  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Параметр updateProgressMillisecondInterval меньше нуля.  
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[StoreAsync - перегрузка](Overload_Tessa_Cards_CardHelper_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
