# ICardRequestExtension - интерфейс
Расширение для процесса универсального взаимодействия с сервисом карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardRequestExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardRequestExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardRequestExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardRequestExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_ICardRequestExtension_AfterRequest.htm)|
Действие, выполняемое после универсального взаимодействия с сервисом карточек
как при успешном, так и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardRequestExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardRequestExtension_BeforeRequest.htm)|
Действие, выполняемое перед универсальным взаимодействием с сервисом карточек
стандартными средствами. Может установить ответ на запрос для того, чтобы
взаимодействие с сервисом карточек стандартными средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
