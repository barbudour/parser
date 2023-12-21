# ICardStoreExtension - интерфейс
Расширение для процесса сохранения карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStoreExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardStoreExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardStoreExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardStoreExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeRequest.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
