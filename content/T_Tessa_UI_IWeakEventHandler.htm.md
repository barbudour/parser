# IWeakEventHandler - интерфейс
Описание интерфейса обработчика событий от централизованного диспетчера
событий
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWeakEventHandler : IWeakEventListener
VB __Копировать
     Public Interface IWeakEventHandler
    	Inherits IWeakEventListener
C++ __Копировать
     public interface class IWeakEventHandler : IWeakEventListener
F# __Копировать
     type IWeakEventHandler = 
        interface
            interface IWeakEventListener
        end
Implements
    [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener)
##  __Методы
[ReceiveWeakEvent](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener.receiveweakevent#system-
windows-iweakeventlistener-receiveweakevent\(system-type-system-object-system-
eventargs\))| Receives events from the centralized event manager.  
(Унаследован от
[IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener))  
---|---  
[SkipEvents](M_Tessa_UI_IWeakEventHandler_SkipEvents.htm)|  Осуществляет
запрет обработки событий поступающих от централизованного обработчика событий.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
