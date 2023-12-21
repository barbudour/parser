# ICardNewExtension - интерфейс
Расширение для процесса создания структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardNewExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardNewExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardNewExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardNewExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_ICardNewExtension_AfterRequest.htm)|
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardNewExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardNewExtension_BeforeRequest.htm)|
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
