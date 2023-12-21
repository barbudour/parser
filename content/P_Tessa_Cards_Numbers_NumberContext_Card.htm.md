# NumberContext.Card - свойство
Карточка, для которой производится работа с номером.
В методе [Tessa.Cards.Numbers.INumberDirectorBase.IsAvailableAsync] для
события [Tessa.Cards.Numbers.NumberEventTypes.DeletingCardWithoutBackup] может
отсутствовать любая информация по карточке для оптимизации загрузки секций
удаляемой карточки. Поэтому в этом случае, если в карточке нет секций,
рекомендуется не выполнять никаких проверок. Метод будет позже вызван ещё раз
для того же действия.
Во всех остальных случаях для того, чтобы гарантировать успешную обработку в
расширениях, в карточке должны присутствовать системная информация и все
секции, но могут отсутствовать файлы и задания.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Card Card { get; }
VB __Копировать
     Public ReadOnly Property Card As Card
    	Get
C++ __Копировать
     public:
    virtual property Card^ Card {
    	Card^ get () sealed;
    }
F# __Копировать
     abstract Card : Card with get
    override Card : Card with get
#### Значение свойства
[Card](T_Tessa_Cards_Card.htm)
#### Реализации
[INumberContext.Card](P_Tessa_Cards_Numbers_INumberContext_Card.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
