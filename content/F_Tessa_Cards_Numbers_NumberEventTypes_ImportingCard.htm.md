# NumberEventTypes.ImportingCard - поле
Карточка импортируется. При этом может потребоваться занять номер, который был
ранее занят. Обычно выполняется на сервере на этапе BeforeCommitTransaction в
транзакции на сохранение карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType ImportingCard
VB __Копировать
     Public Shared ReadOnly ImportingCard As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ ImportingCard
F# __Копировать
     static val ImportingCard: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
