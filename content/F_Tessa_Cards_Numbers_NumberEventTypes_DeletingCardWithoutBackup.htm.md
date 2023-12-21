# NumberEventTypes.DeletingCardWithoutBackup - поле
Карточка удаляется без возможности восстановления. При этом может
потребоваться освободить занятый номер. Обычно выполняется на сервере на этапе
BeforeCommitTransaction при удалении карточки без возможности восстановления
методом [DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType DeletingCardWithoutBackup
VB __Копировать
     Public Shared ReadOnly DeletingCardWithoutBackup As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ DeletingCardWithoutBackup
F# __Копировать
     static val DeletingCardWithoutBackup: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
