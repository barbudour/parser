# CardStreamServerGetComponent - конструктор
Создаёт экземпляр класса с указанием стратегий, используемых для потокового
получения контента файлов на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamServerGetComponent(
    	ICardStreamGetStrategy getStrategy
    )
VB __Копировать
     Public Sub New ( 
    	getStrategy As ICardStreamGetStrategy
    )
C++ __Копировать
     public:
    CardStreamServerGetComponent(
    	ICardStreamGetStrategy^ getStrategy
    )
F# __Копировать
     new : 
            getStrategy : ICardStreamGetStrategy -> CardStreamServerGetComponent
#### Параметры
getStrategy
[ICardStreamGetStrategy](T_Tessa_Cards_ComponentModel_ICardStreamGetStrategy.htm)
    Стратегия, используемая для потокового получения контента файлов.
##  __См. также
#### Ссылки
[CardStreamServerGetComponent -
](T_Tessa_Cards_ComponentModel_CardStreamServerGetComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
