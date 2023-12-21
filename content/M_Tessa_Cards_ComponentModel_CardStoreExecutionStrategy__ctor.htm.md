# CardStoreExecutionStrategy - конструктор
Создаёт экземпляр класса с указанием стратегий, требуемых для сохранения
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreExecutionStrategy(
    	ICardStoreDeletionStrategy storeDeletionStrategy,
    	ICardStoreCachingStrategy storeCachingStrategy
    )
VB __Копировать
     Public Sub New ( 
    	storeDeletionStrategy As ICardStoreDeletionStrategy,
    	storeCachingStrategy As ICardStoreCachingStrategy
    )
C++ __Копировать
     public:
    CardStoreExecutionStrategy(
    	ICardStoreDeletionStrategy^ storeDeletionStrategy, 
    	ICardStoreCachingStrategy^ storeCachingStrategy
    )
F# __Копировать
     new : 
            storeDeletionStrategy : ICardStoreDeletionStrategy * 
            storeCachingStrategy : ICardStoreCachingStrategy -> CardStoreExecutionStrategy
#### Параметры
storeDeletionStrategy
[ICardStoreDeletionStrategy](T_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy.htm)
     Стратегия выполнения запросов на удаление элементов карточки при её сохранении или удалении. 
storeCachingStrategy
[ICardStoreCachingStrategy](T_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy.htm)
     Стратегия кэширования объектов для операции по сохранению карточки. 
## __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
