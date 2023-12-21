# HostExtensions - класс
Методы-расширения для пространства имён Host.
## __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class HostExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class HostExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class HostExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type HostExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HostExtensions
##  __Методы
[RegisterHostLauncher](M_Tessa_Host_HostExtensions_RegisterHostLauncher.htm)|
Регистрирует реализацию интерфейса
[IHostLauncher](T_Tessa_Host_IHostLauncher.htm) для запуска дочерних процессов
TessaHost и объект
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
для генерации адресов. Требуется зарегистрированный объект
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm), для чего
обычно используется метод RegisterProcessManager(IUnityContainer).  
---|---  
## __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
