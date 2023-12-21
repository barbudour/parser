# NumberEventTypes.CreatingCard - поле
Создаётся карточка (обычным способом или по шаблону). При этом может
потребоваться зарезервировать номер. Обычно выполняется на сервере на этапе
AfterRequest после создания карточки методом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType CreatingCard
VB __Копировать
     Public Shared ReadOnly CreatingCard As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ CreatingCard
F# __Копировать
     static val CreatingCard: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
