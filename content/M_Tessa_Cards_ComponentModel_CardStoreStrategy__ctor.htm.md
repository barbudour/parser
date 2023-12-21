# CardStoreStrategy - конструктор
Создаёт экземпляр класса с указанием стратегии, требуемой для сохранения
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreStrategy(
    	ICardStoreExecutionStrategy executionStrategy
    )
VB __Копировать
     Public Sub New ( 
    	executionStrategy As ICardStoreExecutionStrategy
    )
C++ __Копировать
     public:
    CardStoreStrategy(
    	ICardStoreExecutionStrategy^ executionStrategy
    )
F# __Копировать
     new : 
            executionStrategy : ICardStoreExecutionStrategy -> CardStoreStrategy
#### Параметры
executionStrategy
[ICardStoreExecutionStrategy](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
     Стратегия выполнения запросов на сохранение элементов карточки. 
## __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
