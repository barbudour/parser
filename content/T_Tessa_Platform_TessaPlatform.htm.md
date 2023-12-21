# TessaPlatform - класс
Обеспечивает доступ к зависимостям платформы, используемым в Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaPlatform
VB __Копировать
     Public NotInheritable Class TessaPlatform
C++ __Копировать
     public ref class TessaPlatform abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TessaPlatform = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaPlatform
##  __Свойства
[Dependencies](P_Tessa_Platform_TessaPlatform_Dependencies.htm)|  Зависимости
платформы от операционной системы, используемые в данный момент. По умолчанию
используются
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm)
без привязки к конкретному типу платформы. Рекомендуется установить значение
свойства в соответствии с используемой ОС, например, используя метод
[InitializeFromConfigurationAsync(Boolean, IConfigurationManager,
CancellationToken)](M_Tessa_Platform_TessaPlatform_InitializeFromConfigurationAsync.htm).  
---|---  
[ServerDependencies](P_Tessa_Platform_TessaPlatform_ServerDependencies.htm)|
Зависимости платформы от разновидности сервера, используемые в данный момент.
По умолчанию используются
[DefaultTessaServerDependencies](T_Tessa_Platform_DefaultTessaServerDependencies.htm)
без привязки к конкретному типу сервера. Рекомендуется установить значение
свойства в соответствии с используемым типом сервера, например, используя
метод [InitializeFromConfigurationAsync(Boolean, IConfigurationManager,
CancellationToken)](M_Tessa_Platform_TessaPlatform_InitializeFromConfigurationAsync.htm).  
## __Методы
[InitializeFromConfigurationAsync](M_Tessa_Platform_TessaPlatform_InitializeFromConfigurationAsync.htm)|
Выполняет инициализацию зависимостей от платформы в соответствии со
значениями, указанными в конфигурации. Рекомендуется вызвать метод до того,
как будут вызваны другие методы платформы. Также выполняет асинхронную
инициализацию конфигурации по умолчанию
[GetDefaultAsync(CancellationToken)](M_Tessa_Platform_ConfigurationManager_GetDefaultAsync.htm),
если configurationManager равен null и если инициализация ещё не выполнена.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
