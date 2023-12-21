# IConsoleRegistrator - интерфейс
Интерфейс, реализуемый в объектах регистраторов консольных команд. Помимо
интерфейса также требуется указать атрибут
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConsoleRegistrator : ISealable
VB __Копировать
     Public Interface IConsoleRegistrator
    	Inherits ISealable
C++ __Копировать
     public interface class IConsoleRegistrator : ISealable
F# __Копировать
     type IConsoleRegistrator = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[CommandContext](P_Tessa_Platform_ConsoleApps_IConsoleRegistrator_CommandContext.htm)|
Контекст команд, в котором выполняется регистрация.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы
[FinalizeRegistration](M_Tessa_Platform_ConsoleApps_IConsoleRegistrator_FinalizeRegistration.htm)|
Завершает регистрацию после того, как все команды инициализированы.  
---|---  
[InitializeRegistration](M_Tessa_Platform_ConsoleApps_IConsoleRegistrator_InitializeRegistration.htm)|
Инициализирует регистрацию перед тем, как какие-либо команды были добавлены.  
[RegisterCommands](M_Tessa_Platform_ConsoleApps_IConsoleRegistrator_RegisterCommands.htm)|
Выполняет регистрацию команд консоли в заданном объекте.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
