# NumberEventTypes.DeletingBackupCard - поле
Карточка окончательно удаляется, т.е. удаляется её удалённая карточка
[DeletedTypeName](F_Tessa_Cards_CardHelper_DeletedTypeName.htm). При этом
может потребоваться освободить занятый номер. Обычно выполняется на сервере на
этапе BeforeCommitTransaction при удалении удалённой карточки методом
[DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly NumberEventType DeletingBackupCard
VB __Копировать
     Public Shared ReadOnly DeletingBackupCard As NumberEventType
C++ __Копировать
     public:
    static initonly NumberEventType^ DeletingBackupCard
F# __Копировать
     static val DeletingBackupCard: NumberEventType
#### Значение поля
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
##  __См. также
#### Ссылки
[NumberEventTypes - ](T_Tessa_Cards_Numbers_NumberEventTypes.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
