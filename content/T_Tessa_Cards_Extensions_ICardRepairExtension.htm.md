# ICardRepairExtension - интерфейс
Расширение на исправление структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardRepairExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardRepairExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardRepairExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardRepairExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_ICardRepairExtension_AfterRequest.htm)|
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardRepairExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardRepairExtension_BeforeRequest.htm)|
Действие, выполняемое перед исправлением структуры карточки.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
