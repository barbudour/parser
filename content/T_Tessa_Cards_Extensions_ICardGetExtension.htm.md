# ICardGetExtension - интерфейс
Расширение для процесса получения карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardGetExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardGetExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardGetExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardGetExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_ICardGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
