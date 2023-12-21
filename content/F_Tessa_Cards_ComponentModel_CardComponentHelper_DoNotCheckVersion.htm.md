# CardComponentHelper.DoNotCheckVersion - поле
Значение версии, которое передаётся в метод [ExecuteInWriterLockAsync(Guid,
Int32, IValidationResultBuilder, Func<ICardTransactionParameter, Task>,
Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInWriterLockAsync.htm)
для того, чтобы обозначить, что проверка версии не требуется. Это имеет смысл
при удалении карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const int DoNotCheckVersion = -1
VB __Копировать
     Public Const DoNotCheckVersion As Integer = -1
C++ __Копировать
     public:
    literal int DoNotCheckVersion = -1
F# __Копировать
     static val mutable DoNotCheckVersion: int
#### Значение поля
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
