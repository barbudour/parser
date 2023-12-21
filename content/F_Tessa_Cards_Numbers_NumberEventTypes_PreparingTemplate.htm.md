# NumberEventTypes.PreparingTemplate - поле
Карточка шаблона подготавливается к созданию. При этом может потребоваться
очистить поля номеров, заданных в шаблоне.. Обычно выполняется на сервере на
этапе AfterRequest после создания карточки методом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm), но перед
событием
[CreatingCard](F_Tessa_Cards_Numbers_NumberEventTypes_CreatingCard.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType PreparingTemplate
VB __Копировать
     Public Shared ReadOnly PreparingTemplate As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ PreparingTemplate
F# __Копировать
     static val PreparingTemplate: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
