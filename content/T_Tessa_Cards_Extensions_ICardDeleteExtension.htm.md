# ICardDeleteExtension - интерфейс
Расширение для процесса удаления карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardDeleteExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardDeleteExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardDeleteExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardDeleteExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterRequest.htm)|
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeRequest.htm)|
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
