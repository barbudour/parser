# CardStreamClientStoreComponent - конструктор
Создаёт экземпляр класса с указанием потокового сервиса карточек, требуемого
для сохранения карточки с контентом файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamClientStoreComponent(
    	ICardService cardService,
    	IOperationRepository operationRepository,
    	[OptionalDependencyAttribute] IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	cardService As ICardService,
    	operationRepository As IOperationRepository,
    	<OptionalDependencyAttribute> Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    CardStreamClientStoreComponent(
    	ICardService^ cardService, 
    	IOperationRepository^ operationRepository, 
    	[OptionalDependencyAttribute] IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            cardService : ICardService * 
            operationRepository : IOperationRepository * 
            [<OptionalDependencyAttribute>] ?dbScope : IDbScope 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
    *)
    -> CardStreamClientStoreComponent
#### Параметры
cardService [ICardService](T_Tessa_Cards_ICardService.htm)
    Потоковый сервис карточек.
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
    Репозиторий, управляющий операциями.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект, обеспечивающий соединение с базой данных, или null, если выполнение происходит на клиенте. 
## __См. также
#### Ссылки
[CardStreamClientStoreComponent -
](T_Tessa_Cards_ComponentModel_CardStreamClientStoreComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
