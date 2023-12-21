# ChronosPlatform - класс
Обеспечивает доступ к зависимостям платформы, используемым в Chronos.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ChronosPlatform
VB __Копировать
     Public NotInheritable Class ChronosPlatform
C++ __Копировать
     public ref class ChronosPlatform abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ChronosPlatform = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ChronosPlatform
##  __Свойства
[Dependencies](P_Chronos_Platform_ChronosPlatform_Dependencies.htm)|
Зависимости платформы, используемые в данный момент. По умолчанию используются
[DefaultChronosPlatformDependencies](T_Chronos_Platform_DefaultChronosPlatformDependencies.htm)
без привязки к конкретному типу платформы.  
---|---  
## __Методы
[InitializeFromConfigurationAsync](M_Chronos_Platform_ChronosPlatform_InitializeFromConfigurationAsync.htm)|
Выполняет инициализацию зависимостей от платформы в соответствии со
значениями, указанными в конфигурации. Рекомендуется вызвать метод до того,
как будут вызваны другие методы платформы. Также выполняет асинхронную
инициализацию конфигурации по умолчанию
[GetDefaultAsync(CancellationToken)](M_Chronos_Platform_Configuration_ConfigurationManager_GetDefaultAsync.htm),
если configurationManager равен null и если инициализация ещё не выполнена.  
---|---  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
