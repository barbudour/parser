# IInputBinding - интерфейс
Привязка команды к жесту (нажатию клавиши или клику мыши).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IInputBinding : IEquatable<IInputBinding>, 
    	IEquatable<InputBinding>
VB __Копировать
     Public Interface IInputBinding
    	Inherits IEquatable(Of IInputBinding), IEquatable(Of InputBinding)
C++ __Копировать
     public interface class IInputBinding : IEquatable<IInputBinding^>, 
    	IEquatable<InputBinding^>
F# __Копировать
     type IInputBinding = 
        interface
            interface IEquatable<IInputBinding>
            interface IEquatable<InputBinding>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IInputBinding>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)>
##  __Свойства
[Command](P_Tessa_UI_IInputBinding_Command.htm)| Команда.  
---|---  
[Gesture](P_Tessa_UI_IInputBinding_Gesture.htm)| Жест, связанный с командой.
Обычно нажатие клавиши или клик мыши.  
##  __Методы
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IInputBinding>)  
---|---  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)>)  
##  __Методы расширения
[CreateWpfBinding](M_Tessa_UI_UIExtensions_CreateWpfBinding.htm)|  Создаёт
объект привязки
[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)
для использования в WPF. Вызывайте в потоке диспетчера WPF.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
