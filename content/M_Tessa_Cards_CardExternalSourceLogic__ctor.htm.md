# CardExternalSourceLogic - конструктор
Инициализирует новый экземпляр класса
[CardExternalSourceLogic](T_Tessa_Cards_CardExternalSourceLogic.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardExternalSourceLogic(
    	IStorageSerializer storageSerializer,
    	ICardStreamClientRepository cardStreamClientRepository,
    	[OptionalDependencyAttribute("Files")] ISignatureProvider fileSignatureProvider = null
    )
VB __Копировать
     Public Sub New ( 
    	storageSerializer As IStorageSerializer,
    	cardStreamClientRepository As ICardStreamClientRepository,
    	<OptionalDependencyAttribute("Files")> Optional fileSignatureProvider As ISignatureProvider = Nothing
    )
C++ __Копировать
     public:
    CardExternalSourceLogic(
    	IStorageSerializer^ storageSerializer, 
    	ICardStreamClientRepository^ cardStreamClientRepository, 
    	[OptionalDependencyAttribute(L"Files")] ISignatureProvider^ fileSignatureProvider = nullptr
    )
F# __Копировать
     new : 
            storageSerializer : IStorageSerializer * 
            cardStreamClientRepository : ICardStreamClientRepository * 
            [<OptionalDependencyAttribute("Files")>] ?fileSignatureProvider : ISignatureProvider 
    (* Defaults:
            let _fileSignatureProvider = defaultArg fileSignatureProvider null
    *)
    -> CardExternalSourceLogic
#### Параметры
storageSerializer
[IStorageSerializer](T_Tessa_Platform_Storage_IStorageSerializer.htm)
     Объект, предоставляющий методы для сериализации и десериализации карточек с учетом контента, выгружаемого во внешние файлы. 
cardStreamClientRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
     Потоковый репозиторий карточек на клиенте, используемый для выполнения операций с карточками. 
fileSignatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm) (Optional)
     Объект, предоставляющий криптографические средства для вычисления хеш-суммы содержимого файла, или null, если хеш сумма будет вычислена стандартными средствами [Files](P_Tessa_Platform_HashSignatureProvider_Files.htm). Объект должен поддерживать [IHashSignatureProvider](T_Tessa_Platform_IHashSignatureProvider.htm). 
## __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
