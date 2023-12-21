# ICardGetFileContentExtension - интерфейс
Расширение для процесса получения контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardGetFileContentExtension : ICardExtension, 
    	IExtension
VB __Копировать
     Public Interface ICardGetFileContentExtension
    	Inherits ICardExtension, IExtension
C++ __Копировать
     public interface class ICardGetFileContentExtension : ICardExtension, 
    	IExtension
F# __Копировать
     type ICardGetFileContentExtension = 
        interface
            interface ICardExtension
            interface IExtension
        end
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_ICardGetFileContentExtension_AfterRequest.htm)|
Действие, выполняемое после получения контента файла как при успешном, так и
при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_ICardGetFileContentExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
контента файла как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_ICardGetFileContentExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением контента файла стандартными средствами.
Может установить ответ на запрос и функцию получения контента для того, чтобы
получение контента стандартными средствами не выполнялось.  
## __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
