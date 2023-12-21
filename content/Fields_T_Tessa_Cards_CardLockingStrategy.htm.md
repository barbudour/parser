# CardLockingStrategy - поля
##  __Поля
[CardNotFoundWhileWritingCode](F_Tessa_Cards_CardLockingStrategy_CardNotFoundWhileWritingCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если
карточка не существует.  
---|---  
[LockedByReadersCode](F_Tessa_Cards_CardLockingStrategy_LockedByReadersCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
не дождался окончания чтения другими reader'ами.  
[LockedByWriterCode](F_Tessa_Cards_CardLockingStrategy_LockedByWriterCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock или ObtainReaderLock
в случае, если writer не дождался снятия блокировки другим writer'ом.  
[LockedWithChangedVersion](F_Tessa_Cards_CardLockingStrategy_LockedWithChangedVersion.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
не дождался снятия блокировки другим writer'ом. ///  
[LockObtained](F_Tessa_Cards_CardLockingStrategy_LockObtained.htm)|  Результат
выполнения хранимой процедуры ObtainWriterLock или ObtainReaderLock в случае,
если блокировка успешно получена.  
[LockTimeoutWhileObtainingWriterLockCode](F_Tessa_Cards_CardLockingStrategy_LockTimeoutWhileObtainingWriterLockCode.htm)|
Результат выполнения хранимой процедуры ObtainWriterLock в случае, если writer
натолкнулся на длительную блокировку Instances в процессе выполнения запроса и
не дождался снятия блокировки другим writer'ом.  
## __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
