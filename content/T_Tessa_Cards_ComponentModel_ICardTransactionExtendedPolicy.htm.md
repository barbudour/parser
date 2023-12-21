# ICardTransactionExtendedPolicy - интерфейс
Политика, обеспечивающая выполнение расширений в транзакционных действиях с
карточкой.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTransactionExtendedPolicy
VB __Копировать
     Public Interface ICardTransactionExtendedPolicy
C++ __Копировать
     public interface class ICardTransactionExtendedPolicy
F# __Копировать
     type ICardTransactionExtendedPolicy = interface end
##  __Методы
[AfterBeginTransactionAsync](M_Tessa_Cards_ComponentModel_ICardTransactionExtendedPolicy_AfterBeginTransactionAsync.htm)|
Метод, выполняющий расширения после начала транзакции, но перед выполнением
действий с карточкой.  
---|---  
[BeforeCommitTransactionAsync](M_Tessa_Cards_ComponentModel_ICardTransactionExtendedPolicy_BeforeCommitTransactionAsync.htm)|
Метод, выполняющий расширения перед коммитом транзакции после выполнения
действий с карточкой.  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
