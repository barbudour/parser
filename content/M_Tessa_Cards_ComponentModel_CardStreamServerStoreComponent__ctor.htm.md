# CardStreamServerStoreComponent - конструктор
Создаёт новый экземпляр класса с указанием стратегии, требуемой для потокового
сохранения карточки с контентом файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamServerStoreComponent(
    	ICardStreamStoreStrategy streamStoreStrategy,
    	IOperationRepository operationRepository,
    	IDbScope dbScope
    )
VB __Копировать
     Public Sub New ( 
    	streamStoreStrategy As ICardStreamStoreStrategy,
    	operationRepository As IOperationRepository,
    	dbScope As IDbScope
    )
C++ __Копировать
     public:
    CardStreamServerStoreComponent(
    	ICardStreamStoreStrategy^ streamStoreStrategy, 
    	IOperationRepository^ operationRepository, 
    	IDbScope^ dbScope
    )
F# __Копировать
     new : 
            streamStoreStrategy : ICardStreamStoreStrategy * 
            operationRepository : IOperationRepository * 
            dbScope : IDbScope -> CardStreamServerStoreComponent
#### Параметры
streamStoreStrategy
[ICardStreamStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStreamStoreStrategy.htm)
    Стратегия потокового сохранения карточки с контентом файлов.
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
    Репозиторий, управляющий операциями.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
##  __См. также
#### Ссылки
[CardStreamServerStoreComponent -
](T_Tessa_Cards_ComponentModel_CardStreamServerStoreComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
