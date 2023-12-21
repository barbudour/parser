# CardHelper.StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamServerRepository, CancellationToken) - метод
Выполняет сохранение карточки на сервере с возможным наличием файлов. Не
выполняет проверку на наличие изменений в контенте файлов методом
[EnsureAllContentModifiedAsync(IEnumerable<IFile>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureAllContentModifiedAsync.htm).
Метод для внутреннего использования, рекомендуется использовать объект
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
    	ICardStreamServerRepository cardStreamServerRepository,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function StoreAsync ( 
    	request As CardStoreRequest,
    	fileContainer As IFileContainer,
    	cardRepository As ICardRepository,
    	cardStreamServerRepository As ICardStreamServerRepository,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As CardStoreOperationToken
C++ __Копировать
     public:
    static CardStoreOperationToken^ StoreAsync(
    	CardStoreRequest^ request, 
    	IFileContainer^ fileContainer, 
    	ICardRepository^ cardRepository, 
    	ICardStreamServerRepository^ cardStreamServerRepository, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member StoreAsync : 
            request : CardStoreRequest * 
            fileContainer : IFileContainer * 
            cardRepository : ICardRepository * 
            cardStreamServerRepository : ICardStreamServerRepository * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
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
cardStreamServerRepository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
    Репозиторий для потокового управления карточками на сервере.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[CardStoreOperationToken](T_Tessa_Cards_CardStoreOperationToken.htm)  
Ответ на запрос на сохранение карточки.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметры request, fileContainer, cardRepository или
cardStreamServerRepository равны null.  
---|---  
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[StoreAsync - перегрузка](Overload_Tessa_Cards_CardHelper_StoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
