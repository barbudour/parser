# IMenuActionVisual - интерфейс
Визуальный объект, который был сгенерирован посредством
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm). При выходе
из визуального дерева следует вызывать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для исправления утечек памяти.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMenuActionVisual : IDisposable
VB __Копировать
     Public Interface IMenuActionVisual
    	Inherits IDisposable
C++ __Копировать
     public interface class IMenuActionVisual : IDisposable
F# __Копировать
     type IMenuActionVisual = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[FrameworkElement](P_Tessa_UI_Menu_IMenuActionVisual_FrameworkElement.htm)|
Сгенерированный объект, который должен быть отображён в визуальном дереве WPF.  
---|---  
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
