# IMenuActionCollectionVisual - интерфейс
Коллекция визуальных объектов, которая была сгенерирована посредством
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm). При выходе
из визуального дерева следует вызывать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для исправления утечек памяти.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMenuActionCollectionVisual : IDisposable
VB __Копировать
     Public Interface IMenuActionCollectionVisual
    	Inherits IDisposable
C++ __Копировать
     public interface class IMenuActionCollectionVisual : IDisposable
F# __Копировать
     type IMenuActionCollectionVisual = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[FrameworkElements](P_Tessa_UI_Menu_IMenuActionCollectionVisual_FrameworkElements.htm)|
Сгенерированные объекты, которые должны быть отображены в визуальном дереве
WPF с сохранением порядка следования.  
---|---  
## __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
