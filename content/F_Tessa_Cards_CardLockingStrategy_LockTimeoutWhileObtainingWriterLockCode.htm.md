# CardLockingStrategy.LockTimeoutWhileObtainingWriterLockCode - поле
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
натолкнулся на длительную блокировку Instances в процессе выполнения запроса и
не дождался снятия блокировки другим writer'ом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected const int LockTimeoutWhileObtainingWriterLockCode = 4
VB __Копировать
     Protected Const LockTimeoutWhileObtainingWriterLockCode As Integer = 4
C++ __Копировать
     protected:
    literal int LockTimeoutWhileObtainingWriterLockCode = 4
F# __Копировать
     static val mutable LockTimeoutWhileObtainingWriterLockCode: int
#### Значение поля
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
