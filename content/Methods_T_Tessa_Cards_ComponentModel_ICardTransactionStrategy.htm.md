# ICardTransactionStrategy - методы
##  __Методы
[ExecuteInReaderLockAsync](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInReaderLockAsync.htm)|
Выполняет запрос на чтение карточки внутри блокировки reader/writer.  
---|---  
[ExecuteInTransactionAsync](M_Tessa_Platform_Data_ITransactionStrategy_ExecuteInTransactionAsync.htm)|
Выполняет запрос на изменение карточки внутри транзакции. При этом не
используется блокировка reader/writer. Обычно транзакция открывается только в
том случае, если на этом соединении с БД отсутствует другая незакрытая
транзакция.  
(Унаследован от
[ITransactionStrategy](T_Tessa_Platform_Data_ITransactionStrategy.htm))  
[ExecuteInWriterLockAsync](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInWriterLockAsync.htm)|
Выполняет запрос на изменение карточки внутри блокировки reader/writer и
внутри транзакции. Последним действием внутри делегата asyncAction должно быть
увеличение номера версии карточки.  
[ReleaseWriterLockAsync](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ReleaseWriterLockAsync.htm)|
Выполняет освобождение блокировки на запись карточки.  
##  __См. также
#### Ссылки
[ICardTransactionStrategy -
](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
