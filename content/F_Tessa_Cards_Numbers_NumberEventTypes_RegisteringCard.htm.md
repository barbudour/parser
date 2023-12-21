# NumberEventTypes.RegisteringCard - поле
Выполняется регистрация карточки. При этом может потребоваться выделить
регистрационный номер. Обычно выполняется на сервере на этапе BeforeRequest
перед сохранением карточки методом [StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType RegisteringCard
VB __Копировать
     Public Shared ReadOnly RegisteringCard As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ RegisteringCard
F# __Копировать
     static val RegisteringCard: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
