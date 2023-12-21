# IApplicationExtension - интерфейс
Расширение, связанное с жизненным циклом приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationExtension : IExtension
VB __Копировать
     Public Interface IApplicationExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IApplicationExtension : IExtension
F# __Копировать
     type IApplicationExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[Initialize](M_Tessa_Platform_Runtime_IApplicationExtension_Initialize.htm)|
Метод, выполняемый при инициализации приложения, когда основные подсистемы уже
инициализированы.  
---|---  
[Shutdown](M_Tessa_Platform_Runtime_IApplicationExtension_Shutdown.htm)|
Метод, выполняемый при завершении работы приложения.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
