# CardLockingStrategy.LockedByWriterCode - поле
Результат выполнения хранимой процедуры ObtainWriterLock или ObtainReaderLock
в случае, если writer не дождался снятия блокировки другим writer'ом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected const int LockedByWriterCode = 1
VB __Копировать
     Protected Const LockedByWriterCode As Integer = 1
C++ __Копировать
     protected:
    literal int LockedByWriterCode = 1
F# __Копировать
     static val mutable LockedByWriterCode: int
#### Значение поля
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
