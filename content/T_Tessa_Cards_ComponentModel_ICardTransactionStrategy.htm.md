# ICardTransactionStrategy - интерфейс
Стратегия обеспечения блокировок reader/writer при выполнении операций с
карточкой. SQL-транзакция открывается только в том случае, если на этом
соединении с БД отсутствует другая незакрытая транзакция.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTransactionStrategy : ITransactionStrategy
VB __Копировать
     Public Interface ICardTransactionStrategy
    	Inherits ITransactionStrategy
C++ __Копировать
     public interface class ICardTransactionStrategy : ITransactionStrategy
F# __Копировать
     type ICardTransactionStrategy = 
        interface
            interface ITransactionStrategy
        end
Implements
    [ITransactionStrategy](T_Tessa_Platform_Data_ITransactionStrategy.htm)
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
